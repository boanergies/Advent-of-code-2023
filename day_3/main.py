from pathlib import Path

import typer

app = typer.Typer()


@app.command()
def part1():
    with (
        Path().cwd()
        / "day_3"
        / "day_3_part1_input.txt"
    ).open() as fin:
        print(fin.read())


@app.command()
def part2():
    with (
        Path().cwd()
        / "day_3"
        / "day_3_part2_input.txt"
    ).open() as fin:
        print(fin.read())


if __name__ == "__main__":
    app()
    app()
