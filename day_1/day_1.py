""" AoC Day 1: Calorie Counting """


def part_1() -> int:
    with open("input.txt", "r") as fp:
        return max(
            sum(int(food or 0) for food in elf.split("\n"))
            for elf in fp.read().split("\n\n")
        )


def part_2() -> int:
    with open("input.txt", "r") as fp:
        return sum(
            sorted(
                sum(int(food or 0) for food in elf.split("\n"))
                for elf in fp.read().split("\n\n")
            )[-3:]
        )


if __name__ == "__main__":
    print(part_1())
    print(part_2())
