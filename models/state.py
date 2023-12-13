#!/usr/bin/python3
"""class State that inherits from BaseModel"""


from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from os import getenv
from models.city import City
import shlex


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="all, delete", backref="state",
                              passive_deletes=True)
    else:

        @property
        def cities(self):
            """Return the list of City instances with state_id
            equals to the current State.id"""
            from models import storage
            state_cities = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    state_cities.append(city)
            return state_cities
