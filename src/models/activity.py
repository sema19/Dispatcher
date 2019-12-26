'''
Created on 07.10.2019

@author: markus.sedlmeier
'''
from datetime import datetime
from datetime import timedelta
import uuid

from sqlalchemy import Column, String, Integer, DateTime, Boolean

from models.baseModel import DbBase

    
class Activity(DbBase):
    __tablename__ = 'activities'
    id          = Column(Integer, primary_key=True)
    start       = Column(DateTime)
    end         = Column(DateTime)    
    info        = Column(String)
    
    
    def __init__(self, start=None, end=None, info=None):        
        self.start = datetime.strptime(start, "%Y-%m-%dT%H:%M:%S.%fZ")
        self.end = datetime.strptime(end, "%Y-%m-%dT%H:%M:%S.%fZ")        
        self.info=info
        