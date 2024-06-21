#imports
from .alu import ALU
from .cpu_cache import CPU_Cache
from .register import Register
from ..gpu.gpu import GPU


# ---Binary instructions breakdown---
# 0-5 in instruction is the op code 
# 6-10 is the register source
# 11-15 is the register target
# 16-25 is the register destination
# 26-31 is the function code section
#000000 00000 00000 0000000000 000000
#  OP    RS    RT       RD       FC


# When storing a number into registers it combines RS and RT

##000000 0000000000 0000000000 000000
#  OP        RS         RD       FC

#The RS is the number to store and rd is the register its getting stored to


#All (a few made up some from mips) CODES OP AND Function
#   OP   |   FC   |   DEF   
# 000101   ######   Sends instruction to gpu (Does not look at function if used)
# 000000   100000   Add two numbers from register
# 000000   100010   Subtract two numbers from register
# 000000   011000   Multiply two numbers from register
# 000000   011010   Divide two numbers from register
# 000001   000000   Store value to register
# 100001   000000   Return Most Recent Calculation 

#class
class CU:
    
    def __init__(self):
        self.alu = ALU()
        self.cache = CPU_Cache()
        self.register = Register()
        self.gpu = GPU()
    
    def read_binary(self, binary):
        return int(binary, 2)

    def instruction_intake(self, instruction):
        op = instruction[:6]
        
        # if using the gpu we dont need to more storage so only initalizing the op code variable
        if op == '000101':
            self.gpu.read_instruction(instruction[6:])

        rs = instruction[6:11]
        rt = instruction[11:16]
        rd = instruction[16:26]
        fc = instruction[26:32]

        if op == '000001':
            rs_number = self.read_binary(rs + rt)
            self.update_display(f"Adding {rs_number} to register")
            self.register.store(rs_number)
            return
        elif op == '100001':
            last_calculation_result = self.register.get_last_history_register()
            if last_calculation_result != None:
                self.update_display(f"Previous Calculation: {last_calculation_result}")
                return
            return
        elif op != '000000':
            print("Error: OP code is not in current list, please check current OP codes.")
            return
        
        
        rs_number = self.read_binary(rs)
        rt_number = self.read_binary(rt)
        rd_number = self.read_binary(rd)

        rs_register_number = self.register.load(rs_number)
        rt_register_number = self.register.load(rt_number)


        if fc == '100000':
            self.update_display(f"Adding {rs_register_number} and {rt_register_number}.")
            result = self.alu.add(rs_register_number, rt_register_number)
            self.arithmitic_repeats(result, rd_number)
            return
        if fc == '100010':
            self.update_display(f"Subtracting {rs_register_number} and {rt_register_number}.")
            result = self.alu.subtract(rs_register_number, rt_register_number)
            self.arithmitic_repeats(result, rd_number)
            return
        if fc == '011000':
            self.update_display(f"Multiplying {rs_register_number} and {rt_register_number}.")
            result = self.alu.multiply(rs_register_number, rt_register_number)
            self.arithmitic_repeats(result, rd_number)
            return
        if fc == '011010':
            self.update_display(f"Dividing {rs_register_number} and {rt_register_number}.")
            result = self.alu.divide(rs_register_number, rt_register_number)
            if result != None:
                self.arithmitic_repeats(result, rd_number)
                return
            else:
                return
        if fc != '000000':
            print("Error: Invalid function code(FC), please enter a vaild one.")
            return
        
        
    
    def update_display(self, text_to_display):
        print(text_to_display + '\n')
        return
    
    def arithmitic_repeats(self, result, rd_number):
        self.update_display(f"Storing {result} at register {rd_number}.")
        self.register.store(result, rd_number)
        self.register.store_to_history_register(result)