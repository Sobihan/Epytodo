from app import app
from flask import jsonify
from app import app
from  flask  import  render_template, request
from app import models
from app import controller
import pymysql as sql

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def route_home ():
    return  render_template("index.html")

@app.route('/user/<username>', methods =['GET'])
def route_user(username):
    return  render_template("index.html",
                            title="Hello " + username ,
                            myContent="My SUPER  content  for " + username + "!!!")

@app.route('/login', methods=['GET'])
def route_login ():
    return  render_template("login.html")

@app.route('/register', methods=['POST', 'GET'])
def route_register ():
    return  render_template("register.html")