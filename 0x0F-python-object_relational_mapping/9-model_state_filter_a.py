#!/usr/bin/python3
"""
This script lists all State objects from the states table from a MySQL DB
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Accessing and listing states from database
    """
    n = len(argv)
    if n != 4:
        print(
            "Usage: {} mysql_username ".format(argv[0]) +
            "mysql_password database_name"
        )
    else:
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                argv[1], argv[2], argv[3]
            ),
            pool_pre_ping=True
        )
        Session = sessionmaker(bind=engine)
        session = Session()

        for instance in session.query(State)\
                .filter(State.name.contains('a'))\
                .order_by(State.id):
            print('{}: {}'.format(instance.id, instance.name))
