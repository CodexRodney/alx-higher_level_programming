#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""


from model_city import City
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    str1 = 'mysql://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3])
    engine = create_engine(str1)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    results = session.query(City).order_by(City.id).all()
    for i in results:
        print("{}: ({}) {}".format(i.states.name, i.id, i.name))
