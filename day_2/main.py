from pathlib import Path

import typer

app = typer.Typer()


@app.command()
def part1():
    with Path().cwd() / "day_2" / "day_2_part1_input.txt" as fin:
        print(fin.read())


@app.command()
def part2():
    with Path().cwd() / "day_2" / "day_2_part2_input.txt" as fin:
        print(fin.read())


if __name__ == "__main__":
    app()
    app()
