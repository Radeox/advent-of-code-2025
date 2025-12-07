def main():
    fresh_ids = {}
    total = 0
    with open("input.txt") as f:
        processing_ids = True

        for line in f:
            line = line.strip()
            if line == "":
                processing_ids = False
                continue

            # Compute ranges
            if processing_ids:
                start, end = line.split("-")
                start = int(start)
                end = int(end)

                if start in fresh_ids:
                    fresh_ids[start] = max(fresh_ids[start], end)
                else:
                    fresh_ids[start] = end
            else:
                # Process IDs
                id_to_check = int(line)

                for start in list(fresh_ids.keys()):
                    end = fresh_ids[start]
                    if start <= id_to_check <= end:
                        total += 1
                        break

    return total


if __name__ == "__main__":
    print(main())
