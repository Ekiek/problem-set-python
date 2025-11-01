# 
# რომელიც მომხმარებელს ჰკითხავს თამაშის სირთულის შესახებ (Level) რომელსაც დავარქვათ n და თუ მომხმარებელი არ შეიყვანს 1, 2 ან 3 – ს მაშინ ახლიდან ჰკითხავს იგივეს.
# რენდომად (შემთხვევითობის პრინციპით) დააგენერირებს 10 მაგალითს, ფორმატირებულს ასე X + Y = სადაც X და Y არის არანეგატიური მთელი რიცხვები n რაოდენობის ციფრებით (1 – ის შემთხვევაში ერთნიშნა, 2 – ის შემთხვევაში ორნიშნა, 3 – ის შემთხვევაში სამნიშნა). არ არის საჭირო სხვა ოპერაციების მხარდაჭერა. მხოლოდ შეკრების ოპერაციაც საკმარისია (+).
# პროგრამამ სათითაოდ უნდა გამოიტანოს ათივე მაგალითი და შეაყვანინოს მომხარებელს პასუხები. თუ პასუხი არასწორია ან საერთოდ რიცხვიც კი არ არის, მაშინ უნდა გამოიტანოს EEE შეცდომის მანიშნებლად. თითოეულ მაგალითზე პროგრამამ მომხმარებელს უნდა მისცეს 3 ცდა. სამივე შემთხვევაში არასწორი შედეგის მიღებისას უნდა გამოიტანოს სწორი პასუხი და გადავიდეს შემდეგ მაგალითზე.
# საბოლოოდ პროგრამამ უნდა გამოიტანოს მომხმარებლის ქულა იმის მიხედვით თუ რამდენი სწორი პასუხი ჰქონდა მომხმარებელს. მაქსიმუმ 10 ქულა. 
# შენი პროგრამის სტრუქტურა იყოს ასეთი: 
# 
import random


def main():
    level = get_level()
    score = 0

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct = x + y
        tries = 0

        while tries < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == correct:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
            tries += 1

        if tries == 3:
            print(f"{x} + {y} = {correct}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Enter Level (1, 2 or 3): ").strip())
            if n in [1, 2, 3]:
                return n
        except ValueError:
            pass  


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Unknown level")


if __name__ == "__main__":
    main()