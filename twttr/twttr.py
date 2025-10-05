text = input("Type your text here: ")

result = ""

for character in text:
    if character not in ["A","E", "I", "O", "U", "a", "e", "i", "o", "u"]:
        result += character

print(result)

