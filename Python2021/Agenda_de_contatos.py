CONTACTS = {}

CONTACTS['Daniel'] = {
    'telephone': '992193213922',
    'email': 'leao.daniel@hotmail.com',
    'address': 'viela celia, 687',
}

CONTACTS['Maria'] = {
    'telephone': '919192312321',
    'email': 'maria@gmail.com',
    'address': 'av. nazare, 348',
}

CONTACTS['João'] = {
    'telephone': '',
    'email': '',
    'address': '',
}


def search_contact(contact):
    try:
        print('Name:', contact)
        print('Telephone:', CONTACTS[contact]['telephone'])
        print('Email:', CONTACTS[contact]['email'])
        print('Adress:', CONTACTS[contact]['address'])
        print("-----------------------")
    except KeyError:
        print()
        print(">>>>>>  Oops!  That was no valid name.  Try again...")
        print()
    except Exception as error:
        print('>>>>>> an unexpected error has occurred')
        print(error)


def show_all_contacts():
    if CONTACTS:  # verifica se CONTACTS existe. evita erro de logica caso CONTACTS não exista
        for contact in CONTACTS:
            print("-----------------------")
            search_contact(contact)
    else:
        print('>>>>>  There is no contact book!')


def add_edit_contact(contact):
    telephone = input("Enter a contact telephone: ")
    email = input("Enter a contact email: ")
    address = input("Enter a contact address: ")
    CONTACTS[contact] = dict(telephone=telephone, email=email, address=address)  # usei dict constructor

def delete_contact(name):
    try:
        CONTACTS.pop(name)
        print()
        print(f">>>>>>  Contact {name} was successfully deleted! ")
        print()
    except:
        print(">>>>>>  Invalid contact!")


#add_edit_contact('Joana', '912903190', None, None)


def show_menu():
    print("-----------------------")
    print('1 - Show all contacts')
    print('2 - Search contact')
    print('3 - Add contact')
    print('4 - Edit contact')
    print('5 - delete contact')
    print('0 - Close contact book')
    print("-----------------------")


while True:
    show_menu()
    option = input('Choose an option:')
    if option == "1":
        show_all_contacts()

    elif option == "2":
        contact = input("Enter a contact name: ")
        search_contact(contact)

    elif option == "3":
        contact = input("Enter a contact name: ")
        try:
            CONTACTS[contact]  # verifica se o contato existe. para diferenciar editar e adicionar!
            print('>>>>>  Contact already exists!')
        except:
            print('>>>>>  Adding contact ', contact)
            add_edit_contact(contact)
            print(f">>>>>>  Contact {contact} has been successfully added! ")

    elif option == "4":
        contact = input("Enter a contact name: ")
        try:
            CONTACTS[contact]  # verifica se o contato existe.
            print('>>>>>  Editing contact!')
            add_edit_contact(contact)
            print(f">>>>>>  Contact {contact} has been successfully edited! ")
        except:
            print('>>>>>  Contact already exists!')
            pass

    elif option == "5":
        contact = input("Enter a contact name: ")
        delete_contact(contact)

    elif option == "0":
        print(">>>>>>  Closing the program!")
        break

    else:
        print('>>>>>>  Invalid option')
