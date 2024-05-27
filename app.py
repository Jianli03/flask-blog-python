from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_paginate import get_page_parameter, Pagination
from models import db, Article

app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PAGINATION_ENABLED'] = True
app.config['PAGINATION_DEFAULT_PER_PAGE'] = 10
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db.init_app(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def show_articles():
    page = get_page_parameter()

    # Fetch articles from the database with pagination
    articles = Article.query.paginate()
    return render_template('articles.html', articles=articles)


@app.route('/article/<int:article_id>/')
def display_article(article_id):
    article = Article.query.get(article_id)
    if not article:
        return "No article with the ID '{}' was found.".format(article_id), 404
    return render_template('article.html', article=article)

@app.route('/create')
def create():
    return render_template('create_article.html')


@app.route('/create_post', methods=['POST'])
def create_post():
    try:
        # Get the article data from the form
        article_data = {
        'author': request.form.get('author'),
        'title': request.form.get('title'),
        'content': request.form.get('content')
        }

        # Create a new Article object and add it to the session
        db_article = Article(author=article_data['author'],
            title=article_data['title'],
            content=article_data['content'])
        db.session.add(db_article)
        db.session.commit()
        print("Done")
        # Return a response to the user
        return render_template('result.html')

    except Exception as e:
          # Return a response to the user with an error message
        message = f"An error occurred while creating the article: {str(e)}"
        return render_template('error.html', message=message)



if __name__ == '__main__':
    with app.app_context():
        #db.drop_all()
        db.create_all()
    app.run(debug=True)



