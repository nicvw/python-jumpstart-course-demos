"""
This is the journal module.

It provides functionality for loading and saving a journal to disk.
"""
import os


def save(name, data):
    """
    This method saves a journal to disk

    :param name: The base name of the journal to save.
    :param data: The journal data to save to disk.
    """

    filename = _journal(name)
    print('... saving journal to {}'.format(filename))
    with open(os.path.join(filename), 'w') as fhl:
        for entry in data:
            fhl.write(entry + '\n')


def load(name):
    """
    This method creates and loads a new journal.

    :param name: The base name of the journal to load.
    :return: A new journal data structure populated with the file data.
    """
    data = []
    filename = _journal(name)
    try:
        with open(filename) as fhl:
            print('... loading journal from {}'.format(filename))
            for entry in fhl:
                data.append(entry.rstrip('\n'))
    except FileNotFoundError:
        print('... starting a new journal')
    return data


def add_entry(text, data):
    """
    Add an entry to the journal data structure.

    :param text: The text data to add to the data structure.
    :param data:  An instance of journal data structure (just a list).
    """
    text = text.strip()
    if text:
        data.append(text)


def _journal(name):
    """
    Return the absolute path to the journal.

    :param name: The base name of the journal.
    :return: An absolute filepath to the journal's location on disk.
    """
    return os.path.abspath(os.path.join('.', 'journal', name))
