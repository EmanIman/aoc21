def loadData() -> list[str]:
    data = []
    with open("i.txt", "r") as f:
        for line in f:
            data.append(line.strip())
    return data


def part1(data: list[str]) -> int:
    g, e = "", ""
    c = commonBits(data)
    for b in c:
        g += str(b)
        e += op(b)
    g, e = binDec(g, e)
    return g * e


def binDec(g: str, e: str) -> tuple[int, int]:
    return int(g, 2), int(e, 2)


def op(b: int) -> str:
    return "0" if b == 1 else "1"


def commonBits(data: list[str]) -> list[int]:
    d: dict[str, tuple[int, int]] = {}
    for l in data:
        for i, b in enumerate(l):
            b = int(b)
            if i in d:
                t = d[i]
                t[b] = t[b] + 1
                d[i] = t
            else:
                t = [0, 0]
                t[b] = 1
                d[i] = t
    cb = []
    for k, v in d.items():
        cb.append(v.index(max(v)))
    return cb


def part2(data: list[str]) -> int:
    oxygen = parseData(data, "1", "max")
    co2 = parseData(data, "0", "min")
    return oxygen * co2


def parseData(data: list[str], equal: str, eval: str) -> int:
    for i in range(len(data[0])):
        b = mostComnBit(data, i, equal, eval)
        data = [l for l in data if l[i] == b]
        if len(data) == 1:
            return(int(data[0], 2))


def mostComnBit(data: list[str], i: int, equal: str, eval: str) -> str:
    t = [0, 0]
    for l in data:
        t[int(l[i])] += 1
    if t[0] == t[1]:
        return equal
    if eval == "max":
        return str(t.index(max(t)))
    return str(t.index(min(t)))


def main() -> None:
    data = loadData()
    # data = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()