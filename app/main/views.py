
from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_source

# from ..models import Article



@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """

    news_source=get_sources()
    title = 'News Sources-catchup on whats latest'
    heading='WELCOME TO NEWSHIGHLIGHT'
    return render_template('index.html',heading=heading,title=title,sources=news_source)

# @main.route('/source/')
# def source():
#     """
#     View source page function that returns the  sources and their details
#     """
#     source= get_source()
#     title = f'{source.name}'
#     return render_template('source.html',title = title,source=source)
