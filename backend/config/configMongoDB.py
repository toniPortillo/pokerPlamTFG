import os

class Config_MongoDB(object):
    def __init__(self, host: str = os.environ["MONGOHOST"], port: int = int(os.environ["MONGOPORT"]),
    document_class: dict = dict, tz_aware: bool = False, connect: bool = True) -> None:
        self.__host = host
        self.__port = port
        self.__document_class = document_class
        self.__tz_aware = tz_aware
        self.__connect = connect 

    @property
    def host(self) -> str:
        return self.__host

    @host.setter
    def sethost(self, host: str) -> None:
        self.__host = host
        
    @property
    def port(self) -> int:
        return self.__port

    @port.setter
    def port(self, port) -> None:
        self.__port = port

    @property
    def document_class(self) -> dict:
        return self.__document_class

    @document_class.setter
    def document_class(self, document_class) -> None:
        self.__document_class = document_class
    
    @property
    def tz_aware(self) -> bool:
        return self.__tz_aware

    @tz_aware.setter
    def tz_aware(self, tz_aware) -> None:
        self.__tz_aware = tz_aware

    @property
    def connect(self) -> bool:
        return self.__connect

    @connect.setter
    def connect(self, connect) -> None:
        self.__connect = connect
