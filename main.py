from packages.cpu.cpu import CPU

#All (a few made up some from mips) CODES OP AND Function
#   OP   |   FC   |   DEF   
# 000101   ######   Sends instruction to gpu (Does not look at function if used)
# 000000   100000   Add two numbers from register
# 000000   100010   Subtract two numbers from register
# 000000   011000   Multiply two numbers from register
# 000000   011010   Divide two numbers from register
# 000001   000000   Store value to register
# 100001   000000   Return Most Recent Calculation 


if __name__ == "__main__":
    cpu = CPU()
    #Look at read me file to view all of the op codes and function codes

    #simple example of adding 3 to a register
    op = "000001"
    rs = "00000"
    rt = "00011"
    rd = "0000000000"
    fc = "000000"
    test_instruction = op + rs + rt + rd + fc
  
    # adds 7 to the next register
    op = "000001"
    rs = "00000"
    rt = "00111"
    rd = "0000000000"
    fc = "000000"
    test_instruction_1 = op + rs + rt + rd + fc
    # adds 18 to register
    op = "000001"
    rs = "00000"
    rt = "10010"
    rd = "0000000000"
    fc = "000000"
    test_instruction_2 = op + rs + rt + rd + fc
    # adds 18 and 7 and stores them at register 3
    op = "000000"
    rs = "00010"
    rt = "00001"
    rd = "0000000011"
    fc = "100000"
    test_instruction_3 = op + rs + rt + rd + fc
    
    # adds result stored at register 3 and number at register 2 stores result at register 7
    op = "000000"
    rs = "00001"
    rt = "00011"
    rd = "0000000111"
    fc = "100010"
    test_instruction_4 = op + rs + rt + rd + fc

    # gets previous calculation
    op = "100001"
    rs = "00000"
    rt = "00000"
    rd = "0000001000"
    fc = "000000"
    test_instruction_5 = op + rs + rt + rd + fc



    cpu.read_instructions(test_instruction)

    cpu.read_instructions(test_instruction_1)

    cpu.read_instructions(test_instruction_2)

    cpu.read_instructions(test_instruction_3)

    cpu.read_instructions(test_instruction_4)

    cpu.read_instructions(test_instruction_5)

    cpu.read_instructions(test_instruction_5)
