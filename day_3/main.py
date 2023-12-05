import string
from itertools import product
from pathlib import Path

import typer

app = typer.Typer()


def is_number_part(number_cooridnate: tuple, grid: list[str]):
    cooridnate = number_cooridnate[1]
    number = number_cooridnate[0]
    for y, x in product(
        range(cooridnate[1] - 1, cooridnate[1] + len(number) + 1),
        range(cooridnate[0] - 1, cooridnate[0] + 2),
    ):
        if (
            y > 0
            and y < len(grid[0])
            and x > 0
            and x < len(grid)
            and grid[x][y] != "."
            and grid[x][y] in string.punctuation
        ):
            return True


@app.command()
def part1():
    with (Path().cwd() / "day_3" / "day_3_part1_input.txt").open() as fin:
        grid = [line.strip() for line in fin]
        total = 0
        for x, line in enumerate(grid):
            number = ""
            coordinate = None
            for y, character in enumerate(line):
                if not number and character.isdigit():
                    number = character
                    coordinate = (x, y)
                elif number and character.isdigit():
                    number += character
                elif number and not character.isdigit():
                    if is_number_part((number, coordinate), grid):
                        total += int(number)
                    number = ""
        print(total)


@app.command()
def part2():
    with (Path().cwd() / "day_3" / "day_3_part2_input.txt").open() as fin:
        print(fin.read())


if __name__ == "__main__":
    app()
    app()
