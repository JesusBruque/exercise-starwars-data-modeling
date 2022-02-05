import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(20), nullable=False)
    nickname = Column(String(100))

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))
    height = Column(Integer)
    skin_color = Column(String(250))
    eye_color = Column(String(250))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    climate = Column(String(250))

class UserFavourite(Base):
    __tablename__ = 'user_favourite'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    id_character = Column(Integer, ForeignKey('character.id'))
    id_planet = Column(Integer, ForeignKey('planet.id'))
    relationship(User)
    relationship(Character)
    relationship(Planet)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')