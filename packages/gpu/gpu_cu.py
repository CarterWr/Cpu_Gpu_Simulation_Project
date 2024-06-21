#imports
from .gpu_alu import GPU_ALU
from .gpu_cache import GPU_Cache
from .gpu_register import GPU_Register
from .video_main_memory import VRAM
#class
class GPU_CU:
    def __init__(self):
        self.gpu_alu = GPU_ALU()
        self.gpu_cache = GPU_Cache()
        self.gpu_register = GPU_Register()
        self.vram = VRAM()


    def instuction_intake(self, instruction):
        pass