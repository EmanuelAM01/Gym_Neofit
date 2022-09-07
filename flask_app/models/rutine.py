from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user


class Rutine:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.type_rutine = data['type_rutine']
        self.time = data['time']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.num_likes = data['num_likes']

    @staticmethod
    def valida_rutina(formulario):
        es_valido = True
        
        if len(formulario['name']) < 3:
            flash('The routine must have a name of at least one character', 'routine')
            es_valido = False
        
        if len(formulario['description']) < 10:
            flash('The routine must have a description of at least 10 characters', 'routine')
            es_valido = False
        
        if formulario['time'] == "":
            flash('You must choose the duration time of the routine', 'routine')
            es_valido = False

        if formulario['type_rutine'] == "":
            flash('You must choose what type of routine it is', 'routine')
            es_valido = False
        
        return es_valido

    @classmethod
    def addrutinesecure(cls, formulario):
        query = "INSERT INTO rutines(name, type_rutine, time, description, user_id) VALUES (%(name)s, %(type_rutine)s, %(time)s, %(description)s, %(user_id)s)"
        result = connectToMySQL('gym').query_db(query, formulario) #1 - Insert recibe id
        return result

    @classmethod
    def all_rutines(cls):
        query = "Select rutines.*, users.first_name, users.last_name from rutines left join users on rutines.user_id = users.id;"
        results = connectToMySQL('gym').query_db(query) 
        print(results)
        rutines = []
        if results == ():
            return None
        else:
            for result in results:
                formulario= {
                    "id":result['id']
                }
                query2 = "select count(*) as num_likes from likes where rutine_id='%(id)s';"
                resultstwo = connectToMySQL('gym').query_db(query2, formulario) 
                superresults={
                    'id': result['id'],
                    'name':result['name'],
                    'type_rutine':result['type_rutine'],
                    'time':result['time'],
                    'description':result['description'],
                    'created_at':result['created_at'],
                    'updated_at':result['updated_at'],
                    'user_id':result['user_id'],
                    'first_name':result['first_name'],
                    'last_name':result['last_name'],
                    'num_likes': resultstwo[0]['num_likes']
                }
                rutines.append(cls(superresults))
            return rutines

    @classmethod
    def delete(cls, formulario):
        query2= "DELETE FROM likes WHERE rutine_id=%(id)s;"
        result2= connectToMySQL('gym').query_db(query2,formulario)
        query = "DELETE FROM rutines WHERE id=%(id)s;"
        results = connectToMySQL('gym').query_db(query,formulario) 
        return results

    @classmethod
    def edit(cls, formulario):
        #query = "Select rutines.*, users.first_name, users.last_name, count(*) as num_likes from rutines left join users on rutines.user_id = users.id left join likes on likes.rutine_id = rutines.id where rutines.id = %(id)s;"
        query= "Select rutines.*, users.first_name, users.last_name, count(likes.rutine_id) as num_likes from rutines left join users on rutines.user_id = users.id left join likes on likes.rutine_id = rutines.id where rutines.id = %(id)s;"
        result = connectToMySQL('gym').query_db(query,formulario)
        print(result)
        return cls(result[0])

    @classmethod
    def edittwo(cls, formulario):
        query = "update rutines set name=%(name)s, type_rutine=%(type_rutine)s, time=%(time)s, description=%(description)s where id=%(id)s;"
        result = connectToMySQL('gym').query_db(query,formulario)
        return result

    @classmethod
    def rutinelike(cls, formulario):
        query = "insert into likes(user_id, rutine_id) values ( %(user_id)s , %(rutine_id)s );"
        result = connectToMySQL('gym').query_db(query,formulario)
        return result
    