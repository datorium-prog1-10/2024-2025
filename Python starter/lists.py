names = ['Anna', 'Oskars', 'Jennifer']

# for name in names:
#    print(f"Hey hey {name}!")

ages = [16, 15, 21]

university = [False, False, True]

personal_data = [
    ['Anna', 16, False, 'anna@somemail.com'],
    ['Oskars', 15, False, 'oskars@bestemail.com'],
    ['Jennifer', 21, True, 'jenni@ggmail.com'],
    ['Jānis', 18, True, 'jj@fastemail.com']
]

name = input('Enter your name: ')
age = int(input('Enter your age: '))
university = input('Are you in university? (yes/no): ').lower() == 'yes'
email = input('Enter your email: ')

new_data = [name, age, university, email]
personal_data.append(new_data)

for rinda in personal_data:
    # te varētu būt programm kas aizsūtīs ziņas uz tiem e-pastiem
    print(f"Aizsūtam e-pastu uz adresi {rinda[3]}")