from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
app.secret_key = "cambia_esta_clave"

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "BancoSangre",
    "port": 3306
}

def conectar():
    return mysql.connector.connect(**DB_CONFIG)

def pagina(nombre, titulo, rol=None):
    return render_template(nombre, titulo=titulo, rol=rol)

@app.route("/")
def inicio():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        correo = request.form.get("correo", "")
        contrasena = request.form.get("contrasena", "")
        try:
            con = conectar()
            cur = con.cursor(dictionary=True)
            cur.execute("SELECT * FROM Usuario WHERE correo=%s AND estado=1", (correo,))
            usuario = cur.fetchone()
            cur.close(); con.close()
            # En una aplicación real se verifica el hash de la contraseña.
            if usuario and usuario["contrasena"] == contrasena:
                session["usuario_id"] = usuario["id_usuario"]
                session["rol"] = usuario["rol"]
                if usuario["rol"] == "Administrador":
                    return redirect(url_for("admin_dashboard"))
                if usuario["rol"] == "Medico":
                    return redirect(url_for("medico_dashboard"))
                return redirect(url_for("donante_dashboard"))
            flash("Correo o contraseña incorrectos.")
        except Error:
            flash("No se pudo conectar con la base de datos. Verifica la configuración.")
    return pagina("I01_login.html", "Inicio de sesión")

@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        try:
            con = conectar(); cur = con.cursor()
            cur.execute("""INSERT INTO Usuario(nombre, apellido_paterno, apellido_materno, correo, contrasena, telefono, rol)
                VALUES (%s,%s,%s,%s,%s,%s,'Donante')""",
                (request.form["nombre"], request.form["apellido_paterno"], request.form.get("apellido_materno",""),
                 request.form["correo"], request.form["contrasena"], request.form.get("telefono","")))
            uid=cur.lastrowid
            cur.execute("""INSERT INTO Donante(id_usuario, fecha_nacimiento, sexo, CURP, domicilio, tipo_sangre, factor_Rh)
                VALUES (%s,%s,%s,%s,%s,%s,%s)""",
                (uid, request.form["fecha_nacimiento"], request.form["sexo"], request.form["curp"],
                 request.form.get("domicilio",""), request.form["tipo_sangre"], request.form["factor_rh"]))
            con.commit(); cur.close(); con.close()
            flash("Registro completado. Ya puedes iniciar sesión.")
            return redirect(url_for("login"))
        except Error as e:
            flash("No se pudo completar el registro. Revisa los datos y la base de datos.")
    return pagina("I02_registro.html", "Registro de donante")

@app.route("/recuperar")
def recuperar():
    return pagina("I03_recuperar.html", "Recuperar contraseña")

@app.route("/admin")
def admin_dashboard():
    return pagina("I04_admin_dashboard.html", "Dashboard - Administrador", "Administrador")

@app.route("/admin/usuarios")
def usuarios():
    return pagina("I05_usuarios.html", "Gestión de usuarios", "Administrador")

@app.route("/admin/medicos")
def medicos():
    return pagina("I06_medicos.html", "Gestión de médicos", "Administrador")

@app.route("/admin/donantes")
def admin_donantes():
    return pagina("I07_donantes.html", "Gestión de donantes", "Administrador")

@app.route("/admin/citas")
def admin_citas():
    return pagina("I08_citas.html", "Gestión de citas", "Administrador")

@app.route("/admin/sedes")
def sedes():
    return pagina("I09_sedes.html", "Gestión de sedes y horarios", "Administrador")

@app.route("/admin/campanas")
def campanas():
    return pagina("I10_campanas.html", "Gestión de campañas", "Administrador")

@app.route("/admin/reportes")
def reportes():
    return pagina("I11_reportes.html", "Reportes y estadísticas", "Administrador")

@app.route("/medico")
def medico_dashboard():
    return pagina("I12_medico_dashboard.html", "Dashboard - Médico", "Medico")

@app.route("/medico/donantes")
def lista_donantes():
    return pagina("I13_lista_donantes.html", "Lista de donantes", "Medico")

@app.route("/medico/citas")
def citas_medicas():
    return pagina("I14_citas_medicas.html", "Gestión de citas médicas", "Medico")

@app.route("/medico/valoracion")
def valoracion():
    return pagina("I15_valoracion.html", "Valoración médica y registro de donación", "Medico")

@app.route("/medico/historial")
def historial():
    return pagina("I16_historial.html", "Historial de donaciones", "Medico")

@app.route("/donante")
def donante_dashboard():
    return pagina("I17_donante_dashboard.html", "Dashboard - Donante", "Donante")

@app.route("/donante/perfil")
def perfil():
    return pagina("I18_perfil.html", "Perfil del donante", "Donante")

@app.route("/donante/solicitar")
def solicitar_cita():
    return pagina("I19_solicitar_cita.html", "Solicitar cita de donación", "Donante")

@app.route("/donante/citas")
def mis_citas():
    return pagina("I20_mis_citas.html", "Mis citas e historial de donaciones", "Donante")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
