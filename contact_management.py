contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    address = input("Enter contact address: ")
    
    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print(f"Contact {name} added successfully.\n")

def view_contacts():
    if contacts:
        print("Contact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")
    else:
        print("No contacts available.\n")

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found_contacts = [name for name, details in contacts.items() if search_term in name or search_term in details['phone']]
    
    if found_contacts:
        for name in found_contacts:
            print(f"Name: {name}, Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}, Address: {contacts[name]['address']}")
    else:
        print("No contact found.\n")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        
        contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print(f"Contact {name} updated successfully.\n")
    else:
        print("Contact not found.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.\n")
    else:
        print("Contact not found.\n")

def display_menu():
    print("Contact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.\n")

if _name_ == "_main_":
    main()


# Contact Management System
# 1. Add Contact
# 2. View Contact List
# 3. Search Contact
# 4. Update Contact
# 5. Delete Contact
# 6. Exit
# Choose an option: 1
# Enter contact name: pragati
# Enter contact phone number: 93456 78654
# Enter contact email: codsoft123@gmail.com
# Enter contact address: madurai
# Contact pragati added successfully.
