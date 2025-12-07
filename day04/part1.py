def main():
    matrix = []
    total = 0

    with open("input.txt") as f:
        for line in f:
            row = [x for x in line.strip()]
            matrix.append(row)

    # Compute which rolls are accessible
    for y, row in enumerate(matrix):
        for x, value in enumerate(row):
            if value == "@":
                counter = 0

                # Check left
                if x > 0 and matrix[y][x - 1] == "@":
                    counter += 1
                # Check right
                if x < len(row) - 1 and matrix[y][x + 1] == "@":
                    counter += 1
                # Check up
                if y > 0 and matrix[y - 1][x] == "@":
                    counter += 1
                # Check down
                if y < len(matrix) - 1 and matrix[y + 1][x] == "@":
                    counter += 1
                # Check top-left
                if x > 0 and y > 0 and matrix[y - 1][x - 1] == "@":
                    counter += 1
                # Check top-right
                if x < len(row) - 1 and y > 0 and matrix[y - 1][x + 1] == "@":
                    counter += 1
                # Check bottom-left
                if x > 0 and y < len(matrix) - 1 and matrix[y + 1][x - 1] == "@":
                    counter += 1
                # Check bottom-right
                if (
                    x < len(row) - 1
                    and y < len(matrix) - 1
                    and matrix[y + 1][x + 1] == "@"
                ):
                    counter += 1

                if counter < 4:
                    print("X", end="")
                    total += 1
                else:
                    print("@", end="")
            else:
                print(value, end="")
        print()

    return total


if __name__ == "__main__":
    print(main())
