from flask_app.config.mysqlconnection import connectToMySQL

import re #Importamos expresiones regulares
#crear una expresión regular para verificar que tengamos el email con formato correcto
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PWD_REGEX=re.compile("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")

from flask import flash #mandar mensajes a la plantilla
from flask_app.models import rutine

class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.type_user = data['type_user']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.rutines = [] #así sabremos qu ruinas son del usuario 
        self.rutine_like = [] #asi sabremos que rutinas le gustan 

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO users(first_name, last_name, email, password, type_user) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, %(type_user)s)"
        result = connectToMySQL('gym').query_db(query, formulario) #1 - Insert recibe id
        return result #result = Identificador del nuevo registro

    @staticmethod
    def valida_usuario(formulario):
        es_valido = True
        
        if len(formulario['first_name']) < 3:
            flash('Name must have at least 3 characters', 'register')
            es_valido = False
        
        if len(formulario['last_name']) < 3:
            flash('Last name must have at least 3 characters', 'register')
            es_valido = False
        
        if not EMAIL_REGEX.match(formulario['email']): 
            flash('Invalid e-mail', 'register')
            es_valido = False

        if not PWD_REGEX.match(formulario['password']):
            flash('Password must have at least 8 characters, a special character, a number, an uppercase and a lowercase', 'register')
            es_valido = False

        
        if formulario['password'] != formulario['confirm_password']:
            flash('Passwords do not match', 'register')
            es_valido = False

        if formulario['type_user'] == "":
            flash('You must choose a type of user', 'register')
            es_valido = False
        
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('gym').query_db(query, formulario)
        if len(results) >= 1:
            flash('previously registered e-mail', 'register')
            es_valido = False

        return es_valido

    @classmethod
    def get_by_email(cls, formulario):
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL('gym').query_db(query, formulario)
        if len(result) < 1:
            return False
        else:
            #result = [ {first_name: Elena, last_name: De Troya.....} ]
            user = cls(result[0]) #Haciendo una instancia de User -> CON los datos que recibimos de la base de datos
            return user

    @classmethod
    def get_by_id(cls, formulario):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('gym').query_db(query, formulario) #Select recibe lista
        user = cls(result[0])
        return user