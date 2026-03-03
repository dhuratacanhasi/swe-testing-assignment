"""
Core calculation logic for Quick-Calc application.
"""

class CalculatorLogic:
    """
    Handles all mathematical operations for the calculator.
    """
    
    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a."""
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """
        Divide a by b.
        Raises:
            ValueError: If b is zero (division by zero)
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def calculate(self, operation: str, a: float, b: float) -> float:
        """
        Generic calculator method that routes to specific operations.
        """
        operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }
        
        if operation not in operations:
            raise ValueError(f"Unknown operation: {operation}")
        
        return operations[operation](a, b)