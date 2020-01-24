'''
Created on 24.09.2019

@author: markus.sedlmeier
'''

import logging

import os

import connexion

from models import baseModel
#import src.cleanup

logger = logging.getLogger("dispatcher")

def run(host, port, debugflag, ssl):

    app = connexion.App("Dispatcher", specification_dir='../src/apispec/',debug=True)
    app.add_api('api.yaml')
    
    flask_app=app.app
    application=flask_app
    
    logger.info("--------- START Dispatcher -------------")    
    db_uri='sqlite:///../db/database.sqlite3'
    
    baseModel.Create(db_uri)    
    
    #cleanup.startCleanupTask()    
    
    if ssl:
        app.run(host=host, port=port, debug=debugflag, ssl_context='adhoc',threaded=True)
    else:
        app.run(host=host, port=port, debug=debugflag,threaded=True)
    
    #cleanup.stopCleanupTask()