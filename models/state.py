#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    def __init__(self, *args, **kwargs):
        """Initializes a new state"""
        super().__init__(*args, **kwargs)
    name = ""
