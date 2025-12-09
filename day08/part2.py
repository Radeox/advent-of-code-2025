class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.num_components = n

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
        self.num_components -= 1
        return True

    def is_single_component(self):
        return self.num_components == 1


def main():
    boxes_coordinates = {}

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
    print(f"Total boxes: {n}")

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
    last_box1 = None
    last_box2 = None

    # Keep connecting until all boxes are in one circuit
    for distance, box1, box2 in distances:
        # Only connect if they're not already in the same circuit
        if uf.union(box1, box2):
            connections_made += 1
            last_box1 = box1
            last_box2 = box2

            # Check if we've connected everything into one circuit
            if uf.is_single_component():
                print(f"All boxes connected after {connections_made} connections")
                print(
                    f"Last connection: box {box1} ({boxes_coordinates[box1]['x']},{boxes_coordinates[box1]['y']},{boxes_coordinates[box1]['z']}) <-> box {box2} ({boxes_coordinates[box2]['x']},{boxes_coordinates[box2]['y']},{boxes_coordinates[box2]['z']})"
                )
                print(f"Distance: {distance:.2f}")
                break

    if last_box1 is not None and last_box2 is not None:
        x1 = boxes_coordinates[last_box1]["x"]
        x2 = boxes_coordinates[last_box2]["x"]
        result = x1 * x2
        print(f"X coordinates: {x1} and {x2}")
        print(f"Product of X coordinates: {result}")
        return result
    else:
        print("ERROR: Could not connect all boxes into one circuit")
        return None


if __name__ == "__main__":
    print(main())
