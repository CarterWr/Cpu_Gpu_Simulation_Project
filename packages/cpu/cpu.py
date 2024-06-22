#imports
from .cu import CU

#cpu class
class CPU:

    def __init__(self):
        self.cu = CU()

    def __del__(self):
        print("\nProgram shutting down, Have a nice day!\n")

    def check_instruciton(self, instruction):
        comparioson_set = {'0', '1'}

        if (type(instruction) != str):
            print("Error: please use a valid binary instruction. ex: 00000100011000010000000010000001")
            return False
        elif (set(instruction) != comparioson_set):
            print("Error: Instruction needs to contain binary only.")
            return False
        elif (len(instruction) < 32) or (len(instruction) > 32):
            print("Error: wrong instruction format please use a 32 length instruciton.")
            return False
        return True

    
    def read_instructions(self, instruction):
        if not self.check_instruciton(instruction):
            return
        self.cu.instruction_intake(instruction)

    

    