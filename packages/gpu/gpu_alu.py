from ..cpu.alu import ALU

class GPU_ALU(ALU):

    def vector_add(self, num1, num2):
        vector1 = [num1 for i in range(3)]
        vector2 = [num2 for i in range(3)]
        
        return [vector1[i] + vector2[i] for i in range(len(vector1))]

    def vector_subtract(self, num1, num2):
        vector1 = [num1 for i in range(3)]
        vector2 = [num2 for i in range(3)]

        return [vector1[i] - vector2[i] for i in range(len(vector1))]

    def vector_divide(self, num1, scalar):
        if scalar == 0:
            print("Division By Zero Error: cannot have scalar value be 0.")
            return
        vector1 = [num1 for i in range(3)]
        
        return [vector1[i] // scalar for i in range(len(vector1))]

    def scalar_multiply(eslf, num1, scalar):
        vector1 = [num1 for i in range(3)]
        
        return [vector1[i] * scalar for i in range(len(vector1))]