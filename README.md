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
Входной файл следует вводить в соответствии с шаблоном заполнения (sudoku.json).
Для решения следует ввести в консоли вот так: `python3 путь_до_файла_solve_sudoku.py путь_до_файла_название_входного_файла.json путь_до файла_название_файла_с_результатом.json`
Предусмотрен тестовый файл с набором тестов функций для решения.
Предусмотрена проверка входящего судоку на корректность, с механизмом исключений.
В качестве фреймворка для тестирования выбран pytest.
Добавлен контроль качества кода с помощью flake8 + доп.плагины.
Форматирование с помощью black.
Все зависимости занесены в файл requirements.txt
Добавлена реализация rest-api http-сервера с функциональностью решения судоку.
Сервер по запросу post по пути /solve с приложенным судоку в виде json выдает либо решённый судоку, либо сообщает об ошибке.
Для реализации сервера использован flask.
