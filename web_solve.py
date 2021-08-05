from decision_sudoku import solve
from solve_sudoku import validate_sudoku
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    """
    Заполняем начальную форму судоку нулями, затем когда пользователь вводит данные:
    1) Проверяем введенные данные на валидность переиспользуя функцию "validate_sudoku".
    2) Если данные валидны, решаем судоку переиспользуя функцию "solve", возвращам заполненную таблицу с решенным судоку.
    """
    a = []
    if request.method == 'POST':
        s = request.form
        for i in s:
            a.append(int(s[i]))
        sudoku = [a[i:i+9] for i in range(0, len(a), 9)]
        validate_sudoku(sudoku) 
        solve(sudoku)       
        return render_template('index.html', sudoku=sudoku)           
    return render_template('index.html')

@app.errorhandler(500)
def InternalServerErorr(error):
    """
     Если данные не валидны, ловим ошибку, возвращаем сообщение об ошибке.
    """
    return render_template('index.html', a=True)


if __name__ == '__main__':
    app.run()

