contacts = []

# Add Contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    
    contacts[name] = phone
    print(" Contact added!\n")


# View Contacts
def view_contacts():
    if not contacts:
        print(" No contacts found.\n")
    else:
        print("\n--- Contact List ---")
        for name, phone in contacts.items():
            print(f"Name: [name] | Phone: [phone]")
        print()


# Edit Contact
def edit_contact():
    name = input("Enter name to edit: ")
    
    if name in contacts:
        phone = input("Enter new phone number: ")
        contacts[name] = phone
        print(" Contact updated!\n")
    else:
        print(" Contact not found.\n")


# Delete Contact
def delete_contact():
    name = input("Enter name to delete: ")
    
    if name in contacts:
        del contacts[name]
        print(" Contact deleted!\n")
    else:
        print(" Contact not found.\n")


# Main Menu
while True:
    print("===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        edit_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print(" Bye!")
        break
    else:
        print(" Invalid choice\n")