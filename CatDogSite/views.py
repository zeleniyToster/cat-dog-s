"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from CatDogSite import app

@app.route('/')
@app.route('/index.html')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home',
        year=datetime.now().year,
    )

@app.route('/index-2.html')
def Home2():
    return render_template(
        'index-2.html',
        title='Home 2'
        )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact-us.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about-us.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
