from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_mysqldb import MySQL

import psycopg2
from psycopg2 import DatabaseError

app = Flask(__name__)

@app.route('/')
def index():
    # return "<h1>UskoKruM2010 - Suscríbete!</h1>"
    cursos = ['PHP', 'Python', 'Java', 'Kotlin', 'Dart', 'JavaScript']
    data = {
        'titulo': 'Index123',
        'bienvenida': '¡Saludos!',
        'cursos': cursos,
        'numero_cursos': len(cursos)
    }
    return render_template('index.html', data=data)


@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    data = {
        'titulo': 'Contacto',
        'nombre': nombre,
        'edad': edad
    }
    return render_template('contacto.html', data=data)


@app.route('/cursos')
def listar_cursos():

    conn = psycopg2.connect("postgresql://postgres:isis2503@10.128.0.27:5432/postgres")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pacientes")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    return jsonify([])


def pagina_no_encontrada(error):
    # return render_template('404.html'), 404
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(host="0.0.0.0", port=8080)
