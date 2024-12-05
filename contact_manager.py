
from storage import save_contacts, load_contacts

def add_contacts(Name, Email, Phone_number,Address):
    contacts = load_contacts()

    Name = input("Enter your Contact name: ")
    Email = input("Enter your Contact's E-mail: ")
    for mail in contacts:
        if mail ['Email'] == Email:
            print("This Email is already exist..Try again")
            return

    Phone_number = int(input("Enter your contact's Phone Number: "))
    for num in contacts:
        if num ['Phone_number'] == Phone_number:
            print("This number is exist in another contact's.. Try again")
            return

    Address = input("Enter your contact's address: ")

    print("Contact details added successfully!")


    contact = {
        'Name':Name,
        'Email':Email,
        'Phone_number':Phone_number,
        'Address':Address,
    }


    contacts.append(contact)
    save_contacts(contacts)


def view_contacts():
    contacts = load_contacts()
    print("\nContacts List: \n")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['Name']}, E-mail: {contact['Email']}, Phone_number: {contact['Phone_number']}, Address: {contact['Address']} ")
def remove_contacts(index):

    contacts = load_contacts()
    if 0<index<=len(contacts):
        del contacts[index-1]
        save_contacts(contacts)
    else:
        print("Invalid Index")


def search_contacts(query):
    contacts = load_contacts()  # Load contacts from the file or memory
    results = []

    # Iterate over the contacts and search for the query
    for contact in contacts:
        if (
                query.lower() in contact['Name'].lower() or
                query.lower() in contact['Email'].lower() or
                query in contact['Phone_number'] or
                query.lower() in contact['Address'].lower()
        ):
            results.append(contact)

def search_contacts(query):
    contacts = load_contacts()  # Load contacts from the file or memory
    results = []

    # Iterate over the contacts and search for the query
    for contact in contacts:
        if (
            query.lower() in contact['Name'].lower() or
            query.lower() in contact['Email'].lower() or
            query in str(contact['Phone_number']) or  # Convert Phone_number to string
            query.lower() in contact['Address'].lower()
        ):
            results.append(contact)

    # Display the search results
    if results:
        print("\nSearch Results:\n")
        for i, contact in enumerate(results, start=1):
            print(f"{i}. Name: {contact['Name']}, Email: {contact['Email']}, "
                  f"Phone Number: {contact['Phone_number']}, Address: {contact['Address']}")
    else:
        print("No matching contacts found.")


