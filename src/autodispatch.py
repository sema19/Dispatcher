'''
Created on Dec 8, 2019

@author: sedlmeier
'''

from models.baseModel import db_session
from models.servicedemand import ServiceDemand
from models.serviceprovider import ServiceProvider
from models.unavailability import Unavailability
import numpy as np   

def autodispatch(activity_id, services_to_skip):
        
    # find service demands
    db = db_session()
    qServiceDemands = db.query(ServiceDemand).filter(ServiceDemand.activity_id==activity_id).all()
    db.close()
    if qServiceDemands == None:
        return
    for serviceDemand in qServiceDemands:        
        dispatch_service(serviceDemand,activity)        
        
            
    # find service providers
    
    
    # filter availabe service providers
    # dispatch by existing relations
    # dispatch by service provation times
    # correct for service combinations
    # correct for relations
    
    db.commit()
    
    pass

def dispatch_service(serviceDemand,activity):
    
    db = db_session()
    qServiceProviders = db.query(ServiceProvider).filter(ServiceProvider.service_id == serviceDemand.service_id).all()    
    db.close()
    v = np.array([])
    v = availability(v,qServiceProviders,activity)
    
    
    
    
    
    
    
    
    
def availableServiceProviders(v,serviceProviders, activity):
    avail=[]
    db = db_session()
    for serviceProvider in serviceProviders:
        qServiceProviders = db.query(Unavailability).filter(Unavailability.person_id == serviceProvider.person_id,Unavailability.end < activity.start, Unavailability.start > activity.end).all()
        if qServiceProviders==None:
            continue
        if len(qServiceProviders)>0:
            continue;
        avail.append(serviceProvider)            
    db.close()
    return avail;
    
    
    
    
    
    
    
    
    
    
    
    
