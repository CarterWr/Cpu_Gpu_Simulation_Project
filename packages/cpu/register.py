class Register:
    def __init__(self):
        self.data_registers = [0 for i in range(0, 24)]
        # register at index 0 is protected
        self.data_index = 1
        self.history_registers = [0 for i in range(0, 8)]
        self.history_index = 0
        #used to backtack one
        self.temp_history_index = 0

    def store(self, data, address=None):
        if address is None:
            address = self.data_index

            if self.data_index > 24:
                self.data_index = 1

            self.data_registers[self.data_index] = data

            self.data_index += 1

            #print(self.data_registers)
        
            return
        else:
            if address == 0:
                print("Error: Trying to overwrite a protected register.")
                return
            elif address > 24:
                print("Error: value passed through is larger than current data registers please enter a value between 1 and 24.")
                return
            else:
                self.data_registers[address] = data


                return


    def load(self, address):
         if address != 0 or None:
            return self.data_registers[address]
         else:
             print("Error: register at index 0 is protected please use another.")

    def store_to_history_register(self, result):
        if self.history_index > 9:
            self.history_index = 0
        
        self.history_registers[self.history_index] = result
        self.history_index += 1
        self.temp_history_index = self.history_index

    def get_last_history_register(self):

        # if you wish to see the one previous to the previos it keeps going till it hits 0
        if self.temp_history_index  != 0:
            self.temp_history_index -= 1
        else:
            print("Error: At the begining of the history index please do a new calculation to reset")
            return
        
        return self.history_registers[self.temp_history_index]
    