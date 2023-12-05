from pathlib import Path

import typer

app = typer.Typer()

EXPECTED_RESULTS = {"red": 12, "green": 13, "blue": 14}


def is_valid_game(sub_game: str) -> bool:
    for result in sub_game.split(","):
        number, color = result.strip().split(" ")
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


@app.command()
def part2():
    with (Path().cwd() / "day_2" / "day_2_input.txt").open() as fin:
        print(fin.read())


if __name__ == "__main__":
    app()
    app()
