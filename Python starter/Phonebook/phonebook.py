# IZVĒLNE (MENU)
# 1 - pievienot jaunu kontaktu
# 2 - izvadīt visus kontaktus
# 3 - izdzēst kontaktu
# 0 - iziet no programmasD

import json

contacts = [['Anna', '987654321'], ['Oskars', '123456789'], ['Jenifere', '654987321']]

# UZDEVUMS# Ielasi datus no contacts.json uz šo vārdnīcu:
# Tev ir 5 minūtes :)
with open('Phonebook/contacts.json', 'r', encoding="utf-8") as file:
    contacts_dictionary = json.load(file)

while True:
    response = input("Izvēlies darbību 1-pievienot, 2-izvadīt, 3-izdēst, 0-iziet: ")

    if response == '1':
        print('Pievienosim jaunu kontaktu')
        name = input("Ievadi vārdu: ")
        number = input("Ievadi numuru: ")

        contact = {
            "name": name,
            "phone": number
        }
        contacts_dictionary["contacts"].append(contact)

    elif response == '2':
        print('Izvadīsim visus kontaktus')
        for contact in contacts_dictionary["contacts"]:
            print(contact)

    elif response == '3':
        print('Izdzēsisim kādu kontaktu')
    
    elif response == '0':
        filename = "Phonebook/contacts.json" #svarīgi, jo tas ir faila nosaukums

        with open(filename, "w") as json_file:
            json.dump(contacts_dictionary, json_file, indent=4)
        
        print('Dati ir saglabāti, Iziesim no programmas')
        break
    else:
        print('Šadas izvēles nav!')