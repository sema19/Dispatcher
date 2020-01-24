'''
Created on Dec 22, 2019

@author: sedlmeier
'''


from models.unavailability import Unavailability
from controllers import crud_base


def get(limit=None):
    return crud_base.get(Unavailability, limit)
    
def post(odata=None):
    return crud_base.post(Unavailability, odata)
    
def put(oid,odata):
    return crud_base.put(Unavailability,oid,odata)

def delete(oid):
    return crud_base.delete(Unavailability,oid)