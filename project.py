phonebook = {}

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    if name and phone:
        phonebook[name] = phone
        print("Contact added.")
    else:
        print("Name and phone cannot be empty.")

def search_contact():
    name = input("Enter name to search: ").strip()
    print(phonebook.get(name, "Contact not found."))

def update_contact():
    name = input("Enter name to update: ").strip()
    if name in phonebook:
        phone = input("Enter new phone: ").strip()
        if phone:
            phonebook[name] = phone
            print("Contact updated.")
        else:
            print("Phone cannot be empty.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ").strip()
    if phonebook.pop(name, None):
        print("Contact deleted.")
    else:
        print("Contact not found.")

def display_contacts():
    if phonebook:
        print("Contacts:")
        for name, phone in phonebook.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts.")

def main():
    while True:
        print("\n1. Add  2. Search  3. Update  4. Delete  5. Display  6. Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1': add_contact()
        elif choice == '2': search_contact()
        elif choice == '3': update_contact()
        elif choice == '4': delete_contact()
        elif choice == '5': display_contacts()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

main()