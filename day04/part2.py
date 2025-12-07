def main():
    matrix = []
    rv = 0
    looping = True

    with open("input.txt") as f:
        for line in f:
            row = [x for x in line.strip()]
            matrix.append(row)

    # Compute which rolls are accessible
    while looping:
        total = 0
        new_matrix = []

        for y, row in enumerate(matrix):
            new_row = []

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
                        total += 1
                        rv += 1
                        new_row.append(".")
                    else:
                        new_row.append("@")
                else:
                    new_row.append(value)

            new_matrix.append(new_row)

        if total == 0:
            looping = False

        matrix = new_matrix

    return rv


if __name__ == "__main__":
    print(main())
