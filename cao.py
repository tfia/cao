import sys

errs = ["Program exit.", "You say too many 啊!", "Too many 怎么样呢 is killing the sheep!"]


def execute(filename):
    f = open(filename, "r")
    return errs[run(f.read())]


def run(code):
    code = cleanup(list(code))
    posmap = buildposmap(code)
    cells, codepointer, cellspointer = [0], 0, 0
    while codepointer <= len(code):
        command = code[codepointer]
        if command == "欸":
            cellspointer += 1
            if cellspointer == len(code):
                cells.append(0)

        if command == "啊":
            cellspointer -= 1
            if cellspointer < 0:
                return 1

        if command == "怎么样呢":
            cells[cellspointer] += 1
            if cells[cellspointer] > 256:
                return 2

        if command == "欸怎么样呢":
            cells[cellspointer] -= 1
