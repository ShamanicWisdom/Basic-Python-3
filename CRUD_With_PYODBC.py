# A very simple CRUD console application using pyodbc API module.
# Database type: Microsoft SQL Server.
# Database name: PythonDB.
# Database content: one simple table named Contacts (3 columns: Name (varchar(50)), Surname (varchar(50)), Number (int)
# and Primary Key column named PrimaryKey - with auto incrementation implemented).
# PYODBC (Python Open Database Connector) needs to have Visual C++ 2014 installed in order to work properly.
import pyodbc

# Initializing a connection with Database.
connection = pyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-L00KIJH;' 'Database=PythonDB;')
# initializing a cursor for fetching SQL queries.
cursor = connection.cursor()


# Creating a new Contact.
def add_a_contact():
    while True:
        try:
            print("Adding a new contact:")
            name = input("Type a name: ")
            surname = input("Type a surname: ")
            number = input("Type a phone number: ")
            # Check if number can be a real number (digits only) - if not, ValueError will be thrown.
            int_value = int(number)
            if name == "":
                print("Please type a name!\n")
            elif surname == "":
                print("Please type a surname!\n")
            else:
                cursor.execute("insert into Contacts (name, surname, number) values ('" + name + "','" + surname + "'," + number + ")")
                cursor.commit()
                break
        except ValueError:
            print("Please insert  proper phone number!")


# Reading all Contacts.
def read_contacts():
    print()
    print("All contacts: ")
    print("Key\t\tName\t\tSurname\t\tNumber")
    cursor.execute('select * from Contacts')
    if cursor.rowcount != 0:
        for row in cursor:
            print(str(row.PrimaryKey) + "\t\t" + row.Name + "\t\t" + row.Surname + "\t\t" + str(row.Number))
        print()
    else:
        print("No records in Phone Book.\n")


# Updating an existing Contact.
def edit_a_contact():
    while True:
        try:
            print("Editing a contact (type 0 to cancel this process):")
            key_number = int(input("Type a key number of contact:"))
            if key_number == 0:
                break
            else:
                cursor.execute("select * from Contacts where PrimaryKey = " + str(key_number))
                # If Contact exists:
                if cursor.rowcount != 0:
                    try:
                        print("(Press enter if you don't want to edit a field).")
                        new_name = input("Type a new name: ")
                        new_surname = input("Type a new surname: ")
                        new_number = input("Type a new phone number: ")
                        edit_name = False
                        edit_surname = False
                        edit_number = False
                        if new_name != "":
                            edit_name = True
                        if new_surname != "":
                            edit_surname = True
                        if new_number != "":
                            # Check if number can be a real number (digits only) - if not, ValueError will be thrown.
                            new_number_value = int(new_number)
                            edit_number = True
                        if edit_name is False and edit_surname is False and edit_number is False:
                            print("Nothing to edit here.")
                        else:
                            # Building a proper query.
                            query_builder = "update Contacts set "
                            if edit_name is True:
                                query_builder += "Name = '" + new_name + "' "
                            if edit_surname is True:
                                if edit_name is True:
                                    query_builder += ","
                                query_builder += "Surname = '" + new_surname + "' "
                            if edit_number is True:
                                if edit_name is True or edit_surname is True:
                                    query_builder += ","
                                query_builder += "Number = " + new_number
                            query_builder += " where PrimaryKey = " + str(key_number)
                            cursor.execute(query_builder)
                            cursor.commit()
                            print("Contact modified successfully.\n")
                            break
                    except ValueError:
                        print("Please insert a proper phone number!")
                else:
                    print("No record with the PrimaryKey = " + key_number + " in Phone Book.\n")
        except ValueError:
            print("Please insert a proper number of PrimaryKey!")


# Deleting chosen Contact.
def delete_a_contact():
    while True:
        try:
            print("Deleting a contact (Type 0 to cancel this process):")
            key_number = int(input("Type a key number of contact:"))
            if key_number == 0:
                break
            else:
                cursor.execute("select * from Contacts where PrimaryKey = " + str(key_number))
                if cursor.rowcount != 0:
                    row = cursor.fetchone()
                    while True:
                        delete_confirmation = input("Are you sure to delete this contact (" + row.Name + " " + row.Surname + ")? (Y/N): ")
                        if delete_confirmation == "Y" or delete_confirmation == "y":
                            cursor.execute("delete from Contacts where PrimaryKey = " + str(key_number))
                            cursor.commit()
                            print("Delete process finished successfully.")
                            break
                        elif delete_confirmation == "N" or delete_confirmation == "n":
                            print("Delete process aborted.")
                            break
                        else:
                            print("Please input a correct confirmation symbol!")
                else:
                    print("No record with the PrimaryKey = " + str(key_number) + " in Phone Book.\n")
        except ValueError:
            print("\nProgram will accept only integer numbers as an user choice!\n")


# Exit.
def exit_the_program():
    print("Exiting the program...")
    exit()


# Dictionary - binding function name to specific number.
all_functions = {1: read_contacts, 2: add_a_contact, 3: edit_a_contact, 4: delete_a_contact, 0: exit_the_program}


# Core application loop.
print("==Simple CRUD Application (Phone Book)==")
while True:
    try:
        print("1. Read Phone Book Content.")
        print("2. Add a new Phone Contact.")
        print("3. Edit a Phone Contact.")
        print("4. Delete a Phone Contact.")
        print("0. Exit.")
        user_choice = int(input("Please input a number: "))
        all_functions[user_choice]()
    except ValueError:
        print("\nProgram will accept only integer numbers as an user choice!\n")
    except KeyError:
        print("\nNo function is binded to this number! Try again.\n")
