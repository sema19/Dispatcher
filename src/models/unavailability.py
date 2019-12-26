'''
Created on Dec 8, 2019

@author: sedlmeier
'''

from datetime import datetime
from datetime import timedelta

from sqlalchemy import Column, Integer, DateTime, Boolean
from sqlalchemy.schema import ForeignKey

from models.baseModel import DbBase

    
class Unavailability(DbBase):
    __tablename__ = 'unavailability'
    id          = Column(Integer, primary_key=True)    
    person_id   = Column(Integer, ForeignKey("persons.id"))
    fadein      = Column(DateTime) 
    start       = Column(DateTime)
    end         = Column(DateTime)
    fadeout     = Column(DateTime)
    
    def __init__(self, person_id=None, start=None, end=None, fadein=None, fadeout=None):        
        self.person_id=person_id
        self.fadein= datetime.strptime(fadein, "%Y-%m-%dT%H:%M:%S.%fZ") if fadein!=None else datetime.strptime(start-timedelta(hour=1), "%Y-%m-%dT%H:%M:%S.%fZ")
        self.start = datetime.strptime(start, "%Y-%m-%dT%H:%M:%S.%fZ")
        self.end = datetime.strptime(end, "%Y-%m-%dT%H:%M:%S.%fZ")
        self.fadeout=datetime.strptime(fadein, "%Y-%m-%dT%H:%M:%S.%fZ") if fadein!=None else datetime.strptime(end+timedelta(hour=1), "%Y-%m-%dT%H:%M:%S.%fZ")
        
        
    