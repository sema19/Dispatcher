'''
Created on Dec 8, 2019

@author: sedlmeier
'''

from datetime import datetime
from datetime import timedelta
import uuid

from sqlalchemy import Column, String, Integer
from models.baseModel import DbBase

    
class Person(DbBase):
    __tablename__ = 'persons'
    id          = Column(Integer, primary_key=True)
    info        = Column(String)
        
    def __init__(self, info=None):
        self.info=info        
        
    
        