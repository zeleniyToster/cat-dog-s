"""
This script runs the CatDogSite application using a development server.
"""
import os
from os import environ
from CatDogSite import app

if __name__ == '__main__':
    #HOST = environ.get('SERVER_HOST', 'localhost')
    #try:
    #    PORT = int(environ.get('SERVER_PORT', '5555'))
    #except ValueError:
    #    PORT = 5555
    port = int(os.environ.get('PORT', 33507))
    app.run(host='0.0.0.0', port=port)