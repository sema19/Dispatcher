'''
Created on 03.01.2020

@author: markus.sedlmeier
'''

from models.baseModel import db_session
from connexion import NoContent


def get(CrudObj, limit=None):
    if (limit==None):
        limit=100
    curr_session=db_session()
    q = curr_session.query(CrudObj)    
    return [p.dump() for p in q][:limit]

def get_by_id(CrudObj, oid, oid_ref="id"):
    curr_session=db_session()
    q = curr_session.query(CrudObj).filter(CrudObj.getattr(CrudObj,oid_ref) == oid).one_or_none()
    if q==None:
        return NoContent, 404
    return q.dump()


def post(CrudObj, odata):
    curr_session=db_session()     
    tobj = CrudObj(**odata)
    curr_session.add(tobj)
    curr_session.commit()
    if tobj==None:
        return NoContent, 404
    return tobj.dump(), 201


def put(CrudObj, oid, odata, oid_ref="id"):
    curr_session=db_session()
    p = curr_session.query(CrudObj).filter(getattr(CrudObj,oid_ref) == oid).one_or_none()    
    if p is not None:        
        if (p.update(**odata)):
            curr_session.commit()
    else:        
        return NoContent, 404
    return p.dump(), 200


def delete(CrudObj, oid, oid_ref="id"):
    curr_session=db_session()
    delobject = curr_session.query(CrudObj).filter(getattr(CrudObj,oid_ref) == oid).one_or_none()
    if delobject is not None:        
        curr_session.query(CrudObj).filter(getattr(CrudObj,oid_ref) == oid).delete()
        curr_session.commit()
        return NoContent, 204
    else:
        return NoContent, 404



