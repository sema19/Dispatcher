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

    
class dispatch(DbBase):
    __tablename__ = 'dispatch'
    id          = Column(Integer, primary_key=True)
    person_id   = Column(Integer, ForeignKey("persons.id"))    
    activity_id = Column(Integer, ForeignKey("activity.id"))
    service_id = Column(Integer, ForeignKey("services.id"))
    demand_id   = Column(Integer, ForeignKey("servicedemands.id"))
    status      = Column(String(50))        # CREATED, QAPASSED, CONFIRMED, DECLINED    
       
        
    def __init__(self, person_id=None, activity_id=None, service_id=None, demand_id=None, status=None):        
        self.person_id = person_id 
        self.activity_id = activity_id
        self.service_id = service_id
        self.demand_id = demand_id
        status = status

        
    
        

        