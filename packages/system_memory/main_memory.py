#imports

#class
class Main_Memory():
    def __init__(self):
        self.data = [None for i in range(0, 18)]

    def read(self, address):
        if self.data[address] != None:
            return self.data[address]
        #Should return none on this return always
        return

    def write(self, address, data):
        self.data[address] = data
        
        