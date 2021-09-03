import pytest

from decision_sudoku import _box_slice, _find_unassigned, solve
from solve_sudoku import validate_sudoku


def test_validate_sudoku_str():
    """
    Проверка входящего судоку на одинаковые цифры в строке
    :return: True or False
    """
    sudoku_wrong = [
        [1, 2, 3, 4, 4, 6, 7, 8, 9],
        [4, 0, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 0, 6],
        [2, 3, 4, 0, 6, 7, 8, 9, 1],
        [0, 6, 7, 8, 9, 1, 2, 3, 4],
        [8, 9, 1, 2, 3, 4, 0, 6, 7],
        [3, 4, 0, 6, 7, 8, 9, 1, 2],
        [6, 7, 8, 9, 1, 2, 3, 4, 0],
        [9, 0, 2, 3, 4, 0, 6, 7, 8],
    ]
    with pytest.raises(ValueError) as exc:
        validate_sudoku(sudoku_wrong)
        assert "The same numbers in the string (column,block). Unsolvable sudoku" == str(exc.value)


def test_validate_sudoku_column():
    """
    Проверка входящего судоку на одинаковые цифры в столбце
    :return: True or False
    """
    sudoku_wrong = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 0, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 0, 6],
        [2, 3, 4, 0, 6, 7, 8, 9, 1],
        [0, 6, 7, 8, 9, 1, 2, 3, 4],
        [2, 9, 1, 0, 3, 4, 0, 6, 7],
        [3, 4, 0, 6, 7, 8, 9, 1, 2],
        [6, 7, 8, 9, 1, 2, 3, 4, 0],
        [9, 0, 2, 3, 4, 0, 6, 7, 8],
    ]
    with pytest.raises(ValueError) as exc:
        validate_sudoku(sudoku_wrong)
        assert "The same numbers in the string (column,block). Unsolvable sudoku" == str(exc.value)


def test_validate_sudoku_block():
    """
    Проверка входящего судоку на одинаковые цифры в блоке 3*3
    :return: True or False
    """
    sudoku_wrong = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    with pytest.raises(ValueError) as exc:
        validate_sudoku(sudoku_wrong)
        assert "The same numbers in the string (column,block). Unsolvable sudoku" == str(exc.value)


def test_validate_sudoku_type():
    """
    Проверка входящего судоку на тип данных(допускаются только целые цифры)
    :return: True or False
    """
    sudoku_wrong = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, "m", 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    with pytest.raises(TypeError) as exc:
        validate_sudoku(sudoku_wrong)
        assert "sudoku can only enter numbers from 0 to 9 inclusive" == str(exc.value)


def test_validate_sudoku_num():
    """
    Проверка входящего судоку на интервал входящих цифр(допускаются только цифры от 0 до 9)
    :return: True or False
    """
    sudoku_wrong = [
        [1, -1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    with pytest.raises(TypeError) as exc:
        validate_sudoku(sudoku_wrong)
        assert "sudoku can only enter numbers from 0 to 9 inclusive" == str(exc.value)

    # def test__box_slice():
    """
    Проверяет правильность возвращаемого слайса
    :return: слайс
    """
    assert _box_slice(3) == slice(3, 6, None)


def test_solve():
    """
    Проверяет работу функции.
    :return: вместо пустых значений таблицы, обозначенных нулем, подставляет 5.
    """
    sudoku_start = [
        [1, 2, 3, 4, 0, 6, 7, 8, 9],
        [4, 0, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 0, 6],
        [2, 3, 4, 0, 6, 7, 8, 9, 1],
        [0, 6, 7, 8, 9, 1, 2, 3, 4],
        [8, 9, 1, 2, 3, 4, 0, 6, 7],
        [3, 4, 0, 6, 7, 8, 9, 1, 2],
        [6, 7, 8, 9, 1, 2, 3, 4, 0],
        [9, 0, 2, 3, 4, 0, 6, 7, 8],
    ]
    sudoku_solved = solve(sudoku_start)
    assert sudoku_solved == [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [9, 1, 2, 3, 4, 5, 6, 7, 8],
    ]

    # def test__find_unassigned():
    """
    Ищет пустое значение в таблице
    :return: координаты пустого значения в таблице
    """
    assert _find_unassigned(
        [
            [1, 2, 3, 4, 0, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [2, 3, 4, 5, 6, 7, 8, 9, 1],
            [5, 6, 7, 8, 9, 1, 2, 3, 4],
            [8, 9, 1, 2, 3, 4, 5, 6, 7],
            [3, 4, 5, 6, 7, 8, 9, 1, 2],
            [6, 7, 8, 9, 1, 2, 3, 4, 5],
            [9, 1, 2, 3, 4, 5, 6, 7, 8],
        ]
    ) == (0, 4)


def test_solve_with_all_empty_cells():
    """
    Работа функции с пустым судоку
    :return: True or False
    """
    sudoku_start = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    sudoku_solved = solve(sudoku_start)
    assert sudoku_solved == [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 1, 4, 3, 6, 5, 8, 9, 7],
        [3, 6, 5, 8, 9, 7, 2, 1, 4],
        [8, 9, 7, 2, 1, 4, 3, 6, 5],
        [5, 3, 1, 6, 4, 2, 9, 7, 8],
        [6, 4, 2, 9, 7, 8, 5, 3, 1],
        [9, 7, 8, 5, 3, 1, 6, 4, 2],
    ]


def test_solved_sudoku():
    """
    Работа функции с уже правильно решенным судоку.
    :return: Булево
    """
    sudoku_start = [
        [1, 2, 6, 9, 7, 5, 8, 3, 4],
        [3, 5, 8, 4, 1, 2, 6, 9, 7],
        [9, 7, 4, 6, 8, 3, 1, 2, 5],
        [2, 3, 5, 1, 3, 8, 7, 6, 9],
        [6, 8, 9, 2, 5, 7, 4, 1, 3],
        [7, 4, 1, 3, 6, 9, 5, 8, 2],
        [8, 6, 2, 7, 3, 4, 9, 5, 1],
        [4, 1, 3, 5, 9, 6, 2, 7, 8],
        [5, 9, 7, 8, 2, 1, 3, 4, 6],
    ]
    sudoku_solved = solve(sudoku_start)
    assert sudoku_solved == [
        [1, 2, 6, 9, 7, 5, 8, 3, 4],
        [3, 5, 8, 4, 1, 2, 6, 9, 7],
        [9, 7, 4, 6, 8, 3, 1, 2, 5],
        [2, 3, 5, 1, 3, 8, 7, 6, 9],
        [6, 8, 9, 2, 5, 7, 4, 1, 3],
        [7, 4, 1, 3, 6, 9, 5, 8, 2],
        [8, 6, 2, 7, 3, 4, 9, 5, 1],
        [4, 1, 3, 5, 9, 6, 2, 7, 8],
        [5, 9, 7, 8, 2, 1, 3, 4, 6],
    ]
