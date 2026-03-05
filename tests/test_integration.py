from calculator.gui import CalculatorGUI


def test_full_calculation():
 """Simulate user interaction: 5 + 3 = 8 """
 app = CalculatorGUI() 
 app.simulate_button_click('5')
 app.simulate_button_click('+')
 app.simulate_button_click('3')
 app.simulate_button_click('=')

 assert app.get_display_value()== '8'

def test_clear_button():
 """Tst that clear resets display"""
 app = CalculatorGUI()

 app.simulate_button_click('9')
 app.simulate_button_click('C')

 assert app.get_display_value()== '0'