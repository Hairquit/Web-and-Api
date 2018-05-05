

from flask import Flask, render_template, json, request
from flask_mysqldb import MySQL
from flask_restplus import fields, Api, Resource
# from werkzeug import generate_password_hash, check_password_hash


app = Flask(__name__)
api = Api(app)

app.config.from_object('config')
mysql = MySQL(app)


@app.route("/")
def default():
	return render_template('home.html')


@app.route("/main")
def mainPage():
    """ 
        router for the main method
    """
    return render_template('home.html')


@app.route('/register')
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp', methods=['POST'])
def signUp():
    # create user code will be here !!
# read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

	 # validate the received values
    if _name and _email and _password:
        con =mysql.connection
        cur = mysql.connection.cursor()
        cur.callproc('sp_createUser', (_name, _email, _password))
        data = cur.fetchall()
        if len(data) is 0:
            con.commit()
            return json.dumps({'message':'User created successfully !'})
        else:
            return json.dumps({'error':str(data[0])})
        return json.dumps({'html': '<span>All fields good !!</span>'})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

if __name__ == "__main__":
    app.run(debug=True)
