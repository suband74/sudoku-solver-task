from decision_sudoku import box_slice, solve, find_unassigned


def test_box_slice():
    """
    Проверяет правильность возвращаемого слайса
    :return: слайс
    """
    assert box_slice(3) == slice(3, 6, None)


def test_solve():
    """
    Проверяет работу функции.
    :return: вместо пустых значений таблицы, обозначенных нулем, подставляет 5.
    Считаются контрольные суммы в строках и в столбцах.
    """
    s = [[1, 2, 3, 4, 0, 6, 7, 8, 9],
         [4, 0, 6, 7, 8, 9, 1, 2, 3],
         [7, 8, 9, 1, 2, 3, 4, 0, 6],
         [2, 3, 4, 0, 6, 7, 8, 9, 1],
         [0, 6, 7, 8, 9, 1, 2, 3, 4],
         [8, 9, 1, 2, 3, 4, 0, 6, 7],
         [3, 4, 0, 6, 7, 8, 9, 1, 2],
         [6, 7, 8, 9, 1, 2, 3, 4, 0],
         [9, 0, 2, 3, 4, 0, 6, 7, 8]]
    solve(s)
    assert s == [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [9, 1, 2, 3, 4, 5, 6, 7, 8]
    ]
    solve(s)
    for i in s:
        assert sum(i) == 45
    a = list(zip(*s))
    for k in a:
        assert sum(k) == 45


def test_solve1():
    """
    Проверяет корректность судоку.
    :return: True or False
    """
    s = [
        [1, 2, 6, 9, 7, 5, 8, 3, 4],
        [3, 5, 8, 4, 1, 2, 6, 9, 7],
        [9, 7, 4, 0, 8, 3, 1, 2, 5],
        [2, 3, 5, 0, 3, 8, 7, 6, 9],
        [6, 8, 9, 0, 5, 7, 4, 1, 3],
        [7, 4, 1, 3, 6, 9, 5, 8, 2],
        [8, 6, 2, 7, 3, 4, 9, 5, 1],
        [4, 1, 3, 5, 9, 6, 2, 7, 8],
        [5, 9, 7, 8, 2, 1, 3, 4, 6]
    ]
    solve(s)
    assert s == [
        [1, 2, 6, 9, 7, 5, 8, 3, 4],
        [3, 5, 8, 4, 1, 2, 6, 9, 7],
        [9, 7, 4, 6, 8, 3, 1, 2, 5],
        [2, 3, 5, 1, 4, 8, 7, 6, 9],
        [6, 8, 9, 2, 5, 7, 4, 1, 3],
        [7, 4, 1, 3, 6, 9, 5, 8, 2],
        [8, 6, 2, 7, 3, 4, 9, 5, 1],
        [4, 1, 3, 5, 9, 6, 2, 7, 8],
        [5, 9, 7, 8, 2, 1, 3, 4, 6]
    ]


def test_find_unassigned():
    """
    Ищет пустое значение в таблице
    :return: координаты пустого значения в таблице
    """
    assert find_unassigned([
        [1, 2, 3, 4, 0, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [9, 1, 2, 3, 4, 5, 6, 7, 8]
    ]) == (0, 4)


def test_solve2():
    """
    Control not empty sudoky.
    :return: True or False
    """
    s = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    count = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] != 0:
                count += 1
    assert count > 0


def test_solve3():
    """
    Если судоку полностью заполненный.
    :return: True or False
    """
    s = [
        [1, 2, 6, 9, 7, 5, 8, 3, 4],
        [3, 5, 8, 4, 1, 2, 6, 9, 7],
        [9, 7, 4, 0, 8, 3, 1, 2, 5],
        [2, 3, 5, 0, 3, 8, 7, 6, 9],
        [6, 8, 9, 0, 5, 7, 4, 1, 3],
        [7, 4, 1, 3, 6, 9, 5, 8, 2],
        [8, 6, 2, 7, 3, 4, 9, 5, 1],
        [4, 1, 3, 5, 9, 6, 2, 7, 8],
        [5, 9, 7, 8, 2, 1, 3, 4, 6]
    ]
    for i in s:
        if all(i):
            assert False
