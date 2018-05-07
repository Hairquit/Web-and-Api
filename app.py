"""This app module which starts the haircut application"""
import os
import logging.config
from flask import Flask, render_template, json, request
# from flask_mysqldb import MySQL
# from apis import api
from database import mysql
from apis import blueprint as api
# from werkzeug import generate_password_hash, check_password_hash

logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object('config')


@app.route("/")
@app.route('/index.html', alias=True)
@app.route("/main" , alias=True)
def default():
    """ router for the default url """
    return render_template('home.html')


@app.route('/register')
def show_sign_up():
    """This route to signup page"""
    return render_template('signup.html')



def main():
    """main function initialize the haircut application"""
    log.info('> Starting development server at http://localhost:5000 <')
    log.info('> apis running at http://localhost:5000/api <')
    # api.init_app(app)
    app.register_blueprint(api, url_prefix='/api')
    mysql.init_app(app)
    app.run(debug=True)


if __name__ == "__main__":
    main()
    # app.run(debug=True)
