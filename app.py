import os
from flask import Flask, request, abort, jsonify, Response
from utils import get_query
from typing import Optional, Union, List

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query/")
def perform_query() -> Response:
    cmd1: Optional[str] = request.args.get('cmd1')
    val1: Optional[str] = request.args.get('val1')
    cmd2: Optional[str] = request.args.get('cmd2')
    val2: Optional[str] = request.args.get('val2')
    file_name: Optional[str] = request.args.get('file_name')
    if not (cmd1 and val1 and file_name):
        abort(400, 'Нет необходимого минимума команд!')

    file_path: str = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        return abort(400, 'File not found')

    with open(file_path) as file:
        result: Union[str, List] = get_query(cmd1, val1, file)
        if cmd2 and val2:
            result = get_query(cmd2, val2, result)
        return jsonify(result)

    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат
    # return app.response_class('', content_type="text/plain")


if __name__ == '__main__':
    app.run(debug=True)
