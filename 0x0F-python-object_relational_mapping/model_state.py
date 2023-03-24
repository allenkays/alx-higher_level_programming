#!/usr/bin/env python3
"""
File containing class definition of a given state and an instance
"""

from sqlalchemy import Column, Interger, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Interger, Primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
