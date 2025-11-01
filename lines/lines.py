import sys
import os


def main():
    if len(sys.argv) != 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    if not os.path.isfile(filename):
        sys.exit("File does not exist")
    try:
        with open(filename) as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File not found")

    count = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("#"):
            continue
        count += 1

    print(count)

if __name__ == "__main__":
    main()

