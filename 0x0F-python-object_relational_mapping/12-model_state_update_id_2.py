#!/usr/bin/python3
"""
Changes name of a State objects from the database hbtn_0e_6_usa
"""


from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    str1 = 'mysql://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3])
    engine = create_engine(str1)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    results = session.query(State).get(2)
    results.name = "New Mexico"
    session.commit()
