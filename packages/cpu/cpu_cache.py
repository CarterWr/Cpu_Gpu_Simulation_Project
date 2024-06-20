#imports
from ..system_memory.memory import Memory
from ..system_memory.main_memory import Main_Memory
#class     
class CPU_Cache(Memory):

    def __init__(self):

        self.main_memory = Main_Memory()
        
        self.data = [{"tag": None, "data": None},
                     {"tag": None, "data": None},
                     {"tag": None, "data": None},
                     {"tag": None, "data": None}]
        
        self.sets = 1
        self.fifo_indices = [0, None, None, None]
    
    def read(self, address):
        pass

    def write(self, address, data):
        pass

    def fifo_policy(self, set_number):
        pass

    def replace_entry(self, address, data):
        pass

    def get_entry(self, address):
        pass
