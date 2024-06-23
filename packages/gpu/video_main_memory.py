#imports

#class
class VRAM:
    def __init__(self):

        self.frame_buffer = [0 for i in range(0, 64)]

        self.test_buffer = [['H   H  III'],
                            ['H   H   I'],
                            ['HHHHH   I'],
                            ['H   H   I'],
                            ['H   H  III']]

    def display_frame_buffer(self):
        #change test buffer if created frame buffer functionality
        for line in self.test_buffer:
            for character in line:
                print(character)
