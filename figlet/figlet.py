from pyfiglet import Figlet
import random
import sys

def main():
    figlet = Figlet()
    args = sys.argv[1:]

    if len(args) == 0:
        fonts = figlet.getFonts()
        figlet.setFont(font=random.choice(fonts))

    elif len(args) == 2 and args[0] in ["-f", "--font"]:
        font_name = args[1]
        fonts = figlet.getFonts()
        if font_name not in fonts:
            sys.exit("Invalid font")
        figlet.setFont(font=font_name)

    else:
        sys.exit("Invalid usage")

    text = input("Input: ")
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()