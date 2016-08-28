import CalculatorView as view
from Util import CalculatorBrain as Brain
from Util import EventHandler

class CalculatorViewController(EventHandler):
    numberDisplaying = "0"
    brain = Brain()
    def __init__(self):
        view.handler = self
        view.load()

    @staticmethod
    def handle(eventStr):
        current = CalculatorViewController.numberDisplaying
        engine = CalculatorViewController.brain
        def clear(val="0"):
            CalculatorViewController.numberDisplaying = "0"
            view.setDisplay(val)
        try:
            if eventStr == 'C':
                clear()
                raise ValueError
            else:
                if eventStr == '.':
                    if current.find('.') < 0:
                        CalculatorViewController.numberDisplaying += '.'
                elif int(eventStr) in range(10):
                    if current == '0':
                        CalculatorViewController.numberDisplaying = eventStr
                    else:
                        CalculatorViewController.numberDisplaying += eventStr
                view.setDisplay(CalculatorViewController.numberDisplaying)
        except:
            if engine.accumulator == 0:
                engine.accumulator = float(current)
            view.setDisplay(eventStr)
            response = engine.calc(eventStr,float(current))
            if response == None:
                clear()
            else:
                view.setDisplay(response.val)
                if response.resetting:
                    CalculatorViewController.numberDisplaying = "0"

if __name__ == "__main__":
    calc = CalculatorViewController()
