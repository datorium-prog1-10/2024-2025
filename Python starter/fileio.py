file = open("rindas.txt", "w", encoding="UTF-8")

for i in range(1, 101):
    text = f"Rinda {i}\n"
    file.write(text)

file.close