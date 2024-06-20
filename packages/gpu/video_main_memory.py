#imports
from ..system_memory.memory import Memory

#class
class VRAM(Memory):
    def __init__(self):

        self.frame_buffer = []

    def display_frame_buffer(self):
        pass