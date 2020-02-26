import sys
sys.path.append("../../")

from repositories.index import *
from services.raw.createrawdata import * 
from services.raw.showrawdata import *

class IndexRawServices():
  def __init__(self, repository = indexRepositories()):
    self.repository = repository['Raw']

  def create(self, data):
    rawData = createRawData(self.repository, data)
    
    return rawData

  def showData(self):
    rawData = showRawData(self.repository)

    return rawData
