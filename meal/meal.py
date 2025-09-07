def main():
    time = convert(input("What time is it? "))
    if 7 <= time  <= 8:
        print("Breakfast")
    elif 12 <= time  <= 13:
        print("lunch")
    elif 18 <= time  <= 19:
        print("dinner")


def convert(time):
    hour, minute = time.split(":")
    hour = int(hour)
    minute = float(minute)/60
    return hour + minute

if __name__ == "__main__":
    main()