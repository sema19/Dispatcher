'''
Created on Dec 8, 2019

@author: sedlmeier
'''

from datetime import datetime
from datetime import timedelta

from sqlalchemy import Column, String, Integer, DateTime, Boolean
from sqlalchemy.schema import ForeignKey

from models.baseModel import DbBase

    
class ServiceDemand(DbBase):
    __tablename__ = 'servicedemands'
    id          = Column(Integer, primary_key=True)
    activity_id   = Column(Integer, ForeignKey("activities.id"))    
    service_id = Column(Integer, ForeignKey("service.id"))
    min_cnt     = Column(Integer)
    cnt         = Column(Integer)
    max_cnt     = Column(Integer)
    expirence   = Column(Integer)
        
    def __init__(self, activity_id=None, service_id=None, min_cnt=1, cnt=1, max_cnt=1, experience=0):        
        self.activity_id = activity_id 
        self.service_id = service_id
        self.min_cnt = min_cnt
        self.cnt=cnt
        self.max_cnt = max_cnt
        experience=experience