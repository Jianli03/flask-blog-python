from flask import Flask, render_template
from article_data import articles

app = Flask(__name__)

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

if __name__ == '__main__':
  app.run(debug=True)


