# columns and their types, including fk relationships
from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

# declarative base 
from sqlalchemy.ext.declarative import declarative_base

# create the base class (declarative base)
# call it Base!
Base = declarative_base()

# implement the following three classes...

# class Scooter(Base):

# class ScooterType(Base):

# class Company(Base):
