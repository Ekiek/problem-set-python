# change = int(input("Insert Coin: "))

# while change < 50:
#     new_change = int(input(f"Insert Coin {50 - change}: "))
#     change += new_change
#     if change >= 50:
#         print(f"Amount Due: {50 - change}: ")
#     elif change == 0:
#         break

total = 0

while total < 50:
    coin = int(input("Insert Coin: "))
    if coin in [25, 10, 5]:
        total += coin
    if total < 50:
        print(f"Amount Due: {50 - total}")

print(f"Change Owed: {total - 50}")
