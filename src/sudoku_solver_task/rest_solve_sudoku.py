from src.sudoku_solver_task.cli_solve_sudoku import validate_sudoku


from flask import Flask, request


from src.sudoku_solver_task.sudoku_solver import solve


app = Flask(__name__)


@app.route("/solve", methods=["POST"])
def update_sudoku() -> dict:
    """
    Принимаем нерешенный судоку из json-файла, проверяем его данные
    на валидность, валидный судоку решаем, невалидный вызовет исключение,
    возвращаем решенный судоку или сообщение об ошибке.

    Returns:
        dict: [Решенный судоку]
    """
    sudoku_table = request.json["table"]
    validate_sudoku(sudoku_table)
    solve(sudoku_table)
    return {"table": sudoku_table}


if __name__ == "__main__":
    app.run()
