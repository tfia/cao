import sys
import getch

errs = ["Program exit.", "You say too many 啊!", "我们说 and 是吧 do not match!"]


def execute(filename):
    f = open(filename, "r", encoding='UTF-8')
    r = errs[run(f.read())]
    f.close()
    return r


def run(code):
    code = cleanup(code)
    posmap = buildposmap(code)
    if posmap == -1:
        return 2
    cells, codepointer, cellspointer = [0], 0, 0

    while codepointer < len(code):
        command = code[codepointer]
        if command == "欸":
            cellspointer += 1
            if cellspointer == len(cells):
                cells.append(0)

        if command == "啊":
            if cellspointer < 0:
                return 1
            cellspointer -= 1

        if command == "怎么样呢":
            cells[cellspointer] = cells[cellspointer] + 1 if cells[cellspointer] < 255 else 0

        if command == "欸怎么样呢":
            cells[cellspointer] = cells[cellspointer] - 1 if cells[cellspointer] > 0 else 255

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
    tempstack, posmap = [], {}
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


def cleanup(code):
    for i in range(0,len(code)):
        if code[i] == "*":
            while True:
                code[i] = " "
                i += 1
                if code[i] == "/":
                    code[i] = " "
                    break
    code = code.replace('\n', '')
    code = code.replace(' ', '')
    code = code.replace('   ', '')
    code = code.split(",")
    return code

def main():
    if len(sys.argv) == 2:
        execute(sys.argv[1])
    else:
        print("Cao Script on Python, Dec 6 2020")
        print("Usage: python", sys.argv[0], "filename")


if __name__ == '__main__':
    main()
