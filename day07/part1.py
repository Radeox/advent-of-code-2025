def main():
    total = 0
    grid = []
    beams = []
    spawns = []
    start_position = tuple()
    hit_splitters = set()

    with open("input.txt") as f:
        for line in f:
            row = []
            for char in line.strip():
                row.append(char)
            grid.append(row)

    # Search for starting position
    for char in grid[0]:
        if char == "S":
            start_position = (0, grid[0].index(char))
            beams.append(start_position)

    # Process beams
    # Each beam moves down until it hits a splitter ^ or the bottom of the grid
    while beams:
        beam = beams.pop(0)
        x, y = beam

        # Avoid processing the same spawn point multiple times
        if beam in spawns:
            continue
        else:
            spawns.append((x, y))

        while x < len(grid):
            if grid[x][y] == "^":
                # Only count this splitter if it hasn't been hit before
                if (x, y) not in hit_splitters:
                    hit_splitters.add((x, y))
                    total += 1

                # Split the beam into two new beams
                if y > 0:
                    beams.append((x, y - 1))
                if y < len(grid[0]) - 1:
                    beams.append((x, y + 1))
                break

            # Move the beam down
            x += 1

    return total


if __name__ == "__main__":
    print(main())
