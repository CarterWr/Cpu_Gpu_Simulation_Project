# Cpu Gpu Simulation Project
 
## Instructions

   ![](https://github.com/CarterWr/Cpu_Gpu_Simulation_Project/blob/main/Instruciton_photo.png)

   * Above is a image of the code contained in main.py file (where the executeable code runs)
   * To give diffrent instrucitons to the cpu you change op and fc.
     * [NOTE: THE GPU ALSO HAS ITS OWN OP AND FC CODES THOSE WILL BE BELOW]
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
   
