from ..cpu.register import Register
class GPU_Register(Register):
    def __init__(self):
        super().__init__()
        self.data_registers = [0 for i in range(0, 54)]
        self.history_registers = [0 for j in range(0, 12)]

    def store(self, address, data):
        pass

    def load(self, address):
        pass 