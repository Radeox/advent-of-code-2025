def main():
    grid = []
    start_position = None

    with open("input.txt") as f:
        for line in f:
            row = []
            for char in line.strip():
                row.append(char)
            grid.append(row)

    # Search for starting position
    for i, char in enumerate(grid[0]):
        if char == "S":
            start_position = (0, i)
            break

    memo = {}

    def count_paths(x, y):
        # Check memo first
        if (x, y) in memo:
            return memo[(x, y)]

        # Base case: reached S
        if (x, y) == start_position:
            memo[(x, y)] = 1
            return 1

        # Can't go further up
        if x == 0:
            memo[(x, y)] = 0
            return 0

        next_x = x - 1
        total = 0

        # Try to move straight up (if no splitter directly above)
        if grid[next_x][y] != "^":
            total += count_paths(next_x, y)

        # Try to merge with splitters to the left or right
        for dy in [-1, 1]:
            splitter_y = y + dy
            if 0 <= splitter_y < len(grid[0]) and next_x >= 0:
                if grid[next_x][splitter_y] == "^":
                    # Found a splitter adjacent in the next row
                    # We can merge with it and spawn above
                    spawn_x = next_x - 1
                    if spawn_x >= 0:
                        total += count_paths(spawn_x, splitter_y)

        memo[(x, y)] = total
        return total

    # Count paths from all bottom positions
    bottom_row = len(grid) - 1
    total_paths = 0
    for col in range(len(grid[0])):
        total_paths += count_paths(bottom_row, col)

    return total_paths


if __name__ == "__main__":
    print(main())
