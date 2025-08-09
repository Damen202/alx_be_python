class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method"""
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """Class Method"""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
    

    