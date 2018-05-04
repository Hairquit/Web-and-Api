

from flask import Flask , render_template 
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '206.189.71.70'
app.config['MYSQL_USER'] = 'bhabani'
app.config['MYSQL_PASSWORD'] = 'wisdom'
app.config['MYSQL_DB']= 'haircut'

mysql = MySQL(app)

@app.route("/")
def hello():
	return render_template('home.html')

if __name__ == "__main__":
	app.run(debug=True)
 
