from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/test1'
app.config['SQLALCHEMY_BINDS'] = {
    'test2': 'mysql+pymysql://root:root@localhost:3306/test2',
    'test1': 'mysql+pymysql://root:root@localhost:3306/test1'
}
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "tb_user"
    __bind_key__ = 'test2'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Store(db.Model):
    __tablename__ = "tb_store"
    __bind_key__ = 'test1'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, primary_key=True)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/user")
def get_user():
    return User.query.scalar().name


@app.route("/store")
def get_store():
    return Store.query.scalar().name


app.run(host='0.0.0.0', port='8878')
