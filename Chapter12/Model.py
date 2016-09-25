import math, tkinter

window = tkinter.Tk()

class Button():
    def __init__(self, title, x, y, width=1,height=1):
        self.title = title
        self.x = x
        self.y = y
        self.w = width
        self.h = height

class EventHandler():
    numberDisplaying = "0"
    @staticmethod
    def handle(eventStr):
        print("Generic handling",eventStr)

class CalculatorBrain():
    class Response():
        def __init__(self,val,resetting=False):
            self.val = val
            self.resetting = resetting
    
    def calc(self, expression, newValue = None):
        #print(expression,self.accumulator,newValue)
        if expression == 'C':
            self.clear()
        elif expression == '=':
            try:
                self.accumulator = self.supported[self.operator](self.accumulator, newValue)
                return CalculatorBrain.Response(self.accumulator)
            except:
                self.clear()
        elif expression in self.supported.keys():
            self.operator = expression
            return CalculatorBrain.Response(self.operator, True)
        else:
            self.clear()
    
    def __init__(self):
        self.reset()

    def clear(self):
        self.accumulator = 0
        self.operator = ''
        self.floatingLength = 0
        self.cleared = True
    
    def reset(self):
        def sqrt(x,y):
            if math.sqrt(y):
                return math.sqrt(y)
            else:
                return math.sqrt(x)
        def exp(x,y):
            if math.exp(y):
                return math.exp(y)
            else:
                return math.exp(x)
        self.supported = {
            "+":lambda x,y: x+y,
            "-":lambda x,y: x-y,
            "*":lambda x,y: x*y,
            "/":lambda x,y: float(x)/float(y),
            "+/-":lambda x,y: -x,
            "%":lambda x,y: float(x * 100)/float(y),
            "log":lambda x,y: math.log(x),
            "exp":lambda x,y: exp(x,y),
            "cos":lambda x,y: math.cos(x),
            "sin":lambda x,y: math.sin(x),
            "tan":lambda x,y: math.tan(x),
            "acos":lambda x,y: math.acos(x),
            "asin":lambda x,y: math.asin(x),
            "atan":lambda x,y: math.atan(x),
            "pow":lambda x,y: math.pow(x,y),
            "sqrt":lambda x,y: sqrt(x,y)
        }
        self.clear()
