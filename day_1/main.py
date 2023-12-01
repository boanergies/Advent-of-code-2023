from pathlib import Path

import typer

app = typer.Typer()


@app.command()
def part1():
    with (Path.cwd() / "day_1" / "day_1_part1_input.txt").open() as fin:
        print(
            sum(
                (
                    int(numbers[0] + numbers[-1])
                    for numbers in (
                        list(filter(lambda character: character.isdigit(), line))
                        for line in fin
                    )
                )
            )
        )


@app.command()
def part2():
    with (Path.cwd() / "day_1" / "day_1_part2_input.txt").open() as fin:
        print(fin.read())


if __name__ == "__main__":
    app()
