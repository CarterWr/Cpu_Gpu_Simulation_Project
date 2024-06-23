#imports
from .gpu_alu import GPU_ALU
from .gpu_cache import GPU_Cache
from .gpu_register import GPU_Register
from .video_main_memory import VRAM


#class
#GPU CODES
#   OP   |   FC   |   DEF   
# 000101   100000   Adds 2 basic numbers from register
# 000101   100010   Subtracts 2 basic numbers from register
# 000101   011000   Multiplies 2 basic numbers from register
# 000101   011010   Divides 2 basic numbers from register
# 000101   011100   Adds 2 matrices (or vectors)
# 000101   100111   Subtracts 2 matrices (or vectors)
# 000101   111000   Multiply 2 matrices (or vectors)
# 000101   110011   Divides 2 matrices (or vectors)
# 110011   000000   Writes given data to cache at next avalable address
# 111011   000000   Return entry at cache at given location (RD)
# 111000   000000   Reads current frame buffer even if unfinished (NO ACTUAL FRAM BUFFER FUNCTIONALITY) 
# 010011   000000   Store value to register (uses rs + rt)
# 101011   000000   Return Most Recent Calculation

class GPU_CU: # IDEA: make this a child of cpu cu and fix circular imports with cu
    def __init__(self):
        self.gpu_alu = GPU_ALU()
        self.gpu_cache = GPU_Cache()
        self.gpu_register = GPU_Register()
        self.vram = VRAM()

    def read_binary(self, instruction):
        return int(instruction, 2)
    
    def update_display(self, text_to_display):
        print(text_to_display + '\n')
        return

    def instruction_intake(self, instruction):
        op = instruction[:6]
        rs = instruction[6:11]
        rt = instruction[11:16]
        rd = instruction[16:26]
        

        if op == '110011':
            data = self.read_binary(rs + rt)
            rd_number = self.read_binary(rd)
            self.update_display(f"Writing data {data} at with tag {rd_number} in cache.")
            self.gpu_cache.write(rd_number, data)
            return
        elif op == '111011':
            rd_number = self.read_binary(rd)
            self.update_display(f"Looking for data with location {rd_number} in the Cache.")
            self.gpu_cache.read(rd_number)
            return
        elif op == '111000':# IDEA: add working frame buffer that displays a frame inputed by numbers
            self.update_display("[ONLY FOR SHOW]Displaying current frame buffer.\n")
            self.vram.display_frame_buffer()
            return
        elif op == '010011':
            rs_number = self.read_binary(rs + rt)
            self.update_display(f"Adding {rs_number} to register")
            self.gpu_register.store(rs_number)
            return
        elif op == '101011':
            last_calculation_result = self.gpu_register.get_last_history_register()
            if last_calculation_result != None:
                self.update_display(f"Previous Calculation: {last_calculation_result}")
            return
        elif op != '000101':
            print("GPU CU Error: OP code is not in current list, please check current OP codes.")
            return

        fc = instruction[26:32]

        rs_number = self.read_binary(rs)
        rt_number = self.read_binary(rt)
        rd_number = self.read_binary(rd)
        
        rs_register_number = self.gpu_register.load(rs_number)
        rt_register_number = self.gpu_register.load(rt_number)

        if rs_register_number == 0 or rs_register_number == None:
            return
        elif rt_register_number == 0 or rt_register_number == None:
            return


        if fc == '100000':
            self.update_display(f"Adding {rs_register_number} and {rt_register_number}.")
            result = self.gpu_alu.add(rs_number, rt_number)
            self.arithmitic_repeats(result, rd_number)
            return
        elif fc == '100010':
            self.update_display(f"Subtracting {rs_register_number} and {rt_register_number}.")
            result = self.gpu_alu.subtract(rs_number, rt_number)
            self.arithmitic_repeats(result, rd_number)
            return
        elif fc == '011000':
            self.update_display(f"Multiplying {rs_register_number} and {rt_register_number}.")
            result = self.gpu_alu.multiply(rs_number, rt_number)
            self.arithmitic_repeats(result, rd_number)
            return
        elif fc == '011010':
            self.update_display(f"Dividing  {rs_register_number} and {rt_register_number}.")
            result = self.gpu_alu.divide(rs_number, rt_number)
            self.arithmitic_repeats(result, rd_number)
            return
        elif fc == '011100': # ADD working vector/matrix operation functionality
            result = self.gpu_alu.matrix_add(rs_number, rt_number)
            self.arithmitic_repeats(result, rd_number)
            return
        elif fc == '100111':
            result = self.gpu_alu.matrix_subtract(rs_number, rt_number)
            self.arithmitic_repeats(result, rd_number)
            return
        elif fc == '111000':
            result = self.gpu_alu.matrix_multiply_inverse(rs_number, rt_number)
            self.arithmitic_repeats(result, rd_number)
            return
        elif fc == '110011':
            result = self.gpu_alu.scalar_multiply(rs_number, rt_number)
            self.arithmitic_repeats(result, rd_number)
            return
        elif fc != '000000':
            print("GPU CU Error: Invalid function code(FC), please enter a vaild one.")
            return
        
        return
    
    def arithmitic_repeats(self, result, rd_number):
        self.update_display(f"Storing {result} at register {rd_number}.")
        self.gpu_register.store(result, rd_number)
        self.gpu_register.store_to_history_register(result)
    
    