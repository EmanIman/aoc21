def loadData() -> list[list[str]]:
    data = []
    with open("i.txt", "r") as f:
        for line in f:
            data.append(line.split(" "))
    return data

def part1(data: list[list[str]]) -> int:
    h, d = 0, 0
    for l in data:
        if l[0] == "forward":
            h += int(l[1])
        elif l[0] == "down":
            d += int(l[1])
        else:
            d -= int(l[1])
    return h * d

def part2(data: list[list[str]]) -> int:
    h, d, a = 0, 0, 0
    for l in data:
        if l[0] == "forward":
            h += int(l[1])
            d += a * int(l[1])
        elif l[0] == "down":
            a += int(l[1])
        else:
            a -= int(l[1])
    return h * d

def main() -> None:
    data = loadData()
    print(part1(data))
    print(part2(data))

if __name__ == "__main__":
    main()