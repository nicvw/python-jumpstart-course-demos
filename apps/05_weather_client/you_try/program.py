"""Print out all the respositories of a given github user."""
import bs4
import requests


class CustomException(Exception):
    """Custom exception because we don't like generic exceptions."""
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

def main():
    """Main entry point for execution."""
    print_header()
    username = input('Enter the user you would like to search: ')

    try:
        data = get_html_from_web(username)
    except CustomException as err:
        print("Unable to read repositories for '{}', {}".format(username, str(err)))
    else:
        repos = get_repositories_from_html(data)
        display_repositories(username, repos)


def print_header():
    """A header message for out application."""
    print('-' * 40)
    print('              GITHUB APP')
    print('-' * 40)


def get_html_from_web(user):
    """Download the repositories page for the given user from github."""
    url = 'https://github.com/{}?tab=repositories'.format(user)
    response = requests.get(url)
    if response.status_code != 200:
        raise CustomException("failed with {}".format(response.status_code))
    return response.text



def get_repositories_from_html(html):
    """Parse the page and extract the names of all the user's repositories."""
    soup = bs4.BeautifulSoup(html, 'html.parser')
    return [ x.get('href') for x in soup.find(id='user-repositories-list').findAll('a')]


def display_repositories(username, list_of_repos):
    """Print the repositories with a pointless header."""
    print("Github user '{}' has the following repositories:".format(username))
    for repo in list_of_repos:
        print("\t" + repo)


if __name__ == '__main__':
    main()
