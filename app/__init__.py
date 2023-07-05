import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

# 現在のファイルのディレクトリを取得
basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'app.db')}"
    db.init_app(app)
    Migrate(app, db)

    with app.app_context():
        db.create_all()

    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app
