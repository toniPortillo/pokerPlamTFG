class RawRepository():
  def __init__(self, rawEntity):
    self.rawEntity = rawEntity

  def create(self, rawdata):
    return self.rawEntity.insert_one(
      rawdata
    )

  def getAll(self):
    alldata = self.rawEntity.find()
    return alldata
