'''
Created on Dec 8, 2019

@author: sedlmeier
'''

from sqlalchemy import Column, Integer, DateTime, Boolean
from sqlalchemy.schema import ForeignKey
from datetime import datetime

from models.baseModel import DbBase

    
class ServiceProvider(DbBase):
    __tablename__ = 'serviceproviders'
    id          = Column(Integer, primary_key=True)
    person_id   = Column(Integer, ForeignKey("persons.id"))    
    service_id = Column(Integer, ForeignKey("services.id"))    
    started     = Column(DateTime)
    active      = Column(Boolean)
    
    def __init__(self, person_id=None, service_id=None, started=None, active=True):        
        self.person_id = person_id 
        self.service_id = service_id
        self.started = datetime.strptime(started, "%Y-%m-%dT%H:%M:%S.%fZ")
        self.active = active