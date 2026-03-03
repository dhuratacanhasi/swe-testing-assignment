# Quick-Calc

Quick-Calc is a simple calculator application built with Python and Tkinter. It supports basic arithmetic operations with professional testing practices.

## Setup Instructions

### 1. Install Python
Download from: https://www.python.org/downloads/

### 2. Clone the repository
```bash
git clone https://github.com/yourusername/swe-testing-assignment.git
cd swe-testing-assignment

pip install -r requirements.txt
python -m calculator.gui
pytest --cov=calculator -v
pytest tests/test_integration.py -v