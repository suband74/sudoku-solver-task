import json
from collections import Counter
from typing import List

import click

from decision_sudoku import solve


class Box:
    def __init__(self, table, row_idx, column_idx):
        self._rows = table[row_idx : row_idx + 3]
        self._column_idx = column_idx

    def __iter__(self):
        for row in self._rows:
            for column_idx in range(self._column_idx, self._column_idx + 3):
                yield row[column_idx]


def iterate_by_boxes(table: List[List[int]]):
    for row in (0, 3, 6):
        for column in (0, 3, 6):
            yield Box(table, row, column)


def search_same_numbers(sudoku_input: List[List[int]]):
    for row in sudoku_input:
        dict_same_key = Counter(row)
        if any(key != 0 and dict_same_key[key] != 1 for key in dict_same_key):
            raise ValueError(
                "The same numbers in the string (column, block). Unsolvable sudoku.",
            )


def validate_sudoku(sudoku_input: List[List[int]]):
    """
    Проверка входящего судоку на валидность.

    Args:
        sudoku_input (List[List[int]]): [Входящий, нерешенный судоку]

    Raises:
        TypeError: [Исключение, в случае невалидного судоку]
    """
    for row in sudoku_input:
        for cell in row:
            if not isinstance(cell, int) or 9 < cell or cell < 0:
                raise TypeError("sudoku can only enter numbers from 0 to 9 inclusive")

    search_same_numbers(sudoku_input)

    sudoku_input_transposed = list(zip(*sudoku_input))
    search_same_numbers(sudoku_input_transposed)

    search_same_numbers(iterate_by_boxes(sudoku_input))


@click.command()
@click.argument("file_start_sudoku", type=click.Path(exists=True))
@click.argument("file_result_sudoku", type=click.Path(exists=False))
def main(file_start_sudoku, file_result_sudoku):
    with open(file_start_sudoku) as f:
        data = json.load(f)
        sudoku = data["table"]
        validate_sudoku(sudoku)
        solve(sudoku)
        with open(file_result_sudoku, "w") as file:
            json.dump(data, file)


if __name__ == "__main__":
    main()
