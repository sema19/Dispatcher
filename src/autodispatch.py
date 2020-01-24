'''
Created on Dec 8, 2019

@author: sedlmeier
'''

from datetime import timedelta
from models import baseModel
from models.servicedemand import ServiceDemand
from models.serviceprovider import ServiceProvider
from models.activity import Activity
from models.unavailability import Unavailability
from models.dispatch import Dispatch
from models.relation import Relation
from models.candidate import Candidate
        

def autodispatch(activity_id, services_to_skip=[]):
        
    # find service demands
    db = baseModel.db_session()
    qServiceDemands = db.query(ServiceDemand).filter(ServiceDemand.activity_id==activity_id).all()
    #activity = db.query(Activity).filter(Activity.id == activity_id).one_or_none()
    db.close()
    if qServiceDemands == None:
        return
    for serviceDemand in qServiceDemands:                
        dispatch_service(serviceDemand)        
        
            
    # find service providers
    
    
    # filter availabe service providers
    # dispatch by existing relations
    # dispatch by service provation times
    # correct for service combinations
    # correct for relations
    
    db.commit()
    
    

def dispatch_service(serviceDemand):
    
    candidates = get_candidates(serviceDemand)    
    availability(candidates)
    duty(candidates)
    relations(candidates)
    
def get_candidates(serviceDemand):
    candidates = []
    db = baseModel.db_session()
    qServiceProviders = db.query(ServiceProvider).filter(ServiceProvider.service_id == serviceDemand.service_id).all()    
    db.close()
    for serviceProvider in qServiceProviders:
        candidates.append(Candidate(serviceProvider,serviceDemand))
    return candidates
    
def availability(candidates):
    db = baseModel.db_session()
    for candidate in candidates:
        unavailableList = db.query(Unavailability).filter(Unavailability.person_id == candidate.person_id,Unavailability.end < candidate.activity.start, Unavailability.start > candidate.activity.end).all()
        if unavailableList==None:
            continue
        if len(unavailableList)>0:
            continue;
        candidate.setAvailable(100)            
    db.close()
    

def duty(candidates,dutyCountSpanInDays=100, dutyWindowSpanInDays=5):
    """
    
    """    
    db = baseModel.db_session()    
    for candidate in candidates:
        start=candidate.activity.start-timedelta(days=dutyCountSpanInDays)
        end=candidate.activity.end+timedelta(days=dutyCountSpanInDays)
                
        dutyList = db.query(Dispatch).filter(Dispatch.person_id == candidate.person_id,Dispatch.status=="CREATED").join(Activity).filter(Activity.start > start, Activity.end<end).all()
        if dutyList==None:
            continue
        dutyWindowStart = candidate.activity.start-timedelta(days=dutyWindowSpanInDays)
        dutyWindowEnd = candidate.activity.end+timedelta(days=dutyWindowSpanInDays)
        
        dutyCnt=0
        dutyWindow=0
        for duty in dutyList:
            # before the duty window and activity, just iterate the duties fullfilled or assigned
            if duty.Activity.start < dutyWindowStart:
                dutyCnt+=1
            # after the duty window and activity, just iterate the duties fullfilled or assigned
            elif duty.Activity.end > dutyWindowEnd:
                dutyCnt+=1
            # duties within the duty window and before the activity (others are handled above already), set the duty window value and iterate the duty count 
            elif duty.Activity.start < candidate.activity.start:                
                deltaTimeInHours = (candidate.activity.start - duty.Activity.start()).hours()
                dutyWindow+=dutyWindowValue(deltaTimeInHours,dutyWindowSpanInDays*24)
                dutyCnt+=1
            # duties within the duty window and after the activity (others are handled above already), set the duty window value and iterate the duty count
            elif duty.Activity.end > candidate.activity.end:
                deltaTimeInHours = (duty.Activity.end - candidate.activity.end)
                dutyWindow+=dutyWindowValue(deltaTimeInHours,dutyWindowSpanInDays*24)
                dutyCnt+=1                
            else:
                candidate.dutyConflict+=100                
        candidate.dutyWindow=dutyWindow
        candidate.dutyCount=dutyCnt            
    db.close()
    
def dutyWindowValue(deltaH,maxH):
    dn=100*(maxH-deltaH)/maxH
    #TODO: add logarithmic function to have a higher points on duties closer to the target date
    return dn

def relations(candidates):
    db = baseModel.db_session()
    for candidate in candidates:
        # find relations
        relationsTo = db.query(Relation).filter(Relation.person_a_id == candidate.person_id).all()
        relationsFrom = db.query(Relation).filter(Relation.person_b_id == candidate.person_id).all()
        if relationsTo==None:
            continue
        for relation in relationsTo:
            candidate.reationTo+=relation.weight
            candidate.reatedTo.append(relation)
        for relation in relationsFrom:
            candidate.reationTo+=relation.weight
            candidate.reatedTo.append(relation)            
            
        
        
       
    
    
    
    
    
    
    
    
