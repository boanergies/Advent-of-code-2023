import string
from pathlib import Path

import typer

app = typer.Typer()


@app.command()
def part1():
    with (Path.cwd() / "day_1" / "day_1_part1_input.txt").open() as fin:
        print(
            sum(
                (
                    int(
                        line.lstrip(string.ascii_lowercase)[0]
                        + line.rstrip(string.ascii_lowercase + string.whitespace)[-1]
                    )
                    for line in fin
                )
            )
        )


@app.command()
def part2():
    number_words = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    with (Path.cwd() / "day_1" / "day_1_part2_input.txt").open() as fin:
        total = 0
        for line in fin:
            numbers = []
            for number_word, number in number_words.items():
                index = 0
                while index != -1:
                    index = line.find(number_word, index)
                    if index >= 0:
                        numbers.append((index, number))
                        index += len(number_word)
            numbers.extend(
                (line.find(character, index), character)
                for index, character in enumerate(line.strip(string.whitespace))
                if character.isdigit()
            )
            numbers.sort(key=lambda pair: pair[0])
            total += int(numbers[0][1] + numbers[-1][1])
        print(total)


if __name__ == "__main__":
    app()
