'''
Created on Dec 8, 2019

@author: sedlmeier
'''


from datetime import datetime
from datetime import timedelta
import uuid

from sqlalchemy import Column, String, Integer, DateTime, Boolean
from sqlalchemy.schema import ForeignKey

from models.baseModel import DbBase

    
class relation(DbBase):
    __tablename__ = 'relation'
    id          = Column(Integer, primary_key=True)
    person_a_id = Column(Integer, ForeignKey("person"))    
    person_b_id = Column(Integer, ForeignKey("person"))
    weight      = Column(Integer)           # weight of the relation, e.g. father-son 1, person - passed away person = 5, friend 1 - friend b=7
    
    def __init__(self, person_a_id=None, person_b_id=None, weight=None):        
        self.person_a_id = person_a_id
        self.person_b_id = person_b_id
        self.weight=weight