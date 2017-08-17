from pymongo import MongoClient

class Database:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.base = self.client.acessoria
        
    def get_base(self):
        return self.base
    