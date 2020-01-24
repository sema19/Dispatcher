import logging

import connexion
from flask_testing import TestCase
from models import baseModel

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
lfh=logging.FileHandler(os.path.join(logpath,"dispatchertest.log"))
lfh.setLevel(logging.DEBUG)
logger.addHandler(lfh)


class BaseTestCase(TestCase):

    def create_app(self):
        #logging.getLogger('connexion.operation').setLevel('ERROR')
        #app = connexion.App(__name__, specification_dir='../api/')
        app = connexion.App(__name__, specification_dir='../src/apispec/',debug=True)
        #Bootstrap(app.app)
        app.app.config['TESTING'] = True
        #app.app.config['BOOTSTRAP_SERVE_LOCAL'] = True
        app.app.config['LIVESERVER_HOST'] = "0.0.0.0"
        app.app.config['LIVESERVER_PORT'] = 8223
        app.app.config['LIVESERVER_TIMEOUT'] = 10 
        app.add_api('api.yaml')
        #app.add_url_rule('/','/',webpage_ctrl.page_new_version)
        db_uri_test='sqlite:///../tests/db/database.sqlite3'
        baseModel.Create(db_uri_test)
        
        return app.app
    
    #def test_server_is_up_and_running(self):
        #response = urllib2.urlopen(self.get_server_url())
        #self.assertEqual(response.code, 200)
    