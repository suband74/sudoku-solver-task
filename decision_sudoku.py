from typing import List, Tuple


def _find_unassigned(board: List[List[int]]) -> Tuple[int, int]:
    """
    Ищем пустые ячейки в таблице
    :param board: только числа 0-8
    :return: координаты пустой ячейки, только числа -1 - +8
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return -1, -1


def _box_slice(i: int) -> slice:
    """
    делаем слайс размером 3*3
    :param i: только числа 0-8
    :return: краевые значения координат в проверяемом блоке 3*3
    """
    i -= i % 3
    return slice(i, i + 3)


def _suitable_number(board: List[List[int]], i: int, j: int, num: int) -> bool:
    """
    проверяем существует ли такое число в строке, столбце, и в слайсе
    :param board: только числа 0-8
    :param i: только числа  0-8
    :param j: только числа 0-8
    :param num: только числа 1-9
    :return: булево, в зависимости от того, подходит ли это число.
    """
    return (
            all(cell != num for cell in board[i]) and
            all(row[j] != num for row in board) and
            all(
                cell != num
                for row in board[_box_slice(i)]
                for cell in row[_box_slice(j)]
            )
    )


def solve(board: List[List[int]]) -> bool:
    """
    Логический алгоритм решения судоку
    :param board: в ячейки судоку следует вводить только цифры 0-9, при этом 0 символизирует пустое значение
    :return: Булево. True возвращается когда ячейка заполняется значением 1-9. Соответственно, если подстановка
    значения невозможна (по правилам судоку), возвращается False, и значение в ячейке меняется на 0.
    """

    i, j = _find_unassigned(board)
    if (i, j) == (-1, -1):
        # если не нашли пустую ячейку
        return True

    for num in range(1, 10):
        if _suitable_number(board, i, j, num):
            # если цифры нет ни в стороке ни в солобце ни в блоке
            board[i][j] = num
            if solve(board):
                # рекурсия
                return True

    board[i][j] = 0
    return False
