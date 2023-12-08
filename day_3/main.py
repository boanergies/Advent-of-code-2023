from itertools import product
from pathlib import Path

import typer

app = typer.Typer()


def is_number_part(number: str, coordinate: tuple, grid: list[str]) -> bool:
    return any(
        x >= 0
        and x < len(grid)
        and y >= 0
        and y < len(grid[0])
        and grid[x][y] != "."
        and not grid[x][y].isdigit()
        for x, y in product(
            range(coordinate[0] - 1, coordinate[0] + 2),
            range(coordinate[1] - 1, coordinate[1] + len(number) + 1),
        )
    )


def is_star_part(number: str, coordinate: tuple, grid: list[str]) -> tuple:
    for x, y in product(
        range(coordinate[0] - 1, coordinate[0] + 2),
        range(coordinate[1] - 1, coordinate[1] + len(number) + 1),
    ):
        if (
            x >= 0
            and x < len(grid)
            and y >= 0
            and y < len(grid[0])
            and grid[x][y] == "*"
        ):
            return (x, y)
    return ()


@app.command()
def part1():
    with (Path().cwd() / "day_3" / "day_3_part1_input.txt").open() as fin:
        grid = [line.strip() for line in fin]
        number = ""
        total = 0
        for x, line in enumerate(grid):
            for y, character in enumerate(line):
                if not number and character.isdigit():
                    number = character
                    coordinate = (x, y)
                elif number and character.isdigit():
                    number += character
                    # corner case for when the number is at the end of the line
                    if y + 1 == len(line) and is_number_part(number, coordinate, grid):
                        total += int(number)
                        number = ""
                elif number and not character.isdigit():
                    if is_number_part(number, coordinate, grid):
                        total += int(number)
                    number = ""
        print(total)


@app.command()
def part2():
    with (Path().cwd() / "day_3" / "day_3_part1_input.txt").open() as fin:
        grid = [line.strip() for line in fin]
        part_numbers = {}
        number = ""
        for x, line in enumerate(grid):
            for y, character in enumerate(line):
                if not number and character.isdigit():
                    number = character
                    coordinate = (x, y)
                elif number and character.isdigit():
                    number += character
                    # corner case for when the number is at the end of the line
                    if y + 1 == len(line) and (
                        star_coordinate := is_star_part(number, coordinate, grid)
                    ):
                        if star_coordinate not in part_numbers:
                            part_numbers[star_coordinate] = [number]
                        else:
                            part_numbers[star_coordinate].append(number)
                        number = ""
                elif number and not character.isdigit():
                    if star_coordinate := is_star_part(number, coordinate, grid):
                        if star_coordinate not in part_numbers:
                            part_numbers[star_coordinate] = [number]
                        else:
                            part_numbers[star_coordinate].append(number)
                    number = ""
        print(
            sum(
                int(value[0]) * int(value[1])
                for value in part_numbers.values()
                if len(value) == 2
            )
        )


if __name__ == "__main__":
    app()
