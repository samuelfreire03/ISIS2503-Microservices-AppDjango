from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Conexión MySQL
app.config['MYSQL_HOST'] = 'DESKTOP-40E9AHV'
app.config['MYSQL_USER'] = 'pacientes_user1'
app.config['MYSQL_PASSWORD'] = 'Isis2503'
app.config['MYSQL_DB'] = 'pacientes_db'

conexion = MySQL(app)


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
    data = {}
    cursor = conexion.connection.cursor()
    sql = "SELECT id, nombre, tipo FROM pacientes"
    cursor.execute(sql)
    cursos = cursor.fetchall()
    print(cursos)
    data['cursos'] = cursos
    data['mensaje'] = 'Exito'
    return jsonify(data)


def pagina_no_encontrada(error):
    # return render_template('404.html'), 404
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True,host="0.0.0.0", port=8080)
