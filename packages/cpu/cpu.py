#imports
from .cu import CU

#cpu class
class CPU:

    def __init__(self):
        self.cu = CU()

    
    def read_instructions(self, instruction):
        pass

    def update_display(self, text_to_display):
        print(text_to_display)

    