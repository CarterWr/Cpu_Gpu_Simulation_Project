# Cpu Gpu Simulation Project
 
## Instructions

   ![](https://github.com/CarterWr/Cpu_Gpu_Simulation_Project/blob/main/Instruciton_photo.png)

   * Above is a image of the code contained in main.py file (where the executeable code runs)
   * To give diffrent instrucitons to the cpu you change op and fc.
     * [NOTE: THE GPU ALSO HAS ITS OWN OP AND FC CODES THOSE WILL BE BELOW]
     * [NEEDED: USE OP: '000101' as the deafult to access gpu alu operations]
     * op is Operation Code, it tells the cpu CU what to run or where to put/access data (if op code is '000000' then its assumed the instruction is a function code instruction) 
     * fc is Function Code, it tells the cpu if the instruction is not using a op code to utalize the cpu's alu(Arithmetic logic unit) and do operations on the register address given (rs, rt)
   
   * LIST OF ALL CURRENT CPU OP AND FC CODES AND THEIR DEFINTIONS
   *     OP    000001      Store value to register
   *     OP    100001      Return Most Recent Calculation 
   *     OP    100011      Return entry at cache at given location (RD)  
   *     OP    100101      Writes given data to cache at next avalable address
   *     OP    010010      Stores value to secondary memory (when storing using this op code only rs+rt is being looked at)
   *     OP    110001      Returns value at given address in secondary memory (only rd is going to be looked at)
   *     OP    000101  Sends instruction to gpu (Does not look at function code if used)
   *     FC    100000   Add two numbers from register
   *     FC    100010   Subtract two numbers from register
   *     FC    011000   Multiply two numbers from register
   *     FC    011010   Divide two numbers from register
   * LIST OF ALL CURRENT GPU OP AND FC CODES AND THEIR DEFINTIONS
   *     OP   110011     Writes given data to cache at next avalable address
   *     OP   111011     Return entry at cache at given location (RD)
   *     OP   111000     Reads current frame buffer even if unfinished (NO ACTUAL FRAM BUFFER FUNCTIONALITY) 
   *     OP   010011     Store value to register (uses rs + rt)
   *     OP   101011     Return Most Recent Calculation
   *     FC   100000     Adds 2 basic numbers from register
   *     FC   100010     Subtracts 2 basic numbers from register
   *     FC   011000     Multiplies 2 basic numbers from register
   *     FC   011010     Divides 2 basic numbers from register
   *     FC   011100     Adds 2 vectors 
   *     FC   100111     Subtracts 2 vectors 
   *     FC   110011     Multiply a vector by a scalar (vector is made up of the same passed in number)
   *     FC   111000     Divides a vector by a scalar (vector is made up of the same passed in number)

   * RS is Register Source, A address in a register that contains a value to do a operation on
   * RT is Register To, A address in a register that contains a value to use to do an operation
   * RD is Register Direction, A address where to store the result of an operation done on RS and RT
   * When storing data into a register or cache or memory user a combonation of RS+RT
   
 
