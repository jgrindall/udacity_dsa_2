import hashlib
from datetime import datetime,timezone
 
class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
    
    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(self.data)
        return sha.hexdigest()
    


//TODO - @property to stop them being modified

class Blockchain():
    def __init__(self):
        self.tail = None
    
    def add(self, data):
        prev_hash = self.tail.hash if self.tail is not None else None
        block = Block(self.__get_timestamp(), data, prev_hash)
        self.tail = block

    def __get_timestamp():
        return datetime.now(timezone.utc).timestamp() * 1000


#Finally you need to link all of this together in a block chain, which you will be doing by implementing
#it in a linked list. All of this will help you build up to a simple but full blockchain implementation!
 
 
