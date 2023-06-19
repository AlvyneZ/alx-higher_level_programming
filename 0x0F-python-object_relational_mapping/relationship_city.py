#!/usr/bin/python3
"""
This module provides a class City which is an ORM model
"""
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from relationship_state import Base, State


class City(Base):
    """
    This model class links to the MySQL table "cities"
    Attributes:
        id(int): identifier of city
        name(string): name of city
        state_id(int): state the city belongs to
    """
    __tablename__ = "cities"
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(128), nullable=False)
    state_id = mapped_column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")
