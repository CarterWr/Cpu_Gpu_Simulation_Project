#imports

#class
class ALU:
    def add(num1, num2):
        return num1 + num2
    
    def subtract(num1, num2):
        return num1 - num2
    
    def multiply(num1, num2):
        return num1 * num2
    
    def divide(num1, num2):
        try:
            return num1 // num2
        except ZeroDivisionError:
            print(f"Divison by zero error: {num1}/{num2}")
