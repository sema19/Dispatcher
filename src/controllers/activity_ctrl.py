'''
Created on Dec 22, 2019

@author: sedlmeier
'''

from models.activity import Activity
from controllers import crud_base


def get(limit=None):
    return crud_base.get(Activity, limit)
    
def post(odata=None):
    return crud_base.post(Activity, odata)

def put(oid,odata):
    return crud_base.put(Activity,oid,odata)

def delete(oid):
    return crud_base.delete(Activity,oid)


