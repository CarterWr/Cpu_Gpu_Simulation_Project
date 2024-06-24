#imports
from .gpu_alu import GPU_ALU
from .gpu_cache import GPU_Cache
from .gpu_register import GPU_Register
from .video_main_memory import VRAM



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
            self.update_display(f"Error: register at index 0 is protected please use another. rs num: {rs_register_number}")
            return
        elif rt_register_number == 0 or rt_register_number == None:
            self.update_display(f"Error: register at index 0 is protected please use another. rt num: {rt_register_number}")
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
            self.update_display(f"Dividing {rs_register_number} and {rt_register_number}.")
            result = self.gpu_alu.divide(rs_number, rt_number)
            self.arithmitic_repeats(result, rd_number)
            return
        elif fc == '011100': # ADD working vector/vector operation functionality
            self.update_display(f"Converting {rs_register_number} and {rt_register_number} to vectors and adding them.")
            result = self.gpu_alu.vector_add(rs_register_number, rt_register_number)
            self.arithmitic_repeats(result, rd_number)
            return
        elif fc == '100111':
            self.update_display(f"Converting {rs_register_number} and {rt_register_number} to vectors and subtracting them.")
            result = self.gpu_alu.vector_subtract(rs_register_number, rt_register_number)
            self.arithmitic_repeats(result, rd_number)
            return
        elif fc == '111000':
            self.update_display(f"Converting {rs_register_number} to a vector and  {rt_register_number} is a scalar dividing them.")
            result = self.gpu_alu.vector_divide(rs_register_number, rt_register_number)
            self.arithmitic_repeats(result, rd_number)
            return
        elif fc == '110011':
            self.update_display(f"Converting {rs_register_number} to a vector and  {rt_register_number} is a scalar multiplying them.")
            result = self.gpu_alu.scalar_multiply(rs_register_number, rt_register_number)
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
    
    