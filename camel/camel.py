text = input("type your text here: ")

new_text = ""

for i in text:
    if i.isupper():
        new_text += "_" + i.lower()
    else:
        new_text += i

print(new_text)