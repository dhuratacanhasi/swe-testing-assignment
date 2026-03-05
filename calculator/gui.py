"""
Tkinter GUI for Quick-Calc.
"""

import tkinter as tk
from tkinter import messagebox
from .logic import CalculatorLogic


class CalculatorGUI:
    """
    Graphical user interface for the calculator.
    """
    
    def __init__(self):
        self.logic = CalculatorLogic()
        self.window = tk.Tk()
        self.window.title("Quick-Calc")
        self.window.geometry("300x400")
        self.window.resizable(False, False)
        
        # State variables
        self.current_input = ""
        self.previous_value = None
        self.current_operation = None
        self.reset_next = False
        
        self._create_ui()
    
    def _create_ui(self):
        """Create the calculator interface."""
        # Display
        self.display = tk.Entry(
            self.window, 
            font=('Arial', 24), 
            justify='right',
            bd=10,
            insertwidth=2,
            width=14,
            borderwidth=4
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.display.insert(0, "0")
        
        # Button layout
        buttons = [
         ('C', 1, 0), ('', 1, 1), ('', 1, 2), ('/', 1, 3),
         ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
         ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
         ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
         ('0', 5, 0), ('.', 5, 1), ('=', 6, 2, 2) 
        ]
        
        for btn in buttons:
             text, row, col = btn[0], btn[1], btn[2]
             colspan = btn[3] if len(btn) > 3 else 1 
             if text != "": 
              button = tk.Button(
              self.window,
              text=text,
              font=('Arial', 18,"bold"),
              bg='#4A90D9',      
              fg='white',                              
              bd=3,
              relief="raised",      
             command=lambda t=text: self._on_button_click(t)
            )
             button.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5,sticky="nsew")  
    
        for i in range(7):
            self.window.grid_rowconfigure(i,weight=1)
        for j in range (4):
            self.window.grid_columnconfigure(j,weight=1)    
    def _on_button_click(self, char: str):
        """Handle button click events."""
        if char.isdigit():
            self._handle_digit(char)
        elif char == 'C':
            self._clear()
        elif char == '=':
            self._calculate_result()
        elif char in '+-*/':
            self._handle_operation(char)
        elif char == '.':
            self._handle_decimal()
    
    def _handle_digit(self, digit: str):
        """Handle digit input."""
        if self.reset_next:
            self.current_input = digit
            self.reset_next = False
        else:
            if self.current_input == "0":
                self.current_input = digit
            else:
                self.current_input += digit
        self._update_display()
    
    def _handle_operation(self, op: str):
        """Handle operation button press."""
        if self.current_input:
            self.previous_value = float(self.current_input)
            self.current_operation = op
            self.reset_next = True
    
    def _calculate_result(self):
        """Execute calculation and display result."""
        if self.previous_value is not None and self.current_operation and self.current_input:
            try:
                current = float(self.current_input)
                result = self.logic.calculate(
                    self.current_operation, 
                    self.previous_value, 
                    current
                )
                
                # Format result (remove .0 for integers)
                if result == int(result):
                    self.current_input = str(int(result))
                else:
                    self.current_input = str(result)
                
                self._update_display()
                self.reset_next = True
                self.previous_value = None
                self.current_operation = None
                
            except ValueError as e:
                messagebox.showerror("Error", str(e))
                self._clear()
    
    def _clear(self):
     self.current_input = ""
     self.previous_value = None
     self.current_operation = None
     self.reset_next = False
     self._update_display("0") 
    
    def _handle_decimal(self):
        """Handle decimal point input."""
        if '.' not in self.current_input:
            self.current_input += '.' if self.current_input else '0.'
            self._update_display()
    
    def _update_display(self, value=None):
        """Update the display with current value."""
        self.display.delete(0, tk.END)
        self.display.insert(0, value if value is not None else self.current_input)
    
    def run(self):
        """Start the application."""
        self.window.mainloop()
    
    # Methods for integration testing
    def get_display_value(self) -> str:
        """Get current display value (for testing)."""
        return self.display.get()
    
    def simulate_button_click(self, button: str):
        """Simulate button press (for integration testing)."""
        self._on_button_click(button)
    
    def clear(self):
        """Public clear method (for testing)."""
        self._clear()


def main():
    """Entry point for the application."""
    app = CalculatorGUI()
    app.run()


if __name__ == "__main__":
    main()