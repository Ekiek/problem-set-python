def main():
    text = input("Type your text here: ")
    print(shorten(text))


def shorten(word):
    result = ""
    for character in word:
        if character not in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]:
            result += character
    return result


if __name__ == "__main__":
    main()

