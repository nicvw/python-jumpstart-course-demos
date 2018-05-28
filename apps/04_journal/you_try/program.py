"""A simple file-backed journal."""
import journal


def main():
    """Entrypoint into application."""
    print_header()
    run_event_loop()


def print_header():
    """Print the welcome header."""
    print('-------------------------')
    print('      JOURNAL APP')
    print('-------------------------')


def run_event_loop():
    """The main execution loop of our application."""
    cmd = None
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while cmd != 'x':
        print('What do you want to do with your journal?')
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()
        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x':
            print("'{}' is an unknown command".format(cmd))

    journal.save(journal_name, journal_data)
    print('Done, goodbye')


def list_entries(data):
    """Print out existing entries in our journal."""
    for idx, entry in enumerate(data, 1):
        print('{0}: {1}'.format(idx, entry))


def add_entry(data):
    """Add a new entry into the journal."""
    text = input('Type your entry, <enter> to exit: ')
    if text:
        journal.add_entry(text, data)


if __name__ == '__main__':
    main()
