#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
which contain the letter a
"""


from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


str1 = 'mysql://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3])
engine = create_engine(str1)
DBSession = sessionmaker(bind=engine)
session = DBSession()
results = session.query(State).filter(State.name.like('%a%')).all()
for i in results:
    print("{}: {}".format(i.id, i.name))
