def loadData() -> list[int]:
    data = []
    with open("i.txt", "r") as f:
        for line in f:
            data.append(int(line))
    return data

def part1(data: list[int]) -> int:
    l, r = 0, 1
    count = 0
    while r < len(data):
        if data[r] > data[l]:
            count += 1
        l = r
        r += 1
    return count

def part2(data: list[int]) -> int:
    count = 0
    prev = 0
    l, r = 0, 1
    # this was bad but I though the other better soulutions was wrong before I realized I needed the count - 1 and not count
    # TODO redo correctly
    while r < len(data) - 1:
        sum = data[l] + data[r] + data[r + 1]
        if sum > prev:
            count += 1
        prev = sum
        l += 1
        r = l + 1
    return count - 1

def main() -> None:
    data = loadData()
    print(part1(data))
    print(part2(data))

if __name__ == "__main__":
    main()