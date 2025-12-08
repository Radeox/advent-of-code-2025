def main():
    memory = []
    operators = []
    total = 0

    with open("input.txt") as f:
        for line in f:
            row = []
            line = line.strip()

            # Remove multiple spaces
            line = " ".join(line.split())

            if line.startswith("*") or line.startswith("+"):
                operators = line.split(" ")
                break

            for num in line.split(" "):
                row.append(int(num))
            memory.append(row)

    for j, operator in enumerate(operators):
        if operator == "*":
            tot = 1
        else:
            tot = 0

        for i in range(len(memory)):
            if operator == "*":
                tot *= memory[i][j]
            else:
                tot += memory[i][j]

        total += tot

    return total


if __name__ == "__main__":
    print(main())
