# Quick-Calc

Quick-Calc is a simple desktop calculator application built with Python and Tkinter.  
The application supports basic arithmetic operations and demonstrates software testing practices using unit tests and integration tests.

---

## Features

- Basic arithmetic operations (+, -, *, /)
- Decimal number support
- Clear (C) functionality
- Division by zero error handling
- Simple graphical user interface (GUI)
- Unit testing for calculator logic
- Integration testing for GUI interaction
- Test coverage using pytest-cov

---

## Project Structure

```
swe-testing-assignment
│
├── calculator
│   ├── gui.py
│   ├── logic.py
│
├── tests
│   ├── test_unit.py
│   ├── test_integration.py
│
├── requirements.txt
├── README.md
└── TESTING.md
```

---

## Requirements

- Python 3.8 or higher
- pip

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/dhuratacanhasi/swe-testing-assignment.git
cd swe-testing-assignment
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Calculator

To start the calculator application run:

```bash
python -m calculator.gui
```

---

## Running Tests

Run all tests:

```bash
pytest -v
```

Run tests with coverage:

```bash
pytest --cov=calculator -v
```

Run only integration tests:

```bash
pytest tests/test_integration.py -v
```

---

## Testing Strategy

This project includes two levels of testing.

### Unit Testing

Unit tests verify that the calculator logic works correctly independent of the graphical interface.

The following cases are tested:

- Addition
- Subtraction
- Multiplication
- Division
- Division by zero
- Decimal number operations
- Negative numbers
- Large numbers
- Operation routing

### Integration Testing

Integration tests verify the interaction between the GUI and the calculator logic.

These tests simulate button clicks and ensure that:

- calculations work through the interface
- the display updates correctly
- the clear button resets the calculator state

---

## Technologies Used

- Python
- Tkinter
- Pytest
- Pytest-Cov

---

## Author

Software Engineering Testing Assignment Project- Dhurate Canhasi