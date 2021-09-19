from decision_sudoku import solve

from flask import Flask, jsonify, request

from solve_sudoku import validate_sudoku


app = Flask(__name__)

client = app.test_client()


@app.route("/solve", methods=["GET"])
def get_sudoku() -> jsonify:

    sudoku = {
        "table": [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ],
    }
    return jsonify(sudoku)


@app.route("/solve", methods=["POST"])
def update_sudoku() -> jsonify:
    """
    Принимаем нерешенный судоку из json-файла, проверяем его данные на валидность, валидный судоку решаем,
    невалидный вызовет исключение,возвращаем решенный судоку или сообщение об ошибке.

    Returns:
        jsonify: [description]
    """
    sudoku = {
        "table": [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ],
    }

    new_one = request.json
    sudoku.update(new_one)
    validate_sudoku(sudoku["table"])
    solve(sudoku["table"])
    return jsonify(sudoku)


if __name__ == "__main__":
    app.run()
