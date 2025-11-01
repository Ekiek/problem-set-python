import inflect

def main():
    names = []
    while True:
        try:
            name = input("Enter names: ")
            if name.strip():
                names.append(name.strip())
        except EOFError:
            break

    if not names:  
        return
   
    p = inflect.engine()
   
    adieu_str = f"Adieu, adieu, to {p.join(names)}"
    print(adieu_str)

if __name__ == "__main__":
    main()