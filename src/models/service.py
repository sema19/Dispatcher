'''
Created on Dec 8, 2019

@author: sedlmeier
'''

from sqlalchemy import Column, String, Integer
from models.baseModel import DbBase

    
class Service(DbBase):
    __tablename__ = 'services'
    id      = Column(Integer, primary_key=True)
    text    = Column(String)    
        
    def __init__(self, text=None):         
        self.text = text