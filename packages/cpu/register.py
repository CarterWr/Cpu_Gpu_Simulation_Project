class Register:
    def __init__(self):
        self.data_registers = [0 for i in range(0, 24)]
        self.history_registers = [0 for j in range(0, 8)]

    def store(self, address, data):
        pass

    def load(self, address):
        pass 