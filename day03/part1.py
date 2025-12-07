def main():
    banks = []
    total = 0

    # Read input from file
    with open("input.txt", "r") as file:
        for line in file:
            banks.append(line.strip())

    # Compute solution
    for bank in banks:
        max = 0

        for i, char in enumerate(bank):
            val = char

            for second in bank[i + 1 :]:
                sval = second

                if max < int(f"{val}{sval}"):
                    max = int(f"{val}{sval}")

        total += max

    return total


if __name__ == "__main__":
    print(main())
