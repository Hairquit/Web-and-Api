
from database import mysql
from flask_restplus import Namespace, Resource, fields
from flask import json, request

api = Namespace('Users', description='Users related operations')


@api.route('/signUp')
class SignUpUser(Resource):
    @api.doc('signs up users')
    def post(self):
        """This route to signup page"""
        # create user code will be here !!
        # read the posted values from the UI
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # validate the received values
        if _name and _email and _password:
            con = mysql.connection
            cur = mysql.connection.cursor()
            cur.callproc('sp_createUser', (_name, _email, _password))
            data = cur.fetchall()
            if len(data) is 0:
                con.commit()
                return json.dumps({'message': 'User created successfully !'})
            else:
                return json.dumps({'error': str(data[0])})
            return json.dumps({'html': '<span>All fields good !!</span>'})
        else:
            return json.dumps({'html': '<span>Enter the required fields</span>'})



@api.route('/')
class ListUser(Resource):
    @api.doc('lists users')
    def get(self):
        """ post the new user info to the database"""
        cur = mysql.connection.cursor()
        cur.execute('''select * from haricut.tbl_user''')
        rv = cur.fetchall()
        return str(rv)
