'''
Created on Dec 22, 2019

@author: sedlmeier
'''
from datetime import datetime

from connexion import NoContent
import requests

from models.unavailability import Unavailability
from controllers import crud_base
from models.baseModel import db_session


def get(limit=None):
    return crud_base.get(Unavailability, limit)
    
def post(odata=None):
    return crud_base.post(Unavailability, odata)
    
def get_id(oid):
    return crud_base.get_id(Unavailability,oid)

def put(oid,odata):
    return crud_base.put(Unavailability,oid,odata)

def put_uid(uid,odata):
    return crud_base.put(Unavailability,uid,odata,"uid")

def delete(oid):
    return crud_base.delete(Unavailability,oid)