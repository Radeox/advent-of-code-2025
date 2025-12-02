import re


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

            # Check if string is composed of repeated sequences
            sub = id[0]
            for i in range(1, len(id)):
                if re.fullmatch(f"({sub})+", id):
                    counter += int(id)
                    break

                sub += id[i]

    return counter


if __name__ == "__main__":
    print(main())
