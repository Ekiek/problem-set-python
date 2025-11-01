import random

def main():
    number = random.randint(0,100)
    while True:
        guess_number = int(input("Enter number: ").strip())
        print(number)
        if guess_number == number:
            print ("you guessed")
            break
        elif guess_number > number:
            print("Too large!")
        elif guess_number < number:
            print("Too small!")
        else:
            print("please enter the number")
        
if __name__ == "__main__":
    main()