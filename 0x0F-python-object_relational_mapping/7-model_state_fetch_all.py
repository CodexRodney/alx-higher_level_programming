#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_)e_6_usa
"""


from model_state import Base, State
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))
DBSession = sessionmaker(bind=engine)
session = DBSession()
results = session.query(State).order_by(State.id).all()
for i in results:
    print(i.id, ": ", i.name)
