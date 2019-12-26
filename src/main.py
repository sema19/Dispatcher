'''
Created on Dec 1, 2019

@author: sedlmeier
'''

import os

import configparser
settings = configparser.ConfigParser()
settings.read("../config/config.ini")

import logging

logger = logging.getLogger("dispatcher")
logger.setLevel(logging.DEBUG)
logpath=os.path.join(os.getcwd(),"log")
if not os.path.exists(logpath):
    os.makedirs(logpath)
lfh=logging.FileHandler(os.path.join(logpath,"dispatcher.log"))
lfh.setLevel(logging.DEBUG)
logger.addHandler(lfh)


import app

if __name__ == '__main__':
        
    host=settings.get("webserver","host")
    port=settings.get("webserver","port")
    debugflag=settings.getboolean("webserver","debug")
    ssl=settings.getboolean("webserver","secure")
    
    app.run(host, port, debugflag,ssl)    