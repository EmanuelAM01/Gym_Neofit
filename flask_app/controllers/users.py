from flask import render_template, redirect, session, request, flash #importaciones de módulos de flask
from flask_app import app

#Importando el Modelo de User
from flask_app.models.user import User
from flask_app.models.rutine import Rutine

#Importando BCrypt (encriptar)
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app) #inicializando instancia de Bcrypt

@app.route('/')
def index():
    return render_template('log_reg.html')

@app.route('/register', methods=['POST'])
def register():
    if not User.valida_usuario(request.form):
        return redirect('/')
    pwd = bcrypt.generate_password_hash(request.form['password']) #Me encripta el password
    formulario = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "type_user": request.form['type_user'],
        "password": pwd
    }
    id = User.save(formulario) #Guardando a mi usuario y recibo el ID del nuevo registro
    session['user_id'] = id #Guardando en sesion el identificador
    return redirect('/dashboard')


@app.route('/login', methods=['POST'])
def login():
    user = User.get_by_email(request.form)
    if not user: #si user=False
        flash("e-mail not found", 'login')
        return redirect('/')

    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Wrong password", 'login')
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    formulario = {
        "id": session['user_id']
    }
    user = User.get_by_id(formulario)
    rutines = Rutine.all_rutines()        
    return render_template('dashboard.html', rutines=rutines, user=user)

@app.route('/logout')
def logout():
    session.clear() #Elimine la sesión
    return redirect('/')