def main():
    text = input("Type your text here: ")
    text = convert(text)
    print(text)

def convert(text):
    txt = text.replace(":)","🙂").replace(":(","🙁")
    return txt

main()