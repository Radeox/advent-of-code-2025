def main():
    banks = []
    total = 0

    # Read input from file
    with open("input.txt", "r") as file:
        for line in file:
            banks.append([int(x) for x in line.strip()])

    for bank in banks:
        # Ignore one element and compute max
        while len(bank) > 12:
            new_bank = []
            max = 0
            index = 0

            while index < len(bank):
                tmp = []
                # Create new bank without one element
                for i in range(len(bank)):
                    if i == index:
                        continue

                    tmp.append(bank[i])

                n = int("".join([str(x) for x in tmp]))

                if n > max:
                    max = n
                    new_bank = tmp

                index += 1

            bank = new_bank

        total += int("".join([str(x) for x in bank]))

    return total


if __name__ == "__main__":
    print(main())
