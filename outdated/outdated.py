def main():
    months = {
        "January" : "01",
        "February" : "02",
        "March" : "03",
        "April" : "04",
        "May" : "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
    }
     
    while True:
        date = input("Date: ").strip()
        try:
            if "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)

            elif "," in date:
                month_str, day_year = date.split(" ", 1)
                day, year = day_year.replace(",", "").split()
                month_str = month_str.title().strip()
                month = months[month_str]
                day = int(day)
                year = int(year)
            else:
                raise ValueError
            
            if not (1 <= month <= 12 and 1 <= day <= 31):
                raise ValueError
            print(f"{year:04}-{month:02}-{day:02}")
            break
        
        except (ValueError, KeyError):
            continue

main()