

from flask import Flask, render_template, json, request
from flask_mysqldb import MySQL

# from werkzeug import generate_password_hash, check_password_hash


app = Flask(__name__)

app.config['MYSQL_HOST'] = '206.189.71.70'
app.config['MYSQL_USER'] = 'bhabani'
app.config['MYSQL_PASSWORD'] = 'wisdom'
app.config['MYSQL_DB'] = 'haricut'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# app.secret_key = 'UPDATETHISPART'
mysql = MySQL(app)




@app.route("/")
def default():
	return render_template('home.html')


@app.route("/main")
def mainPage():
	return render_template('home.html')


@app.route('/signUpPage')
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
