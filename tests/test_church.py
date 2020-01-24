# coding: utf-8

from __future__ import absolute_import

from test_app import BaseTestCase
import base64
import json
from datetime import datetime
from datetime import timedelta
import unittest



class Test_Tickets(BaseTestCase):
    
    def getDatetimeNowString(self, addSec=0):
        dt=datetime.now()+timedelta(seconds=addSec)
        return dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    
    testticket=None
    
    def setUp(self):
        BaseTestCase.setUp(self)    
        print(unittest.TestCase.shortDescription(self))
        
    # -------------------------------------------------------------------------
    def test_001_create_a_ticket(self):     
        """create a ticket
        
        ticket init:
        def __init__(self, url=None, starttime=None, progress=0, status="CREATED", log="", 
                 expiresOn=None, releaseOn=None, stopurl=None, resulturl=None, logurl=None):    
        """
        global testticket        
        pwp=base64.b64encode(b"markus:m")
        response = self.client.post(
            '/ticket',            
            headers={"Content-type":"application/json", "Authorization": "Basic "+pwp.decode('utf-8')},
            data=json.dumps({
                  "progress":0,
                  "status":"Created",
                  "log":"+++teststring+++",
                  "expiresOn":self.getDatetimeNowString(60),
                  "releaseOn":self.getDatetimeNowString(120),
                  })            
            )            
        retstr=response.data.decode('utf-8')
        self.assert_status(response,201,'Response body is : ' + retstr)
        testticket=json.loads(retstr)
        print(testticket) 
        
        # get by id
        response = self.client.get(
            '/ticket/%s'%testticket["id"],            
            headers={"Content-type":"application/json", "Authorization": "Basic "+pwp.decode('utf-8')},
            )            
        retstr=response.data.decode('utf-8')
        self.assert_status(response,200,'Response body is : ' + retstr)
        ticketretId=json.loads(retstr)
        print(ticketretId)
        
        # get by uid
        response = self.client.get(
            '/ticket_by_uid/%s'%testticket["uid"],            
            headers={"Content-type":"application/json", "Authorization": "Basic "+pwp.decode('utf-8')},
            )            
        retstr=response.data.decode('utf-8')
        self.assert_status(response,200,'Response body is : ' + retstr)
        ticketretUId=json.loads(retstr)
        print(ticketretUId) 
        
    # -------------------------------------------------------------------------
    def test_101_get_ticket(self):     
        """get ticket by database id   
        """        
        pwp=base64.b64encode(b"markus:m")        
        # get by id
        response = self.client.get(
            '/ticket/%s'%testticket["id"],            
            headers={"Content-type":"application/json", "Authorization": "Basic "+pwp.decode('utf-8')},
            )            
        retstr=response.data.decode('utf-8')
        self.assert_status(response,200,'Response body is : ' + retstr)
        ticketretId=json.loads(retstr)
        print(ticketretId)
        
    # -------------------------------------------------------------------------
    def test_102_get_ticket_by_uid(self):     
        """get ticket by unique id 
        """        
        pwp=base64.b64encode(b"markus:m")                
        # get by uid
        response = self.client.get(
            '/ticket_by_uid/%s'%testticket["uid"],            
            headers={"Content-type":"application/json", "Authorization": "Basic "+pwp.decode('utf-8')},
            )            
        retstr=response.data.decode('utf-8')
        self.assert_status(response,200,'Response body is : ' + retstr)
        ticketretUId=json.loads(retstr)
        print(ticketretUId)
        
    def test_302_change_ticket_by_uid(self):     
        """change ticket by unique id 
        """        
        pwp=base64.b64encode(b"markus:m")                
        # get by uid
        response = self.client.put(
            '/ticket_by_uid/%s'%testticket["uid"],            
            headers={"Content-type":"application/json", "Authorization": "Basic "+pwp.decode('utf-8')},
            data=json.dumps({
                  "progress":50,
                  "status":"RUNNING",
                  "log":"+++ string changed +++"
                  })            
            )           
        retstr=response.data.decode('utf-8')
        self.assert_status(response,200,'Response body is : ' + retstr)
        ticketretUId=json.loads(retstr)
        print(ticketretUId)
        
    def test_501_delete_ticket(self):
        """delete ticket 
        """
        pwp=base64.b64encode(b"markus:m")                
        # get by uid
        response = self.client.delete(
            '/ticket/%s'%(testticket["id"]),            
            headers={"Content-type":"application/json", "Authorization": "Basic "+pwp.decode('utf-8')},
            )                    
        self.assert_status(response,204)
        
        
    def test_520_get_deleted_ticket(self):
        """try to get deleted ticket (expected to fail with 404) 
        """
        pwp=base64.b64encode(b"markus:m")                
        # get by uid
        response = self.client.get(
            '/ticket_by_uid/%s'%testticket["uid"],            
            headers={"Content-type":"application/json", "Authorization": "Basic "+pwp.decode('utf-8')},
            )                    
        self.assert_status(response,404)
                               

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()