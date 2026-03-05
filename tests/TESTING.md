Testing Strategy- Quick Calc
This document presents the testing strategy used in the testing the "QUICK-CALC" application. The testing strategy aims to guarantee the correctness,reliability of the calculator application through testing.

# 2. Testing Pyramid

The **Testing Pyramid** is a model that indicates the ideal proportion of tests in a software project.

The testing pyramid has three levels:

1. *Unit Tests (Base Level)*
   These tests are the most numerous, and the code snippets under test are small in size.  
   In the Quick-Calc project, the majority of the tests belong to this level, where the arithmetic calculations are performed.

2. *Integration Tests (Middle Level)*
   These tests test the integration of different components of the code.  
   In the Quick-Calc project, the tests in this level verify the interaction of the GUI components with the calculations.

3. *End-to-End Tests (Top Level)*
   These tests test the application as the user interacts with it.  
   Due to the small size of the project, the automated GUI tests were not performed.
   The project follows this pyramid structure by including **many unit tests and fewer integration tests**, which keeps the test suite fast and reliable.

---

# 3. Black-Box vs White-Box Testing

Two testing approaches were applied in this project:

### White-Box Testing
White-box testing focuses on the internal structure of the code.  
The unit tests for `CalculatorLogic` are an example of white-box testing because they directly test the internal methods such as:

- `add()`
- `subtract()`
- `multiply()`
- `divide()`
- `calculate()`

These tests verify that the internal logic behaves as expected.

### Black-Box Testing
Black-box testing focuses on testing the behavior of the system without considering its internal implementation.

The integration tests act as black-box tests because they simulate user actions through the GUI and verify the final output shown on the display.

For example:
- Entering `5 + 3 =` should display `8`
- Pressing `Clear` should reset the display to `0`

---

# 4. Functional vs Non-Functional Testing

### Functional Testing
Functional testing verifies that the application behaves according to its requirements.

In Quick-Calc, the following functional behaviors were tested:

- Addition operation
- Subtraction operation
- Multiplication operation
- Division operation
- Handling division by zero
- Working with decimal numbers
- Handling negative numbers
- Resetting the calculator with the Clear button
- Interaction between the GUI and calculation logic

### Non-Functional Testing
Non-functional testing evaluates aspects such as performance, usability, and security.

Due to the limited scope of this project, non-functional testing was not implemented. However, the application is lightweight and performs calculations instantly, which satisfies the basic performance expectations.

---
# 5. Regression Testing

Regression testing ensures that previously working functionality continues to work after code changes.

In this project, the automated test suite acts as a regression testing tool. Whenever the code is modified or new features are added, running the test suite ensures that existing functionality has not been broken.

The following command runs all tests:

If any test fails, it indicates that a recent change introduced a regression that must be fixed.

---

# 6. Test Results Summary

| Test Name | Type | Description | Status |
|----------|------|-------------|--------|
| test_addition_basic | Unit | Tests addition operation | Pass |
| test_subtraction_basic | Unit | Tests subtraction operation | Pass |
| test_multiplication_basic | Unit | Tests multiplication operation | Pass |
| test_division_basic | Unit | Tests division operation | Pass |
| test_division_by_zero_raises_error | Unit | Ensures division by zero raises error | Pass |
| test_negative_numbers | Unit | Tests operations with negative numbers | Pass |
| test_decimal_numbers | Unit | Tests floating point calculations | Pass |
| test_very_large_numbers | Unit | Tests calculations with very large values | Pass |
| test_calculate_method_routing | Unit | Verifies calculate() method routing | Pass |
| test_calculate_unknown_operation | Unit | Tests invalid operation handling | Pass |
| test_zero_operations | Unit | Tests operations involving zero | Pass |
| test_full_calculation | Integration | Simulates full calculation (5 + 3 = 8) | Pass |
| test_clear_button | Integration | Ensures clear button resets display | Pass |

---

# 7. Conclusion

The Quick-Calc testing strategy combines **unit testing and integration testing** to ensure correctness and reliability. Unit tests verify the internal mathematical logic, while integration tests ensure that the GUI correctly interacts with the calculation logic.

By following the **Testing Pyramid principles** and using automated tests, the project achieves a maintainable and reliable testing structure suitable for future development.