#imports

#class
class ALU:
    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2
    
    def multiply(self, num1, num2):
        return num1 * num2
    
    def divide(self, num1, num2):
        try:
            return num1 // num2
        except ZeroDivisionError:
            print(f"Divison by zero error: {num1}/{num2}")
            return