from . import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    sentiment_score = db.Column(db.Float, nullable=False)
