"""File IO for our journal application."""
import os


def save(name, data):
    """Save the journal to disk."""

    filename = _journal(name)
    print('... saving journal to {}'.format(filename))
    with open(os.path.join(filename), 'w') as fhl:
        for entry in data:
            fhl.write(entry + '\n')


def load(name):
    """Load the journal from disk."""
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
    """Add an entry to the journal."""
    text = text.strip()
    if text:
        data.append(text)


def _journal(name):
    """Return the absolute path to the journal."""
    return os.path.abspath(os.path.join('.', 'journal', name))
