#imports
from .alu import ALU
from .cpu_cache import CPU_Cache
from .register import Register
from ..gpu.gpu import GPU



#class
class CU:
    
    def __init__(self):
        self.alu = ALU()
        self.cache = CPU_Cache()
        self.register = Register()
        self.gpu = GPU()
    
    def read_binary(self, binary):
        pass

    def instruction_intake(self, instruction):
        pass
    
    