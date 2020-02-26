import sys
sys.path.append('../../')

from config.configMongoDB import *
from pymongo import MongoClient

class DevDB(Config_MongoDB):
  def __init__(self):
    Config_MongoDB.__init__(self)
    self.client = MongoClient(self.gethost(), self.getport())

  def mongodbdev(self):
    return self.client.PocDBDev
