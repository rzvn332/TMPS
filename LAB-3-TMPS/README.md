# LAB-3-TMPS

[**`Condiția lucrării de laborator nr.3`**](https://github.com/MihaiGaidau/TMPS-LABs/tree/9aeeeeb68abfb9d749f7b0c296fb914972139f86/Lab%233)

## Explicarea codului din fișierul `StructuralDesignPatterns.py`

În codul din `StructuralDesignPatterns.py`, au fost utilizate două pattern-uri de design structural: **Decorator** și **Facade**.<br> Iată cum au fost aplicate și ce funcționalitate nouă au adus:

`Decorator:`

```python
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
```

> Pattern-ul Decorator a fost utilizat pentru a înconjura obiectele de tip operație (`Operation`) cu un decorator (`OperationDecorator`). Acest decorator adaugă funcționalitatea de înregistrare a operațiilor în istoric. Astfel, fiecare operație este înconjurată de decorator, care înregistrează operația și adaugă rezultatul în istoric. Acesta extinde funcționalitatea de bază a operațiilor și le oferă capacitatea de a înregistra istoricul operațiilor efectuate.

`Facade:`

```python
class CalculatorFacade:
    def __init__(self, calculator):
        self.calculator = calculator

    def compute_average(self, numbers):
        total = sum(numbers)
        avg = total / len(numbers)
        return avg

    def compute_power(self, base, exponent):
        return base ** exponent
```

> Pattern-ul Facade este utilizat pentru a oferi o interfață simplificată și unificată către anumite funcționalități complexe ale calculatorului. Clasa `CalculatorFacade` acționează ca o interfață de nivel înalt pentru a efectua operații precum calculul mediei sau ridicarea la putere. Aceasta ascunde detaliile complexe ale operațiilor individuale și oferă o interfață mai prietenoasă utilizatorului pentru a accesa aceste funcționalități avansate. Acesta adaugă un nivel de abstractizare și separă logica complexă în spatele unei interfețe mai simple.

Prin utilizarea pattern-urilor Decorator și Facade, s-a adăugat funcționalitate nouă la calculator, inclusiv înregistrarea istoricului operațiilor și accesul facil la funcționalitățile avansate (calculul mediei și ridicarea la putere) prin intermediul facade-ului. Aceste pattern-uri contribuie la modularizarea și extensibilitatea codului, permițând adăugarea ușoară a altor funcționalități în viitor fără a afecta structura existentă.

---

`ScreenShot` :arrow_down: :arrow_down: :arrow_down:

![alt text](http://url/to/img.png)
