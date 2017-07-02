from flask import Flask, jsonify, request
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from models import User, Request, Proposal, MealDate
from passlib.apps import custom_app_context as pwd_context
from flask_httpauth import HTTPBasicAuth

engine = create_engine('sqlite:///restaruants.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)

@app.route('api/v1/users',methods= ['GET', 'POST','PUT'])
def all_users_handler():
	if request.method == 'GET':
		users = session.query(User).all()
		return jsonify(users = [i.serialize for i in users])
    elif request.method == 'POST':
    	email = request.args.get('email')
    	picture = request.args.get('picture')


@app.route('api/v1/users/<int:id>', methods = ['GET'])
def user_handler(id):

@app.route('api/v1/requests', methods = ['GET', 'POST'])
def all_requests_handler:

@app.route('api/v1/requests/<int:id>', methods = ['GET','PUT' , 'DELETE'])
def request_handler(id):

@app.route('api/v1/proposals', methods = ['GET', 'POST'])
def all_proposals_handler():

@app.route('api/v1/proposals/<int:id>', methods = ['GET', 'PUT' , 'DELETE'])
def proposal_handler(id):

@app.route('api/v1/dates', methods = ['GET', 'POST'])
def all_dates_handler():

@app.route('api/v1/dates/<int:id>', methods = ['GET', 'PUT' , 'DELETE'])
def date_handler(id):

def hash_password(self, password):
    self.password_hash = pwd_context.encrypt(password)

def verify_password(self, password):
    return pwd_context.verify(password, self.password_hash)

def new_user():
    email = request.json.get('email')
    password = request.json.get('password')
    if email is None or password is None:
        abort(400) # missing arguments
    if session.query(User).filter_by(email = email).first() is not None:
        abort(400) # existing user
    user = User(email = email)
    user.hash_password(password)
    session.add(user)
    session.commit()
    return jsonify({ 'email': user.email }), 201

if __name__ == '__main__':
    app.debug = True
    app.run()	


	