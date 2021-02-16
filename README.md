# Проект решателя судоку

**Цель** - обучиться использовать различные технологии в связке. В качестве ядра логики выбран алгоритм решения судоку, поскольку:
- суть судоку понятна всем
- алгоритмы по решению легко формализуемы
- работа алгоритма - это CPU-bound задача
- его можно "обвесить" различными пользовательскими и разработческими сценариями

## Описание проекта

Данный проект реализует решение судоку любой сложности методом простого перебора значений. 
Решение выполняется только один раз, даже если решений несколько.
Решение оформлено в виде консольной утилиты.
В сопровождении решения предусмотрены входной файл(sudoku.json) с шаблоном заполнения, и файл с результатом решения(result.json).
Для решения следует ввести в консоли вот так: python3 путь_до_файла_solve_sudoku путь_до файла_sudoku.json
Уже решенное судоку следует смотреть в result.json(будет создан или перезаписан, в каталоге из которого запускается решение).   
Предусмотрен тестовый файл с набором тестов функций для решения.
Предусмотрена проверка входящего судоку на корректность, с механизмом исключений.
В качестве фреймворка для тестирования выбран PYTEST.

