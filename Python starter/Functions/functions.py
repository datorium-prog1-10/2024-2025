import math

def greetings(greeting, name):
    print(f"{greeting} {name}!")

def add(a, b):
    print(f"Summa ir: {a + b}")

# UZDEVUMS
# Izveido funkciju kas atkarīgi no
# simbolu skaita dotajā vārdā izvada vērtības:
# 'īss', ja simbolu skaits ir mazāk par 5
# 'viedējais', ja simbolu skaits ir mazāk par 10
# 'garš', ja simbolu skaits ir 10 vai vairāk

def classify_word_length(word):
    length = len(word)

    if length < 5:
        response = "īss"
    elif length < 10:
        response = "vidējais"
    else:
        response = "garš"

    print(f"Vārdam '{word}' ir {length} simbolu un garums ir {response}")

#classify_word_length(input('Uzrasti kādu vārdu: '))


def funkcija(name:str, age:int):
    print(f"Cau {name}! You are {age} years old.")



from datetime import datetime

def calculate_age(name: str, birthdate: str):
    """
    Calculate and print the age of a person given their name and birthdate in decimal format rounded to 2 decimal places.
    
    :param name: Name of the person
    :param birthdate: Birthdate in 'YYYY-MM-DD' format
    """
    birth_date = datetime.strptime(birthdate, "%Y-%m-%d").date()
    today = datetime.today().date()
    age_days = (today - birth_date).days
    age_years = round(age_days / 365.25, 2)  # Accounting for leap years
    
    print(f"{name} is {age_years} years old.")

# Example usage
#calculate_age("Alice", "2006-05-15")


grades = [4, 6, 8, 5, 9, 5, 8, 7, 10, 9, 8]

# man vajag aprēķināt vidējo atzīmi
# 1. aprēķinam summu
# 2. aprēķinam cik elemnti man ir sarakstā
# 3. Aprēķinam vidējo vērtību

def list_sum(list_to_sum: list):
    sum = 0
    for list_element in list_to_sum:
        sum += list_element

    return sum

def list_length(list_with_numbers: list):
    return len(list_with_numbers)


def potential_energy(m: float, h: float, g: float = 9.8):
    return m*g*h

def kinetic_energy(m: float, V: float):
    return 1/2 * m * V ** 2

def kmph_to_mps(kmph: float):
    return kmph/3.6

print(kinetic_energy(2500, kmph_to_mps(70)))


# UZDEVUMS
# Izveido funkciju kas pieņem cilvēka v\ardu un uzvārdu kopā
# atgriež sarakstā vārdu un uzvārdu kā atsevišķus elementus

# Input: Anna Marija Bērziņa
# Return: ['Anna', 'Marija', 'Bērziņa']

def split_text():
    full_name = input("Uzraksti savu pilno vārdu: ")
    splitted_text = full_name.split()
    return splitted_text

print(split_text())