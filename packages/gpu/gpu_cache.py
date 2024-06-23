#imports
from .video_main_memory import VRAM
from ..cpu.cpu_cache import CPU_Cache
#class
class GPU_Cache(CPU_Cache):
    def __init__(self):
        super().__init__()
        self.data = [{"tag": None, "data": None},
                     {"tag": None, "data": None},
                     {"tag": None, "data": None},
                     {"tag": None, "data": None},
                     {"tag": None, "data": None},
                     {"tag": None, "data": None},
                     {"tag": None, "data": None},
                     {"tag": None, "data": None}]
        
        