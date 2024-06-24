from packages.cpu.cpu import CPU


if __name__ == "__main__":
    cpu = CPU()
    # Change op, rs, rt, rd, and fc variables to input diffrent instructions to the cpu.
    op = "000001"
    rs = "00000"
    rt = "00011"
    rd = "0000000000"
    fc = "000000"
    test_instruction = op + rs + rt + rd + fc

    cpu.read_instructions(test_instruction)
    


   
