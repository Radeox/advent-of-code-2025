def main():
    total = 0

    with open("input.txt") as f:
        # Rotate file counter-clockwise by 90 degrees
        lines = f.read().splitlines()
        grid = [list(line) for line in lines]
        n = len(grid)
        m = max(len(line) for line in grid) if n > 0 else 0
        rotated_grid = [[""] * n for _ in range(m)]

        for i in range(n):
            for j in range(m):
                if j < len(grid[i]):
                    rotated_grid[m - j - 1][i] = grid[i][j]
                else:
                    rotated_grid[m - j - 1][i] = " "

    memory = []
    for row in rotated_grid:
        # Process as string
        row = "".join(row).strip()

        if "+" in row:
            num = int(row.split("+")[0])
            memory.append(num)

            # Make operation
            tmp = 0
            for number in memory:
                tmp += number
            total += tmp
            memory = []
        elif "*" in row:
            num = int(row.split("*")[0])
            memory.append(num)

            # Make operation
            tmp = 1
            for number in memory:
                tmp *= number
            total += tmp
            memory = []
        elif row == "":
            continue
        else:
            num = int(row)
            memory.append(num)

    return total


if __name__ == "__main__":
    print(main())
