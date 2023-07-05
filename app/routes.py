from flask import Blueprint, request, jsonify
from . import db
from .models import Post
from .nlp import get_sentiment
from flask_cors import cross_origin

bp = Blueprint('app', __name__)

@bp.route('/')
def index():
    return "Hello, World!"

@bp.route('/api/posts', methods=['POST'])
@cross_origin(origins="*", methods=["GET", "POST"])
def post():
    if request.is_json:
        content = request.json['content']
        sentiment_score = get_sentiment(content)
        new_post = Post(content=content, sentiment_score=sentiment_score)
        db.session.add(new_post)
        db.session.commit()
        return jsonify(message="Post created"), 201
    else:
        return jsonify(message="Request must be JSON"), 400

@bp.route('/api/posts', methods=['GET'])
@cross_origin(origins="*", methods=["GET", "POST"])
def get_posts():
    posts = Post.query.all()
    return jsonify([{
        'id': post.id,
        'content': post.content,
        'sentiment_score': post.sentiment_score
    } for post in posts])
