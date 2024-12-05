
from contact_manager import add_contacts, view_contacts, remove_contacts, search_contacts

while True:
    print("\n<<Wellcome to Contact Book Management System>>\n")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Remove Contact")
    print("4. Search Contact")
    print("5. Exit\n")

    choice = input("Enter your choice: ")
    if choice == "1":
        add_contacts("Name", "Email", "Phone_number","Address")


    elif choice == "2":
        view_contacts()

    elif choice == "3":
        index = int(input("Enter the index of the contact to remove: "))
        remove_contacts(index)
        print("Contact removed successfully...")

    elif choice == "4":
        query = input("Enter the search query(avoid zero(0) at first if it is a integer) : ")
        search_contacts(query)


    elif choice == "5":
        print("Thanks for using Contact Manager Book.. ")
        break

    else:
        print("Invalid Choice")