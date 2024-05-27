from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from article_data import articles

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def show_articles():
    return render_template('articles.html', articles=articles)

@app.route('/article/<title>/')
def display_article_title(title):
    global articles
    # Find the article with the given article_id
    article = [a for a in articles if a["title"] == title]
    if not article:
         return "No article with the title '{}' was found.".format(title), 404  # Return 404 Not Found with a custom error message
    return render_template('article.html', article=article[0])


@app.route('/create')
def create():
    return render_template('create_article.html')


@app.route('/create_post', methods=['POST'])
def create_post():
    try:
        # Get the article data from the form
        article_data = {
        'id': request.form.get('id'),
        'title': request.form.get('title'),
        'content': request.form.get('content')
        }

        # Create a new Article object and add it to the session
        db_article = db.Table('Article')(id=article_data['id'], title=article_data['title'], content=article_data['content'])
        db.session.add(db_article)
        db.session.commit()

        # Return a response to the user
        return render_template('result.html')

    except Exception as e:
          # Return a response to the user with an error message
        message = f"An error occurred while creating the article: {str(e)}"
        return render_template('error.html', message=message)

    finally:
        db.session.close()

if __name__ == '__main__':
  app.run(debug=True)



