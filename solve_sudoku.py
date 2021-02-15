import json
from collections import Counter
from typing import List

import click

from decision_sudoku import solve


def validation_sudoku(s: List[List[int]]):
    """
    проверка входящего судоку на валидность
    :param s: List[List[int]]
    :return:
    """
    for u in range(len(s)):
        for r in range(len(s[u])):
            if not isinstance(s[u][r], int) or 9 < s[u][r] or s[u][r] < 0:
                raise TypeError('sudoku can only enter numbers from 0 to 9 inclusive')

    for i in range(len(s)):
        x = Counter(s[i])
        for key in x:
            if key != 0 and x[key] != 1:
                raise ValueError('The same numbers in the string. Unsolvable sudoku')

    s = list(zip(s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8]))
    for n in range(len(s)):
        x = Counter(s[n])
        for key in x:
            if key != 0 and x[key] != 1:
                raise ValueError('The same numbers in the column. Unsolvable sudoku')

    d = [[], [], [], [], [], [], [], [], []]
    n = 0
    for m in range(0, 7, 3):
        for k in range(0, 7, 3):
            for i in range(k, k + 3):
                for j in range(m, m + 3):
                    d[n].append(s[i][j])
            n += 1
    for g in range(len(d)):
        x = Counter(d[g])
        for key in x:
            if key != 0 and x[key] != 1:
                raise ValueError('The same numbers in the block. Unsolvable sudoku')


@click.command()
@click.argument('file_start_sudoku')
def main(file_start_sudoku):
    with open(file_start_sudoku) as f:
        data = json.load(f)
        sudoku = data['table']
        validation_sudoku(sudoku)
        solve(sudoku)
        with open('result.json', 'w') as file:
            json.dump(data, file)


if __name__ == '__main__':
    main()
