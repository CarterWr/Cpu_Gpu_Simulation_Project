from ..cpu.alu import ALU


class GPU_ALU(ALU):
    #Inherits all of alus method so it can "offload the cpu"
    
    def matrix_add(martix_1, matrix_2):
        pass

    def matrix_subtract(matrix_1, matrix_2):
        pass

    def matrix_multiplication(matrix_1, matrix_2):
        pass

    def matrix_divide(matrix_1, matrix_2):
        #to "divide" matrices you have to multiply matrix 1 by the inverse of matrix 2: matrix_1 * matrix_2^-1
        pass

    def scalar_multiplication(matrix, scalar):
        pass