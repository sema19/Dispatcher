'''
Created on Dec 8, 2019

@author: sedlmeier
'''
from datetime import datetime
from datetime import timedelta
import uuid

from sqlalchemy import Column, String, Integer, DateTime, Boolean
from models.baseModel import DbBase

    
class service(DbBase):
    __tablename__ = 'services'
    id      = Column(Integer, primary_key=True)
    text    = Column(String)    
        
    def __init__(self, text=None):         
        self.text = text