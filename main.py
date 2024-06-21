from packages.cpu.cpu import CPU

#All (a few made up some from mips) CODES OP AND Function
#   OP   |   FC   |   DEF   
# 000101   ######   Sends instruction to gpu (Does not look at function code if used)
# 000000   100000   Add two numbers from register
# 000000   100010   Subtract two numbers from register
# 000000   011000   Multiply two numbers from register
# 000000   011010   Divide two numbers from register
# 000001   000000   Store value to register
# 100001   000000   Return Most Recent Calculation 
# 100011   000000   Return entry at cache at given location (RD)  
# 100101   000000   Writes given data to cache at next avalable address 


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


  

    cpu.read_instructions(test_instruction)

   
