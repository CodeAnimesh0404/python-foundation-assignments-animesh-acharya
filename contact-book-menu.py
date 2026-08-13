#Exercise: Contact Book Menu
#Student: Animesh Acharya
#Day: 2
#Exercise: Stretch

contacts = {}

def display_menu():
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Display all contacts")
    print("5. Exit")


def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email
    }
    print(f"Contact '{name}' added successfully.")


def search_contact():
    name = input("Enter the name to search: ").strip()

    if name in contacts:
        details = contacts[name]
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
    else:
        print(f"No contact found with the name '{name}'.")


def delete_contact():
    name = input("Enter the name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"No contact found with the name '{name}'.")


def display_all_contacts():
    if not contacts:
        print("No contacts saved yet.")
        return

    for name, details in contacts.items():
        print(f"Name: {name} | Phone: {details['phone']} | Email: {details['email']}")


# Main program loop

while True:
    display_menu()
    choice = input("Select an option (1-5): ").strip()

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        display_all_contacts()
    elif choice == "5":
        print("Exiting contact book. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a number between 1 and 5.")