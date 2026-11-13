from flask import Flask, flash, redirect, render_template, request, url_for
import mysql
app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def index():
    con = mysql.connection.cursor()
    con.execute('SELECT * FROM tb_albums')
    conAlbums = con.fetchall()
    print(conAlbums)
    return render_template('index.html', listAlbums = conAlbums)


@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        titulo = request.form['txtTitulo']
        artista = request.form['txtArtista']
        anio = request.form['txtAnio']
        calificacion = request.form['txtCalificacion']
        resenia = request.form['txtResenia']
        print(titulo, artista, anio, calificacion, resenia)

        con = mysql.connection.cursor()
        con.execute('INSERT INTO tb_albums (titulo, artista, anio, calificacion, resenia) VALUES (%s, %s, %s, %s, %s)', (titulo, artista, anio, calificacion, resenia))
        mysql.connection.commit()

    flash('El album fue agregado correctamente')
    return redirect (url_for('index'))

@app.route('/editar/<int:id>')
def editar(id):
    con = mysql.connection.cursor()
    con.execute('SELECT * FROM tb_albums WHERE id = %s', (id,))
    consultarId = con.fetchone()
    con.close()
    return render_template('editarAlbum.html', Album = consultarId)

@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        titulo = request.form['txtTitulo']
        artista = request.form['txtArtista']
        anio = request.form['txtAnio']
        calificacion = request.form['txtCalificacion']
        resenia = request.form['txtResenia']

        con = mysql.connection.cursor()
        con.execute('UPDATE tb_albums SET titulo = %s, artista = %s, anio = %s, calificacion = %s, resenia = %s WHERE id = %s', (titulo, artista, anio, calificacion, resenia, id))
        mysql.connection.commit()

    flash('Se actualizó el album '+titulo)
    return redirect(url_for('index'))

@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    if request.method == 'POST':
        titulo = request.form['txtTitulo']

        con = mysql.connection.cursor()
        con.execute('DELETE FROM tb_albums WHERE id = %s', (id,))
        mysql.connection.commit()

    flash('Se eliminó el album '+titulo)
    return redirect(url_for('index'))