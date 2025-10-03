from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    genre = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    image = db.Column(db.String(150), nullable=False, default='default.png')

    def __init__(self, nom, prenom, username, email, genre, password):
        self.nom = nom
        self.prenom = prenom
        self.username = username
        self.email = email
        self.genre = genre
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)