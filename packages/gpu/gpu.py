# imports
from .gpu_cu import GPU_CU
# class
class GPU:
    def __init__(self):
        self.gpu_cu = GPU_CU()
        
    def read_instructions(self, instruction):
        self.gpu_cu.instruction_intake(instruction)
