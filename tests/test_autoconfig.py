'''
Created on Jan 5, 2020

@author: sedlmeier
'''
import unittest
import autodispatch
from models.baseModel import db_session
from models.activity import Activity
from models.person import Person
from models.serviceprovider import ServiceProvider
from models.servicedemand import ServiceDemand
from models.service import Service
from test_app import BaseTestCase
from models import baseModel


from datetime import datetime
from datetime import timedelta

from pprint import pprint

class Test(BaseTestCase):


    def setUp(self):        
        pass

    def create_basic_activity(self):
        db = baseModel.db_session()
        db.query(Activity).delete()
        
        tstart=datetime.now()+timedelta(hours=10)
        tend=tstart+timedelta(minutes=45)
        info="Test Church"        
        a = Activity(start=tstart.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), end=tend.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), info=info)
        
        db.add(a)        
        db.commit()
        
    def create_basic_services(self):
        db=baseModel.db_session()
        db.query(Service).delete()
        p=Service(text="Ministrant")
        db.add(p)
        p=Service(text="Kommunionhelfer")
        db.add(p)
        p=Service(text="Leser")
        db.add(p)
        p=Service(text="Fuerbitten")
        db.add(p)
        p=Service(text="Messner")
        db.add(p)
        p=Service(text="Organist")
        db.add(p)
        p=Service(text="Chor")
        db.add(p)
        p=Service(text="Lautsprechertraeger")
        db.add(p)
        p=Service(text="Himmeltraeger")
        db.add(p)
        db.commit()
        
    def create_basic_persons(self,cnt):
        db=baseModel.db_session()
        db.query(Person).delete()
        for i in range(cnt):
            p=Person(info="Person %d"%(i))
            db.add(p)
        db.commit()
        
    def create_basic_serviceproviders(self):
        db=baseModel.db_session()
        db.query(Person).delete()
        db.query(ServiceProvider).delete()
    
        for i in range(0,20):
            p=Person(info="Ministrant "+str(i))
            db.add(p)
            db.commit()
            
            qp = db.query(Person).filter(Person.info==p.info).one_or_none()
            qs=db.query(Service).filter(Service.text=="Ministrant").one_or_none()                
            #person_id=None, service_id=None, started=None, active=True
            tstart=datetime.now()-timedelta(days=365)
            sp=ServiceProvider(qp.id,qs.id,started=tstart.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),active=True)
            db.add(sp)
            db.commit()
        
    def create_basic_servicedemand(self):
        db=baseModel.db_session()
        db.query(ServiceDemand).delete()
        
        tstart=datetime.now()+timedelta(hours=10)
        tend=tstart+timedelta(minutes=45)
        info="Test Church"        
        a = Activity(start=tstart.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), end=tend.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), info=info)        
        db.add(a)        
        db.commit()
        
        qs = db.query(Service).filter(Service.text=="Ministrant").one_or_none()
        
        
        qa=db.query(Activity).filter(Activity.start==tstart).one_or_none()                        
        sd=ServiceDemand(activity_id=qa.id,service_id=qs.id,min_cnt=4,cnt=4,max_cnt=4,experience=0)
        db.add(sd)
        db.commit()
        
        db.close()      
        
        
        #self, activity_id=None, service_id=None, min_cnt=1, cnt=1, max_cnt=1, experience=0
        
        
        
        

    def tearDown(self):
        pass
    
    
    
    
    def test_0001_get_candidates(self):
        #self.create_basic_activity()
        self.create_basic_services()
        self.create_basic_serviceproviders()
        self.create_basic_servicedemand()
        db = baseModel.db_session()
        #activity = db.query(Activity).first()        
        serviceDemand = db.query(ServiceDemand).first()        
        candidates = autodispatch.get_candidates(serviceDemand)
        #db.close()
        for candidate in candidates:
            print(candidate.dump())




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_1']
    unittest.main()