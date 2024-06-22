# @TODO add functionality where class writes to a file and stores it to simulate disk storage

class Secondary_memory:
    def __init__(self):
        with open('secondary_memory_data.txt', 'r') as file:
            self.data = [line.strip('\n') for line in file.readlines() if line.strip() != '']


    def read(self, address):
         try:
             return self.data[address]
         except IndexError:
             print(f"Index Error: Index {address} is out of range: {address}/{len(self.data)}")
             return None

    def write(self, data):
        with open('secondary_memory_data.txt', 'a') as file:
            file.write((data + '\n'))
        #appending to our data list for our get index
        self.data.append(data)
        return 
    
    def get_index(self, data):
        try:
            return "".join(self.data).rindex(data)
        except ValueError:
            print("Value Error: Value given is not in secondary memory.")
            print(f"Here is a list of all data elements: {self.data}")
            return None
            