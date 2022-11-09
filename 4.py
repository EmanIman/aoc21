def loadData() -> tuple[list[str], list[list[str]]]:
    data = []
    with open("i.txt", "r") as f:
        nums = f.readline().strip().split(",")
        for line in f:
            line = line.strip().split(" ")
            line = [l for l in line if l != ""]
            data.append(line)
    data = [l for l in data if l != []]
    return nums, data


class Board:
    def __init__(self, nums: list[list[str]]):
        self.nums = nums
        self.b = "-1" * len(nums)           # bingo string in this case "-1-1-1-1-1"
        self.done = False

    def num(self, num: str) -> bool:
        for i, r in enumerate(self.nums):
            for j, c in enumerate(r):
                if c == num:
                    self.nums[i][j] = "-1"

        if self.bingo():
            self.done = True
            return True
        return False

    # time complexity: O(lmao)
    def bingo(self) -> bool:
        # check all the rows
        for r in self.nums:
            row = ""
            for c in r:
                row += c
            if row == self.b:
                return True

        # check all the columns
        for i in range(len(self.nums)):
            col = ""
            for r in self.nums:
                col += r[i]
            if col == self.b:
                return True
        return False

    def sum(self) -> int:
        sum = 0
        for r in self.nums:
            for c in r:
                if c != "-1":
                    sum += int(c)
        return sum


def part1(data: tuple[list[str], list[list[str]]]) -> int:
    boards = buildBoards(data[1])
    for num in data[0]:
        for board in boards:
            if board.num(num):
                return board.sum() * int(num)


def buildBoards(data: list[list[str]]) -> list[Board]:
    n = 0
    boards = []
    cboard = []
    for line in data:
        if n < 5:
            cboard.append(line)
            n += 1
        else:
            boards.append(Board(cboard))
            cboard = [line]
            n = 1
    
    # add the last board
    boards.append(Board(cboard))
    return boards


def part2(data: tuple[list[str], list[list[str]]]) -> int:
    boards = buildBoards(data[1])
    num, board = finalNumBoard(data[0], boards)
    return num * board.sum()


def finalNumBoard(nums: list[str], boards: list[Board]) -> tuple[int, Board]:
    for num in nums:
        if len(boards) != 1:
            boards = addNum(num, boards)
        else:
            if boards[0].num(num):
                return int(num), boards[0]


def addNum(num: str, boards: list[Board]) -> list[Board]:
    for b in boards:
        b.num(num)
    rboards = filter(lambda b: not b.done, boards)
    return list(rboards)


def main() -> None:
    data = loadData()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()


