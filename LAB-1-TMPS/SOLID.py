class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Nu se poate împărți la zero")
        return a / b


if __name__ == '__main__':
    calc = Calculator()
    print("Calculator RZVN")
    while True:
        print("Alegeți o operațiune:")
        print("1. Adunare   (+)")
        print("2. Scădere   (-)")
        print("3. Înmulțire (*)")
        print("4. Împărțire (/)")
        print("5. Ieșire")
        choice = int(input())

        if choice == 1:
            a = int(input("Introduceți primul număr: "))
            b = int(input("Introduceți al doilea număr: "))
            print(f"{a} + {b} = {calc.add(a, b)}")
        elif choice == 2:
            a = int(input("Introduceți primul număr: "))
            b = int(input("Introduceți al doilea număr: "))
            print(f"{a} - {b} = {calc.subtract(a, b)}")
        elif choice == 3:
            a = int(input("Introduceți primul număr: "))
            b = int(input("Introduceți al doilea număr: "))
            print(f"{a} * {b} = {calc.multiply(a, b)}")
        elif choice == 4:
            a = int(input("Introduceți primul număr: "))
            b = int(input("Introduceți al doilea număr: "))
            try:
                print(f"{a} / {b} = {calc.divide(a, b)}")
            except ValueError as e:
                print(e)
        elif choice == 5:
            print("Vă mulțumim că ați folosit Calculatorul RZVN")
            break
        else:
            print("Alegere invalidă, vă rugăm să încercați din nou.")
