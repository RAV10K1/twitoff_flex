from flask import Flask, render_template
from .db_models import db, User

def create_app():
    '''Create and configure an instance of the Flask application'''
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tweet_repo.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    
    @app.route('/')
    def root():
        return render_template('base.html', title="Home", users=User.query.all())
    return app