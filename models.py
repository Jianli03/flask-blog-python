from datetime import datetime
from flask import g

# Access the SQLAlchemy instance from the application context
db = g.db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    creation_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
