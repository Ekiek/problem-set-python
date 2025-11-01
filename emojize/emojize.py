import emoji

emoj = input("Enter value: ")
convert_emoj = emoji.emojize(emoj, language='alias')
print(convert_emoj)