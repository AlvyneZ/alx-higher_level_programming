#!/usr/bin/python3
"""
This module provides a class State which is an ORM model
"""
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    This model class links to the MySQL table "states"
    Attributes:
        id(int): identifier of state
        name(string): name of state
    """
    __tablename__ = "states"
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(128), nullable=False)
    cities = relationship(
        "City",
        backref="state",
        cascade="all, delete"
    )
