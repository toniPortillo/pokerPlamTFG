import os

class Config_MongoDB(object):
    def __init__(self, host=os.environ["MONGOHOST"], port = int(os.environ["MONGOPORT"]),
    document_class = dict, tz_aware = False, connect = True):
        self._host = host
        self._port = port
        self._document_class = document_class
        self._tz_aware = tz_aware
        self._connect = connect 

    def gethost(self):
        return self._host

    def sethost(self, host):
        self._host = host
        
    def getport(self):
        return self._port

    def setport(self, port):
        self._port = port

    def getdocument_class(self):
        return self._document_class

    def setdocument_class(self, document_class):
        self._document_class = document_class
    
    def gettz_aware(self):
        return self._tz_aware

    def settz_aware(self, tz_aware):
        self._tz_aware = tz_aware

    def getconnect(self):
        return self._connect

    def setconnect(self, connect):
        self._connect = connect
