from flask import Flask, render_template, redirect, url_for, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
#from config import db, application
#from models import Users
#import json 
 

application = Flask(__name__)

@application.route('/')
def hello():
    return 'hello world'

if __name__ == '__main__':
    application.debug = True
    application.run()  