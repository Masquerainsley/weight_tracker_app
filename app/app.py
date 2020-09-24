from flask import Flask, render_template, redirect, url_for, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
#from config import db, app
#from models import Users
#import json 
 

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def hello():
    return 'hello world'

if __name__ == '__main__':
    app.run()    