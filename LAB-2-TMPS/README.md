# LAB-2-TMPS

[**`Condiția lucrării de laborator nr.2`**](https://github.com/MihaiGaidau/TMPS-LABs/blob/9aeeeeb68abfb9d749f7b0c296fb914972139f86/Lab%232/README.md)

## Explicarea codului din fișierul `CreationalDesignPatterns.py`

Acest cod folosește două design pattern-uri:<br>
* Singleton Pattern<br>
* Factory Pattern

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
Astfel, Singleton Pattern este utilizat pentru a asigura că există o singură instanță a clasei `Calculator`, în timp ce Factory Pattern este utilizat pentru a crea instanțe ale clasei `Calculator` folosind metoda `create_calculator()` din clasa `CalculatorFactory`.

`Sigleton Pattern` și `Factory Pattern` sunt două modele de design utilizate în programare pentru a rezolva anumite probleme comune.

> Singleton Pattern:
> 
**Singleton Pattern** este un model de design care se asigură că o clasă are o singură instanță și oferă un punct global de acces la acea instanță. Scopul său principal este de a restricționa crearea de instanțe multiple ale unei clase și de a asigura că toate referințele la acea clasă se referă la aceeași instanță.

În codul dat, clasa `Calculator` utilizează Singleton Pattern pentru a se asigura că există o singură instanță a sa. Acest lucru este realizat prin utilizarea unei variabile de clasă `_instance` care reține instanța și prin suprascrierea metodei `__new__` pentru a returna întotdeauna aceeași instanță. Astfel, indiferent de câte instanțe ale clasei `Calculator` sunt create, întotdeauna se va referi la aceeași instanță.

> Factory Pattern:
> 
**Factory Pattern** este un model de design care furnizează o metodă de creare a obiectelor fără a expune logica de creare a acestora direct în codul client. În loc să utilizeze constructorii obișnuiți pentru a crea obiecte, Factory Pattern oferă o metodă separată, numită fabrică, pentru a crea și returna obiectele necesare.

În codul dat, clasa `CalculatorFactory` reprezintă o fabrică care are o singură responsabilitate: crearea de instanțe ale clasei `Calculator`. Aceasta oferă metoda `create_calculator()` care creează și returnează o nouă instanță a clasei `Calculator`. Prin utilizarea acestei fabrici, codul client nu trebuie să cunoască detaliile interne ale creării unei instanțe de `Calculator`, ci doar utilizează metoda fabricii pentru a obține o instanță pregătită. Acest lucru adaugă flexibilitate și ușurință în gestionarea creării obiectelor, permițând, de exemplu, schimbarea logică de creare a obiectelor fără a modifica codul client.
