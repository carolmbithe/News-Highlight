
from flask import render_template
from . import main
from ..request import get_sources,get_articles

# from ..models import Article



@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """

    newsSource=get_sources()
    title = 'News Sources-catchup on whats latest'
    print(newsSource)
    return render_template('index.html',title=title,sources=newsSource)

@main.route('/articles/<string:id>')
def source(id):
    """
    View source page function that returns the  sources and their details
    """
    articles= get_articles(id)
    print(articles)
    return render_template('articles.html',articles=articles)
