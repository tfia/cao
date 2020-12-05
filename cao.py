import sys
import getch

errs = ["Program exit.", "You say too many 啊!", "Too many 怎么样呢 is killing the sheep!", "Too many 欸怎么样呢 is killing the sheep!", "我们说 and 是吧 do not match!"]


def execute(filename):
    f = open(filename, "r")
    return errs[run(f.read())]
    f.close()


def run(code):
    code = cleanup(list(code))
    posmap = buildposmap(code)
    if posmap == -1:
        return 4
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
            if cells[cellspointer] < 0:
                return 3

        if command == "有一个成语叫":
            sys.stdout.write(chr(cells[cellspointer]))

        if command == "嗳":
            cells[cellspointer] = ord(getch.getch())

        if command == "我们说" and cells[cellspointer] == 0:
            codepointer = posmap[codepointer]

        if command == "是吧" and cells[cellspointer] != 0:
            codepointer = posmap[codepointer]

        if command == "啊嗯":
            return 0

        codepointer += 1

    return 0


def buildposmap(code):
    tempstack, posmap = [], []
    for pos, command in enumerate(code):
        if command == "我们说":
            tempstack.append(pos)
        if command == "是吧":
            last = tempstack.pop()
            posmap[last] = pos
            posmap[pos] = last
    if len(tempstack) == 0:
        return posmap
    else:
        return -1