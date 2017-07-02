from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	email = Column(String(250), nullable=False)
	picture = Column(String(250))
	password_hash = Column(String(250))

	@property
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
		   'id'   : self.id,
		   'email' : self.email,
		   'picture' : self.picture
	   }


class Request(Base):
	__tablename__ = 'request'

	id = Column(Integer, primary_key=True)
	meal_time = Column(String(250))
	latitude = Column(String(250))
	longitude = Column(String(250))
	location_string = Column(String(250))
	filled = Column(Boolean)
	user_id = Column(Integer,ForeignKey('user.id'))
	user = relationship(User) 

	@property
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
		   'id'   : self.id,
		   'meal_time' : self.meal_time,
		   'latitude' : self.latitude,
		   'longitude' : self.longitude,
		   'location_string' : self.location_string,
		   'filled' : self.filled,
		   'user_id' : self.user_id
	   }

class Proposal(Base):
	__tablename__ = 'proposal'

	id = Column(Integer, primary_key=True)
	user_proposed_to = Column(Integer)
	user_proposed_from = Column(Integer)
	filled = Column(Boolean)
	request_id = Column(Integer,ForeignKey('request.id'))
	request = relationship(Request)
	
	@property
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
		   'id' : self.id,
		   'user_proposed_to' : self.user_proposed_to,
		   'user_proposed_from' : self.user_proposed_from,
		   'filled' : self.filled,
		   'request_id' : self.request_id
	   }

class MealDate(Base):
	__tablename__ = 'meal_date'

	id = Column(Integer, primary_key=True)
	user_1 = Column(Integer)
	user_2 = Column(Integer)
	restaurant_name = Column(String(250))
	restaurant_address = Column(String(250))
	restaurant_picture = Column(String(250))
	meal_time = Column(String(250))
	
	@property
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
		   'id' : self.id,
		   'user_1' : self.user_2,
		   'user_2' : self.user_2,
		   'restaurant_name' : self.restaurant_name,
		   'restaurant_address' : self.restaurant_address,
		   'restaurant_picture' : self.restaurant_picture,
	   }




engine = create_engine('sqlite:///meetngreet.db')
 

Base.metadata.create_all(engine)

