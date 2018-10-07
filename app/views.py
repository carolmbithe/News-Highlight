from flask import render_template
from app import app
from .request import get_newssource,get_source

@app.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """

    news_source=get_newssource()
    title = 'News Sources-catchup on whats latest'
    heading='WELCOME TO NEWSHIGHLIGHT'
    return render_template('index.html',heading=heading,title=title,sources=news_source)

@app.route('/source')
def source():
    """
    View movie page function that returns the  sources and their details
    """
    source= get_source(name)
    title = f'{newssource.name}'
    return render_template('source.html',title = title,source=source)
