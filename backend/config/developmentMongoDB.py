import os

class Development_MongoDB:
    def __init__(self, host=os.environ["MONGOIP"], port = int(os.environ["MONGOPORT"]),
    document_class = dict, tz_aware = False, connect = True):
        self.host = host
        self.port = port
        self.document_class = document_class
        self.tz_aware = tz_aware
        self.connect = connect 

    def gethost(self):
        return self.host

    def sethost(self, host):
        self.host = host
        
    def getport(self):
        return self.port

    def setport(self, port):
        self.port = port

    def getdocument_class(self):
        return self.document_class

    def setdocument_class(self, document_class):
        self.document_class = document_class
    
    def gettz_aware(self):
        return self.tz_aware

    def settz_aware(self, tz_aware):
        self.tz_aware = tz_aware

    def getconnect(self):
        return self.connect

    def setconnect(self, connect):
        self.connect = connect
