from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime 


database_path='postgresql://postgres:12345678@pi3.ccbfa26cin0h.us-east-1.rds.amazonaws.com:5432/postgres'

#Configuracion
db=SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        db.init_app(app)
        db.create_all()

#Modelos
class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key = True)
    name_category = db.Column(db.String(50), nullable = False)
    posts = db.relationship('Post', backref = 'category', lazy = 'joined')

    #Metodo que formatee el objeto a json para devolverlo a mi API y que no de errores
    def format(self):
        return {
            'id':self.id,
            'name_category':self.name_category
        }

    #Metodo que permite la inserción de un post a través de nuestra API
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    modificated = db.Column(db.DateTime, nullable=True)
    category_id =db.Column(db.Integer,db.ForeignKey('categories.id'), nullable=False, default = 1)

    #Metodo que formatee el objeto a json para devolverlo a mi API y que no de errores
    def format(self):
        return {
            'id':self.id,
            'author':self.author,
            'title':self.title,
            'body':self.body,
            'created':self.created,
            'modificated':self.modificated,
            'category_id':self.category_id
        }

    #Metodo que permite la inserción de un post a través de nuestra API
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50))
    password = db.Column(db.Text)

    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
    
    def __repr__(self) -> str:
        return f'User: {self.username}'

    #Metodos para la API:

    def format(self):
        return {
            'id':self.id,
            'username':self.username
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()