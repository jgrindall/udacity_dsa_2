import hashlib
from datetime import datetime,timezone
 
class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.__timestamp = timestamp
        self.__data = data
        self.__previous_hash = previous_hash
        self.__hash = self.__calc_hash()
        self.__next = None
    
    def __calc_hash(self):
        data_enc = str(self.data).encode('utf-8')
        sha = hashlib.sha256()
        sha.update(data_enc)
        return sha.hexdigest()

    @property
    def timestamp(self):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, value):
        raise RuntimeError('can\'t reset the timestamp attribute.')
      
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
      raise RuntimeError('can\'t reset the data attribute.')
      
    @property
    def previous_hash(self):
        return self.__previous_hash

    @previous_hash.setter
    def previous_hash(self, value):
      raise RuntimeError('can\'t reset the previous_hash attribute.')
      
    @property
    def hash(self):
        return self.__hash

    @hash.setter
    def hash(self, value):
      raise RuntimeError('can\'t reset the hash attribute.')
      
    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        if self.__next:
            raise RuntimeError('can\'t reset the next attribute.')
        else:
            self.__next = next


class Blockchain():
    def __init__(self):
        self.root = None
    
    def add(self, data):
        if not self.root:
            self.root = Block(self.__get_timestamp(), data, None)
        else:
            node = self.root
            while node.next:
                node = node.next
            prev_hash = node.hash
            block = Block(self.__get_timestamp(), data, prev_hash)
            node.next = block

    def __get_timestamp(self):
        return datetime.now(timezone.utc).timestamp() * 1000
