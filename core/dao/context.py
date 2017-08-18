from pymongo import MongoClient

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=Singleton):
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.base = self.client.acessoria
        
    def get_base(self):
        return self.base
    