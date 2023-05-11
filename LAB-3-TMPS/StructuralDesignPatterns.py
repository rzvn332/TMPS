class Operation:
    def execute(self, a, b):
        pass

class Add(Operation):
    def execute(self, a, b):
        return a + b

    def get_operation_symbol(self):
        return '+'

class Subtract(Operation):
    def execute(self, a, b):
        return a - b

    def get_operation_symbol(self):
        return '-'

class Multiply(Operation):
    def execute(self, a, b):
        return a * b

    def get_operation_symbol(self):
        return '*'

class Divide(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Nu se poate împărți la zero")
        return a / b

    def get_operation_symbol(self):
        return '/'

class OperationDecorator(Operation):
    def __init__(self, operation):
        self.operation = operation
        self.history = []

    def execute(self, a, b):
        result = self.operation.execute(a, b)
        operation_str = f"{a} {self.operation.get_operation_symbol()} {b} = {result}"
        self.history.append(operation_str)
        return result

    def get_operation_symbol(self):
        return self.operation.get_operation_symbol()

class Calculator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.operations = {
            '+': OperationDecorator(Add()),
            '-': OperationDecorator(Subtract()),
            '*': OperationDecorator(Multiply()),
            '/': OperationDecorator(Divide())
        }

    def compute(self, a, b, op):
        operation = self.operations[op]
        result = operation.execute(a, b)
        print(f"{a} {op} {b} = {result}")
        print(">------------------------<")
        return result

    def print_history(self):
        print("Istoricul operațiilor:")
        for operation in self.operations.values():
            for op in operation.history:
                print(op)
        print(">------------------------<")


class CalculatorFacade:
    def __init__(self, calculator):
        self.calculator = calculator

    def compute_average(self, numbers):
        total = sum(numbers)
        avg = total / len(numbers)
        return avg

    def compute_power(self, base, exponent):
        return base ** exponent


class CalculatorFactory:
    def create_calculator(self):
        return Calculator()


if __name__ == '__main__':
    calc_factory = CalculatorFactory()
    calc = calc_factory.create_calculator()
    facade = CalculatorFacade(calc)

    print("Calculator RZVN")
    while True:
        print("Alegeți o operațiune:")
        print("1. Adunare   (+)")
        print("2. Scădere   (-)")
        print("3. Înmulțire (*)")
        print("4. Împărțire (/)")
        print("5. Ieșire")
        print("6. Calculul mediei")
        print("7. Ridicarea la putere")
        print("8. Afișare istoric operații")
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
        elif choice == 6:
            num_count = int(input("Introduceți numărul de valori: "))
            numbers = []
            for i in range(num_count):
                num = int(input(f"Introduceți valoarea {i + 1}: "))
                numbers.append(num)
            avg = facade.compute_average(numbers)
            print("Media este:", avg)
        elif choice == 7:
            base = int(input("Introduceți baza: "))
            exponent = int(input("Introduceți exponentul: "))
            power = facade.compute_power(base, exponent)
            print(f"{base} ridicat la puterea {exponent} este:", power)
        elif choice == 8:
            calc.print_history()
        else:
            print("Alegere invalidă, vă rugăm să încercați din nou.")

