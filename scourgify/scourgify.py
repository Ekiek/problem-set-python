import sys
import csv

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py before.csv after.csv")

    before = sys.argv[1]
    after = sys.argv[2]

    try:
        with open(before, "r", newline="", encoding="utf-8") as infile:
            reader = csv.DictReader(infile)

            with open(after, "w", newline="", encoding="utf-8") as outfile:
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()

                for row in reader:
                    last, first = row["name"].split(",")
                    last = last.strip()
                    first = first.strip()

                    writer.writerow({
                        "first": first,
                        "last": last,
                        "house": row["house"]
                    })

    except FileNotFoundError:
        sys.exit(f"Could not read {before}")

if __name__ == "__main__":
    main()