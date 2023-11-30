def get_input(file: str) -> list[str]:
    with open(file) as f:
        return f.read().split("\n")


def part1():
    wraping = 0
    for d in get_input("./input.txt"):
        x = d.split("x")
        l, w, h = int(x[0]), int(x[1]), int(x[2])
        s = [l * w, w * h, h * l]
        wraping += 2 * sum(s) + min(s)
    return wraping


def part2():
    ribbon = 0
    for d in get_input("./input.txt"):
        x = d.split("x")
        l, w, h = int(x[0]), int(x[1]), int(x[2])
        ribbon += (2 * min(l + w, w + h, l + h)) + (l * w * h)
    return ribbon


def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()
