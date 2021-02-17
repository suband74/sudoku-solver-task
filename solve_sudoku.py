import json
from collections import Counter
from typing import List

import click

from decision_sudoku import solve


def search_same_numbers(s):
    for i in s:
        x = Counter(i)
        for key in x:
            if key != 0 and x[key] != 1:
                raise ValueError('The same numbers in the string (column,block). Unsolvable sudoku')


def validate_sudoku(s: List[List[int]]):
    """
    проверка входящего судоку на валидность
    :param s: List[List[int]]
    :return:
    """
    for u in s:
        for r in u:
            if not isinstance(r, int) or 9 < r or r < 0:
                raise TypeError('sudoku can only enter numbers from 0 to 9 inclusive')

    search_same_numbers(s)

    s = list(zip(*s))
    search_same_numbers(s)

    d = [[], [], [], [], [], [], [], [], []]
    n = 0
    for m in range(0, 7, 3):
        for k in range(0, 7, 3):
            for i in range(k, k + 3):
                for j in range(m, m + 3):
                    d[n].append(s[i][j])
            n += 1
    search_same_numbers(d)


# @click.command()
# @click.argument('file_start_sudoku')
# def main(file_start_sudoku):
#     with open(file_start_sudoku) as f:
#         data = json.load(f)
#         sudoku = data['table']
#         validate_sudoku(sudoku)
#         solve(sudoku)
#         with open('result.json', 'w') as file:
#             json.dump(data, file)
@click.command()
@click.argument('file_start_sudoku', type=click.Path(exists=True))
@click.argument('file_result_sudoku', type=click.Path(exists=False))
def main(file_start_sudoku, file_result_sudoku):
    with open(file_start_sudoku) as f:
        data = json.load(f)
        sudoku = data['table']
        validate_sudoku(sudoku)
        solve(sudoku)
        with open(file_result_sudoku, 'w') as file:
            json.dump(data, file)

if __name__ == '__main__':
    main()
