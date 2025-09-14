change = int(input("pay with coins: "))

while change != 50:
    new_change = int(input(f"please add {50 - change}: "))
    change += new_change
    if change < 50:
        print(f"your change is {50 - change}")
    else:
        break