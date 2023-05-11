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
