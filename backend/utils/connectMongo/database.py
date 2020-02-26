import sys
sys.path.append("../../")

import os
from utils.connectMongo.devdb import *
from utils.connectMongo.prodb import *
from utils.connectMongo.testdb import *

class FactoryDatabase:

    @staticmethod
    def get_database(enviroment): 
        if enviroment == "ENV":
            devdb = DevDB()
            return devdb.mongodbdev()
        elif enviroment == "PRO":
            prodb = ProDB()
            return prodb.mongodbpro()
        elif enviroment == "TEST":
            testdb = TestDB()
            return testdb.mongodbtest()
        else:
            testdb = TestDB()
            return testdb.mongodbtest()
            
