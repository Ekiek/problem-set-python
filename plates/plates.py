def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) == 6:
        return True
    if s[:2].isalpha():
        return True
    if not s[2:].isalpha():
        return True
    return True
   
main()