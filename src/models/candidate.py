'''
Created on Jan 17, 2020

@author: sedlmeier
'''

class Candidate(object):
    '''
    classdocs
    '''
    def __init__(self,serviceProvider,serviceDemand):
        self.serviceProvider_id = serviceProvider.id
        self.person_id = serviceProvider.person_id
        self.serviceDemand=serviceDemand
        self.availability=0
        self.dutyWindow=0
        self.dutyConflict=0
        self.reationTo=0
        self.relationFrom=0
        self.reatedTo=[]
        self.relatedFrom=[]
        
        
    def setAvailable(self,points):
        self.availability=points
        
    def dump(self):
        return dict([(k,v) for k,v in vars(self).items() if not k.startswith('_')])