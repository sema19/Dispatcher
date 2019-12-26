'''
Created on 29.08.2019

@author: markus.sedlmeier
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_URI='sqlite:///../db/database.sqlite3'
engine = create_engine(DB_URI, convert_unicode=True)


db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)
    )


class DbBaseMixin(object): 
    def dump(self):
        return dict([(k,v) for k,v in vars(self).items() if not k.startswith('_')])
    def setDefault(self, connection):
        print("no default setting available")
    def update(self, **odata):
        commitflag=False        
        for val in odata.keys():
            if val in vars(self).keys():
                if vars(self)[val]!=odata[val]:
                    self.__setattr__(val, odata[val])   # note: vars(self)[val]=odata[val] does not work                    
                    commitflag=True                
            else:
                print("Not able to assign %s"%(val))
        return commitflag
        
DbBase = declarative_base(cls=DbBaseMixin)
DbBase.query = db_session.query_property()

    
def Create():
    #import my models
    DbBase.metadata.create_all(bind=engine)
    
def Teardown():
    db_session.remove()
    

    
    
        

