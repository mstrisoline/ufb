#Application Database Models and Funcations
#Most of these should be self explanitory

from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import *
import pbkdf2

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,index=True, primary_key=True)
    first = db.Column(db.String(32), nullable=False)
    last = db.Column(db.String(32), nullable=False)
    #Required field for Route Decorators
    nickname = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    salt = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime, server_default=text('NOW()'), nullable=False)
    #One to many relationship with Posts made by user
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    #Flask Login User Class Required Methods
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return "<User %r>" % (self.email)

    #Password Methods
    def gen_salt(self):
        self.salt =  pbkdf2.SHA1().hexdigest()

    def hash_pw(self, pw):
        return pbkdf2.crypt(pw, salt=self.salt)

    def set_pw(self, pw):
        self.password = self.hash_pw(pw)

    def validate_pw(self, pw):
        new_hash = self.hash_pw(pw)
        return pbkdf2.HMAC.compare_digest(new_hash, self.password)
        
class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer,index=True, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=text('NOW()'), nullable=False)
    body = db.Column(db.String(256))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    #One to many relationship with Replies to a Post
    replies = db.relationship('Reply', backref='reply', lazy='dynamic')

    def __repr__(self):
        return "<Post %r>" % (self.id)

class Reply(db.Model):
    __tablename__ = 'replies'

    id = db.Column(db.Integer,index=True, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=text('NOW()'), nullable=False)
    body = db.Column(db.String(256))
    #Link Reply back to a user
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    #Link Reply back to a post
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    
    #Return the Author's First and Last for a Reply
    def author(self):
        a = User.query.get(self.user_id)
        return "%s %s" % (a.first, a.last)

    def __repr__(self):
        return "<Post %r>" % (self.id)
