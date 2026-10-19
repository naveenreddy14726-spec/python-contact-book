# Python Contact Book

A simple, menu-driven contact book written in Python. It lets you add, view,
edit, and delete contacts from the command line.

## Features

- Add a contact with a name and phone number.
- View all saved contacts.
- Edit an existing contact's phone number.
- Delete a contact.
- Validate that names and phone numbers are not blank.
- Prevent duplicate contact names and direct you to edit the existing contact.

## Requirements

- Python 3.6 or later
- No third-party packages are required.

## Run the program

Open a terminal in the project folder and run:

```bash
python contact_book_copy.py
```

If your system uses `python3` to launch Python, run:

```bash
python3 contact_book_copy.py
```

## Using the menu

Choose an option by entering its number:

1. **Add Contact** — enter a name and phone number.
2. **View Contacts** — display all contacts.
3. **Edit Contact** — update the phone number for an existing name.
4. **Delete Contact** — remove a contact by name.
5. **Exit** — close the program.

Names are trimmed of leading and trailing spaces. Each name can only be added
once; use **Edit Contact** to change the phone number for an existing name.

## Data storage

Contacts are stored in memory while the program is running. They are not saved
to a file or database, so contacts are cleared when you exit the program.