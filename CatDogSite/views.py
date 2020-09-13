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


@app.route('/contact-us.html')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact-us.html',
        title='Pets',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/events.html')
def events():
    return render_template(
        'events.html',
        title='Event',
        message='Page with upcoming events'
        )

@app.route('/about-us.html')
def about():
    """Renders the about page."""
    return render_template(
        'about-us.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
