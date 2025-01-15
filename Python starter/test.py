# IZVĒLNE (MENU)
# 1 - pirvirnot jaunu kontaktu
# 2 - izvadīt visus kontaktus
# 3 - izdzēst kontaktu
# 0 - iziet no programmas

contacts = [['Anna', '987654321'], ['Oskars', '123456789'], ['Jenifere', '654987321']]

while True:
    response = input("izvēlies darbību 1-pievienot, 2-izvadīt, 3-izdzēst, 0-iziet: ")

    if response == '1':
        print('pievienosim jaunu kontaktu')
        name = input('ievadi vārdu: ')
        number = input('ievadi numuru: ')
        contacts.append([name, number])
    elif response == '2':
        print('izvadīsim visus kontaktus')
        print(contacts)
        for contact in contacts:
            print(f"{contact[0]} {contact[1]}")
        
    elif response == '3':
        print('izdzēsīsim kādu kontaktu')
    elif response == '0':
        print('iziesim no programmas')
        break