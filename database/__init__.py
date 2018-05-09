from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy

alchemydb = SQLAlchemy()
mysql = MySQL()

class Saloon(alchemydb.Model):
    id = alchemydb.Column(alchemydb.Integer, primary_key=True)
    saloonName = alchemydb.Column(alchemydb.String(80), unique=True, nullable=False)
    saloonAddress = alchemydb.Column(alchemydb.String(120), unique=True, nullable=False)
    capacity = alchemydb.Column(alchemydb.Integer, unique=False, nullable=True)
    customerCnt = alchemydb.Column(alchemydb.Integer, unique=False, nullable=True)
    waitTime = alchemydb.Column(alchemydb.Integer, unique=False, nullable=True)

    def __repr__(self):
        return '<saloon %r>' % self.saloonName

