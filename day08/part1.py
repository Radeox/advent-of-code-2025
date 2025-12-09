class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True


def main():
    boxes_coordinates = {}
    cables = 1000

    with open("input.txt") as f:
        lines = f.readlines()
        i = 0
        for line in lines:
            boxes_coordinates[i] = {
                "x": int(line.split(",")[0].strip()),
                "y": int(line.split(",")[1].strip()),
                "z": int(line.split(",")[2].strip()),
            }
            i += 1

    n = len(boxes_coordinates)

    # Pre-calculate all distances once
    distances = []
    for box1 in range(n):
        for box2 in range(box1 + 1, n):
            distance = (
                (boxes_coordinates[box1]["x"] - boxes_coordinates[box2]["x"]) ** 2
                + (boxes_coordinates[box1]["y"] - boxes_coordinates[box2]["y"]) ** 2
                + (boxes_coordinates[box1]["z"] - boxes_coordinates[box2]["z"]) ** 2
            ) ** 0.5
            distances.append((distance, box1, box2))

    # Sort all distances once
    distances.sort()

    # Use Union-Find to track circuits
    uf = UnionFind(n)
    connections_made = 0
    connections_skipped = 0

    # Process the 'cables' shortest pairs (whether they connect or are skipped)
    for i, (distance, box1, box2) in enumerate(distances):
        if i >= cables:
            break
        # Only connect if they're not already in the same circuit
        if uf.union(box1, box2):
            connections_made += 1
        else:
            connections_skipped += 1

    print(f"Processed {cables} shortest pairs")
    print(f"Connections made: {connections_made}, skipped: {connections_skipped}")
    print(f"Total boxes: {n}")

    # Count circuit sizes
    circuit_sizes = {}
    for box in range(n):
        root = uf.find(box)
        circuit_sizes[root] = circuit_sizes.get(root, 0) + 1

    # Get the three largest circuit sizes
    sizes = sorted(circuit_sizes.values(), reverse=True)

    print(f"Number of circuits: {len(sizes)}")
    if len(sizes) > 20:
        print(f"Circuit sizes (first 20): {sizes[:20]}")
    else:
        print(f"Circuit sizes: {sizes}")

    if len(sizes) < 3:
        print(f"ERROR: Only {len(sizes)} circuit(s) found, but need at least 3")
        print(f"This means all {n} boxes were connected into {len(sizes)} circuit(s)")
        print(
            f"With {cables} cables and {n} boxes, all boxes formed one connected component"
        )
        return None

    print(f"Three largest circuits: {sizes[0]}, {sizes[1]}, {sizes[2]}")

    # Calculate the product of the three largest
    result = sizes[0] * sizes[1] * sizes[2]
    print(f"Product of three largest circuits: {result}")

    return result


if __name__ == "__main__":
    print(main())
