import json
from decision_sudoku import solve
import click
from collections import Counter
import numpy as np


def validation_sudoku(s: list):
    for u in range(len(s)):
        for r in range(len(s[u])):
            if not isinstance(s[u][r], int):
                raise TypeError('В судоку можно вводить только цифры')
    for a in range(len(s)):
        for b in range(len(s[a])):
            if 9 < s[a][b] or s[a][b] < 0:
                raise ValueError('В судоку можно вводить только цифры от 0 до 9 включительно')
    for i in range(len(s)):
        x = Counter(s[i])
        for key in x:
            if key != 0 and x[key] != 1:
                raise ValueError('В строке одинаковые цифры. Судоку нерешаемая')
    y = np.array(s)
    for n in range(len(s)):
        x = y[:, n]
        x = Counter(x)
        for key in x:
            if key != 0 and x[key] != 1:
                raise ValueError('В столбце одинаковые цифры. Судоку нерешаемая')
    for k in range(0, 7, 3):
        for t in range(0, 7, 3):
            x = y[k:k+3, t:t+3]
            x = x.ravel()
            x = Counter(x)
            for key in x:
                if key != 0 and x[key] != 1:
                    raise ValueError('В блоке одинаковые цифры. Судоку нерешаемая')


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
