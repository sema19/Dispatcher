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

    
class servicecombination(DbBase):
    __tablename__ = 'servicecombinations'
    id      = Column(Integer, primary_key=True)
    service_a_id=Column(Integer, ForeignKey("services.id"))
    service_b_id=Column(Integer, ForeignKey("services.id"))
    combination_level   = Column(Integer)                       # +100 should be combined , 0=not correlated, -100 not able to combine
        
    def __init__(self, service_a_id=None, service_b_id=None, combination_level=0):         
        self.service_a_id = service_a_id
        self.service_b_id = service_b_id
        self.combination_level = combination_level