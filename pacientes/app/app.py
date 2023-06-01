from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_mysqldb import MySQL

import psycopg2
from psycopg2 import DatabaseError

app = Flask(__name__)

@app.route('/pacientes')
def listar_cursos():

    data = {}

    conn = psycopg2.connect("postgresql://postgres:isis2503@10.128.0.27:5432/postgres")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pacientes")

    rows = cursor.fetchall()

    data['pacientes'] = rows

    for row in rows:
        print(row)

    return render_template('Pacientes/pacientes.html', data=data)


def pagina_no_encontrada(error):
    # return render_template('404.html'), 404
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(host="0.0.0.0", port=8080)
