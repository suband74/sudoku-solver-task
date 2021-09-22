from typing import List, Tuple


def _find_unassigned(board: List[List[int]]) -> Tuple[int, int]:
    """
    Ищем пустые ячейки в таблице.

    Args:
        board (List[List[int]]): [только числа 0-8]

    Returns:
        Tuple[int, int]: [координаты пустой ячейки, только числа -1 - +8]
    """
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                return row, column
    return -1, -1


def _box_slice(i: int) -> slice:
    """
    Делаем слайс размером 3*3.

    Args:
        i (int): [только числа 0-8]

    Returns:
        slice: [краевые значения координат в проверяемом блоке 3*3]
    """
    i -= i % 3
    return slice(i, i + 3)


def _suitable_number(board: List[List[int]], row: int, column: int, num: int) -> bool:
    """
    Проверяем существует ли такое число в строке, столбце, и в слайсе.

    Args:
        board (List[List[int]]): [только числа 0-8]
        row (int): [только числа  0-8]
        column (int): [только числа  0-8]
        num (int): [только числа 1-9]

    Returns:
        bool: [булево, в зависимости от того, подходит ли это число]
    """
    return (
        all(cell != num for cell in board[row])
        and all(row[column] != num for row in board)
        and all(
            cell != num
            for row in board[_box_slice(row)]
            for cell in row[_box_slice(column)]
        )
    )


def solve(board: List[List[int]]) -> bool:
    """
    Логический алгоритм решения судоку.

    Args:
        board (List[List[int]]): [в ячейки судоку следует вводить только
        цифры 0-9, при этом 0 символизирует пустое значение]

    Returns:
        bool: [Булево. True возвращается когда ячейка заполняется значением 1-9.
        Соответственно, если подстановка значения невозможна (по правилам
        судоку), возвращается False, и значение в ячейке меняется на 0.]
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
