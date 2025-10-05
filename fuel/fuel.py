while True:
    try:
        fuel = input("Enter x/y: ")

        x, y = fuel.split("/")
        x = int(x)
        y = int(y)

        if x < 0 or y <= 0:
            raise ValueError
        if x > y:
            raise ValueError
        fuellevel = round(x / y * 100)

        if fuellevel <= 1:
            print("E")
        elif fuellevel >= 99:
            print("F")
        else:
            print(f"{fuellevel}%")
        break

    except ZeroDivisionError:
        print("y must not be 0, try again.")
    except ValueError:
        print("Invalid input, try again.")