# LAB-2-TMPS

[**`Condiția lucrării de laborator nr.2`**](https://github.com/MihaiGaidau/TMPS-LABs/blob/9aeeeeb68abfb9d749f7b0c296fb914972139f86/Lab%232/README.md)

## Explicarea codului din fișierul `CreationalDesignPatterns.py`

Acest cod folosește două design pattern-uri:
1.Singleton Pattern
2.Factory Pattern

În codul dat, Singleton Pattern este utilizat în clasa `Calculator`, în secțiunea marcată cu comentarii `# Add initialization code here`. Iată secțiunea respectivă a codului:

```python
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

    # Restul codului...
```

Factory Pattern este utilizat în clasa `CalculatorFactory`, în metoda `create_calculator()`. Iată secțiunea respectivă a codului:

```python
class CalculatorFactory:
    def create_calculator(self):
        return Calculator()

# Restul codului...
```
