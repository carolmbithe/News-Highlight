from flask import render_template
from app import app

@app.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """

    title = 'Newsources-catchup on whats latest'
    heading='WELCOME TO NEWSHIGHLIGHT'
    return render_template('index.html',heading=heading,title=title)

@app.route('/newssource/<int:newssource_id>')
def newssource(newssource_id):
    """
    View movie page function that returns the news sources and their details
    """
    return render_template('newssource.html',id = newssource_id)
