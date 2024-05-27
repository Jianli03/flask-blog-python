from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    creation_time = db.Column(db.DateTime, nullable=False, default=lambda:datetime.datetime.now(tz=datetime.timezone.utc))
