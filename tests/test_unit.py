"""
Unit Tests for Quick-Calc
"""

import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculator.logic import CalculatorLogic


class TestCalculatorLogic:
    """Unit tests for CalculatorLogic class."""
    
    def setup_method(self):
        """Set up test fixtures before each test."""
        self.calc = CalculatorLogic()
    
    # === Basic Operations (4 tests) ===
    
    def test_addition_basic(self):
        """Test basic addition: 5 + 3 = 8"""
        result = self.calc.add(5, 3)
        assert result == 8
    
    def test_subtraction_basic(self):
        """Test basic subtraction: 10 - 4 = 6"""
        result = self.calc.subtract(10, 4)
        assert result == 6
    
    def test_multiplication_basic(self):
        """Test basic multiplication: 6 * 7 = 42"""
        result = self.calc.multiply(6, 7)
        assert result == 42
    
    def test_division_basic(self):
        """Test basic division: 20 / 4 = 5"""
        result = self.calc.divide(20, 4)
        assert result == 5.0
    
    # === Edge Cases (4+ tests) ===
    
    def test_division_by_zero_raises_error(self):
        """Test division by zero raises ValueError"""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)
    
    def test_negative_numbers(self):
        """Test operations with negative numbers"""
        assert self.calc.add(-5, 3) == -2
        assert self.calc.multiply(-4, -5) == 20
        assert self.calc.subtract(-10, -5) == -5
    
    def test_decimal_numbers(self):
        """Test operations with floating point numbers"""
        result = self.calc.add(0.1, 0.2)
        assert abs(result - 0.3) < 1e-9
    def test_very_large_numbers(self):
        """Test operations with very large numbers"""
        big = 1e150
        result = self.calc.multiply(big, big)
        # Use approximate comparison due to floating point precision
        assert abs(result - 1e300) < 1e290
    def test_calculate_method_routing(self):
        """Test generic calculate method routes correctly"""
        assert self.calc.calculate('+', 5, 3) == 8
        assert self.calc.calculate('-', 10, 4) == 6
        assert self.calc.calculate('*', 6, 7) == 42
        assert self.calc.calculate('/', 20, 4) == 5.0
    
    def test_calculate_unknown_operation(self):
        """Test calculate method with unknown operation"""
        with pytest.raises(ValueError, match="Unknown operation"):
            self.calc.calculate('^', 2, 3)
    
    def test_zero_operations(self):
        """Test operations involving zero"""
        assert self.calc.add(0, 5) == 5
        assert self.calc.subtract(5, 0) == 5
        assert self.calc.multiply(5, 0) == 0
        assert self.calc.divide(0, 5) == 0.0