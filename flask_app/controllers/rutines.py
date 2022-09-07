from flask import render_template, redirect, session, request, flash #importaciones de módulos de flask
from flask_app import app
from flask_app.controllers import users
from flask_app.models.rutine import Rutine

@app.route('/addrutine')
def addrutine():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('add_rutine.html')

@app.route('/add/rutine/secure', methods=['post'])
def addrutinesecure():
    if not Rutine.valida_rutina(request.form):
        return render_template('add_rutine.html')
    rutine = Rutine.addrutinesecure(request.form)
    return redirect('/dashboard')
    

@app.route('/delete/rutine/<int:id>')
def deleterutine(id):
    if 'user_id' not in session:
        return redirect('/')
    formulario = {
        'id':id
    }
    delete = Rutine.delete(formulario)
    return redirect('/dashboard')

@app.route('/edit/rutine/<int:id>')
def editrutine(id):
    if 'user_id' not in session:
        return redirect('/')
    formulario = {
        'id':id
    }
    rutine = Rutine.edit(formulario)
    return render_template('edit_rutine.html', rutine=rutine)


@app.route('/edit/rutine/secure', methods=['post'])
def editrutine2():
    if 'user_id' not in session:
        return redirect('/')
    if not Rutine.valida_rutina(request.form):
        return redirect('/edit/rutine/'+request.form['id'])
    formulario = {
        'id':request.form['id'],
        'name':request.form['name'],
        'type_rutine':request.form['type_rutine'],
        'time':request.form['time'],
        'description':request.form['description']
    }
    Rutine.edittwo(formulario)
    return redirect('/dashboard')


@app.route('/see/rutine/<int:id>')
def seerutine(id):
    if 'user_id' not in session:
        return redirect('/')
    formulario = {
        'id':id
    }
    rutine = Rutine.edit(formulario)
    return render_template('see_rutine.html', rutine=rutine)


@app.route('/like/rutine/<int:id>/<int:idtwo>')
def likerutine(id, idtwo):
    if 'user_id' not in session:
        return redirect('/')
    formulario = {
        'rutine_id':id,
        'user_id':idtwo
    }
    rutine = Rutine.rutinelike(formulario)
    return redirect('/dashboard')
