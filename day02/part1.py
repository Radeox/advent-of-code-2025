def main():
    counter = 0

    # Read input from file
    with open("input.txt", "r") as file:
        line = file.readline().strip()
        products = line.split(",")

    for product in products:
        id_min, id_max = product.split("-")

        for id in range(int(id_min), int(id_max) + 1):
            id = str(id)

            # Check if half string is equal to the other half
            mid = len(id) // 2
            first_half = id[:mid]
            second_half = id[mid:]
            if first_half != second_half:
                continue

            print(f"Found matching id: {id}")
            counter += int(id)

    return counter


if __name__ == "__main__":
    print(main())
