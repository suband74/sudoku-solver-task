from typing import List, Tuple


def find_unassigned(board: List[List[int]]) -> Tuple[int, int]:
    """
    Search empty cell in board
    :param board: only number 0-8
    :return: coordinates empty cell, only number -1 - +8
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return -1, -1


def box_slice(i: int) -> slice:
    """
    do slice for make area 3*3
    :param i: only number 0-8
    :return: краевые значения координат в проверяемом блоке 3*3
    """
    i -= i % 3
    return slice(i, i + 3)


def suitable_number(board: List[List[int]], i: int, j: int, num: int) -> bool:
    """
    inspection exist such number in  row, columns or area 3*3
    :param board: only number 0-8
    :param i: only number  0-8
    :param j: only number 0-8
    :param num: only number 1-9
    :return: True or Folse, depending on the does it fit number.
    """
    return (
            all(cell != num for cell in board[i]) and
            all(row[j] != num for row in board) and
            all(
                cell != num
                for row in board[box_slice(i)]
                for cell in row[box_slice(j)]
            )
    )


def solve(board: List[List[int]]) -> bool:
    """
    Логический алгоритм решения судоку
    :param board: в ячейки судоку следует вводить только цифры 0-9, при этом 0 символизирует пустое значение
    :return: Булево. True возвращается когда ячейка заполняется значением 1-9. Соответственно, если подстановка
    значения невозможна (по правилам судоку), возвращается Folse, и значение в ячейке меняется на 0.
    """

    i, j = find_unassigned(board)
    if (i, j) == (-1, -1):
        # если не нашли пустую ячейку
        return True

    for num in range(1, 10):
        if suitable_number(board, i, j, num):
            # если цифры нет ни в стороке ни в солобце ни в блоке
            board[i][j] = num
            if solve(board):
                # рекурсия
                return True

    board[i][j] = 0
    return False
