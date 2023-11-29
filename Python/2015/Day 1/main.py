def get_input(file: str) -> str:
    with open(file) as f:
        return f.read()


def part1():
    return get_input("./input.txt").count("(") - get_input("./input.txt").count(")")


def part2():
    floor = 0
    seenChars = []
    for c in get_input("./input.txt"):
        floor = floor + 1 if c == "(" else floor - 1
        seenChars.append(c)
        if floor == -1:
            return len(seenChars)


def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()
