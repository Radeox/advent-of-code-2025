def main():
    fresh_ids = {}
    total = 0

    with open("input.txt") as f:
        for line in f:
            line = line.strip()

            # If we reach the block end
            if line == "":
                # Merge ranges
                merged = []
                for start in sorted(fresh_ids.keys()):
                    end = fresh_ids[start]
                    if merged and start <= merged[-1][1]:
                        # Overlapping or adjacent - merge with last range
                        merged[-1] = (merged[-1][0], max(merged[-1][1], end))
                    else:
                        # Non-overlapping - add as new range
                        merged.append((start, end))

                for start, end in merged:
                    total += end - start + 1
                break

            # Compute ranges
            start, end = line.split("-")
            start = int(start)
            end = int(end)

            if start in fresh_ids:
                fresh_ids[start] = max(fresh_ids[start], end)
            else:
                fresh_ids[start] = end

    return total


if __name__ == "__main__":
    print(main())
