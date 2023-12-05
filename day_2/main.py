from pathlib import Path

import typer

app = typer.Typer()

EXPECTED_RESULTS = {"red": 12, "green": 13, "blue": 14}


def is_valid_game(sub_game: str) -> bool:
    for result in sub_game.split(","):
        number, color = result.strip().split()
        if EXPECTED_RESULTS[color] < int(number):
            return False
    return True


@app.command()
def part1():
    with (Path().cwd() / "day_2" / "day_2_input.txt").open() as fin:
        total = sum(
            game_id + 1
            for game_id, game in enumerate(fin)
            if all(
                is_valid_game(sub_game) for sub_game in game.split(":")[1].split(";")
            )
        )
        print(total)


def get_minimum_cubes(game: str) -> int:
    max_red = 0
    max_blue = 0
    max_green = 0
    for sub_game in game.split(";"):
        for result in sub_game.split(","):
            number, color = result.strip().split()
            match (color):
                case "red":
                    max_red = max(max_red, int(number))
                case "blue":
                    max_blue = max(max_blue, int(number))
                case "green":
                    max_green = max(max_green, int(number))
    return max_red * max_green * max_blue


@app.command()
def part2():
    with (Path().cwd() / "day_2" / "day_2_input.txt").open() as fin:
        print(sum(get_minimum_cubes(game.split(":")[1]) for game in fin))


if __name__ == "__main__":
    app()
