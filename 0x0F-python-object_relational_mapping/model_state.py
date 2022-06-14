#!/usr/bin/python3
"""
Defines the class State
"""


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# engine = create_engine('mysql://root@localhost:3306')
Base = declarative_base()


class State(Base):
    __tablename__ = "states"
    id = Column(Integer, primary_key = True)
    name = Column(String(128), nullable = False)
