from flask import Flask
from .db_models import db

def create_app():
    '''Create and configure an instance of the Flask application'''
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tweet_repo.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    @app.route('/')
    def root():
        return 'Welcome to Twitoff!'
    return app