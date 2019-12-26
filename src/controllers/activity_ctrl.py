'''
Created on Dec 22, 2019

@author: sedlmeier
'''

from datetime import datetime

from connexion import NoContent
import requests

from models.activity import Activity
from controllers import crud_base
from models.baseModel import db_session


def get(limit=None):
    return crud_base.get(Activity, limit)
    
def post(odata=None):
    return crud_base.post(Activity, odata)
    
def get_id(oid):
    return crud_base.get_id(Activity,oid)

def put(oid,odata):
    return crud_base.put(Activity,oid,odata)

def put_uid(uid,odata):
    return crud_base.put(Activity,uid,odata,"uid")

def delete(oid):
    return crud_base.delete(Activity,oid)


