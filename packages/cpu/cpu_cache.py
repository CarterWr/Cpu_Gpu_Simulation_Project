#imports
from ..system_memory.main_memory import Main_Memory
#class     
class CPU_Cache:

    def __init__(self):

        self.main_memory = Main_Memory()
        
        self.data = [{"tag": None, "data": None},
                     {"tag": None, "data": None},
                     {"tag": None, "data": None},
                     {"tag": None, "data": None}]
        
        self.sets = 1
        self.fifo_indices = [0, None, None, None]
    
    def read(self, address):
        data = None
        entry = self.get_entry(address)
        if entry != None:
            data = entry["data"]
        else:
            data = self.main_memory.read(address)
            if data is None:
                print(f"Error: data at address {address} in primary memory is None.")
            self.replace_entry(address, data)

    def write(self, address, data):
        entry = self.get_entry(address)
        if entry != None:
            entry["data"] = data
        else:
            self.replace_entry(address, data)
        
        #print(self.data)

        self.main_memory.write(address, data)

    def fifo_policy(self, set_number):
        index = self.fifo_indices[set_number]
        self.fifo_indices[set_number] += 1
        if self.fifo_indices[set_number] == len(self.data)/self.sets+(set_number*int(len(self.data)/self.sets)):
            self.fifo_indices[set_number] = set_number*int(len(self.data)/ self.sets)
        
        return self.fifo_indices[set_number]

    def replace_entry(self, address, data):
        index = 0
        set_number = address % self.sets
        index = self.fifo_policy(set_number)
        self.data[index] = {"tag": address, "data": data}

    def get_entry(self, address):
        for entry in self.data:
            if entry["tag"] == address:
                print("Hit\n")
                return entry
        
        print("Miss\n")
        return None
