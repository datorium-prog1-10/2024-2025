import csv

file_path = 'spotify.csv'

# UZDEVUMS 1:
# Blinding Lights - The Weeknd
# Shape of You - Ed Sheeran
# ...

with open(file_path, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)     
    for row in csv_reader:
        print(f"{row[0]} - {row[1]}")


# UZDEVUMS 2:
# Aprēķināt vidējo dziesmas garumu no visiem esošiem datiem

total_duration = 0
track_count = 0

with open(file_path, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)    
    for row in csv_reader:
        try:
            total_duration += int(row[4])
            track_count += 1
        except:
            continue
    
print(f"Average song duration is: {total_duration / track_count} ms")