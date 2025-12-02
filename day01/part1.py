def main():
    sequence = []
    zero_counter = 0
    dial_pos = 50

    # Read input from file
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            direction = line[0]
            value = int(line[1:])

            sequence.append((direction, int(value)))

    # Process the sequence
    for direction, value in sequence:
        for _ in range(value):
            if direction == "L":
                dial_pos -= 1
            elif direction == "R":
                dial_pos += 1

            if dial_pos == 100:
                dial_pos = 0

            if dial_pos == -1:
                dial_pos = 99

        if dial_pos == 0:
            zero_counter += 1

        print(f"Dial Position: {dial_pos}, Zero Count: {zero_counter}")

    return zero_counter


if __name__ == "__main__":
    print(main())
