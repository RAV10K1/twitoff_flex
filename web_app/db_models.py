'''SQLAlchemy models for Twitoff'''

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from sqlalchemy.sql.schema import ForeignKey

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    follower_count = db.Column(db.String(120), unique=True, nullable=False)
    newest_tweet_id = db.Column(db.BigInteger, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Unicode(300))
    embedding = db.Column(db.PickleType, nullable=False)
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'), nullable=False)
    # user = db.Relationship('User', backref=db.backref('text', lazy=True))
    
    def __repr__(self):
        return '<User %r>' % self.text  
 