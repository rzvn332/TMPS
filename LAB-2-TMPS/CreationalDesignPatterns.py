class Operation:
    def execute(self, a, b):
        pass

class Add(Operation):
    def execute(self, a, b):
        return a + b

class Subtract(Operation):
    def execute(self, a, b):
        return a - b

class Multiply(Operation):
    def execute(self, a, b):
        return a * b

class Divide(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Nu se poate împărți la zero")
        return a / b

class Calculator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Add initialization code here
        return cls._instance

    def __init__(self):
        self.operations = {
            '+': Add(),
            '-': Subtract(),
            '*': Multiply(),
            '/': Divide()
        }

    def compute(self, a, b, op):
        operation = self.operations[op]
        result = operation.execute(a, b)
        print(f"{a} {op} {b} = {result}")
        print(">------------------------<")
        return result

class CalculatorFactory:
    def create_calculator(self):
        return Calculator()

if __name__ == '__main__':
    calc_factory = CalculatorFactory()
    calc = calc_factory.create_calculator()
    print("Calculator RZVN")
    while True:
        print("Alegeți o operațiune:")
        print("1. Adunare   (+)")
        print("2. Scădere   (-)")
        print("3. Înmulțire (*)")
        print("4. Împărțire (/)")
        print("5. Ieșire")
        print(">------------------------<")
        choice = int(input())

        if choice == 1:
            a = int(input("Introduceți primul număr: "))
            b = int(input("Introduceți al doilea număr: "))
            calc.compute(a, b, '+')
        elif choice == 2:
            a = int(input("Introduceți primul număr: "))
            b = int(input("Introduceți al doilea număr: "))
            calc.compute(a, b, '-')
        elif choice == 3:
            a = int(input("Introduceți primul număr: "))
            b = int(input("Introduceți al doilea număr: "))
            calc.compute(a, b, '*')
        elif choice == 4:
            a = int(input("Introduceți primul număr: "))
            b = int(input("Introduceți al doilea număr: "))
            try:
                calc.compute(a, b, '/')
            except ValueError as e:
                print(e)
        elif choice == 5:
            print("Vă mulțumim că ați folosit Calculatorul RZVN")
            break
        else:
            print("Alegere invalidă, vă rugăm să încercați din nou.")
