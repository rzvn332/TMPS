# LAB-2-TMPS

[**`Condiția lucrării de laborator nr.2`**](https://github.com/MihaiGaidau/TMPS-LABs/blob/9aeeeeb68abfb9d749f7b0c296fb914972139f86/Lab%232/README.md)

## Explicarea codului din fișierul `CreationalDesignPatterns.py`

Acest cod folosește două design pattern-uri:

> Singleton Pattern :

Această implementare a clasei Calculator folosește `Singleton Pattern`, prin intermediul metodei `__new__`. Acest design pattern garantează că se va crea o singură instanță a clasei Calculator și această instanță va fi returnată de fiecare dată când se va încerca crearea unei noi instanțe. Prin urmare, există o singură instanță a Calculatorului în întreaga aplicație, ceea ce asigură o gestionare mai bună a resurselor.

> Factory Pattern :

Acest cod folosește `Factory Pattern` prin intermediul clasei `CalculatorFactory`. În loc să creați o instanță a Calculatorului direct prin intermediul constructorului, clasa `CalculatorFactory` oferă o metodă `create_calculator()` care creează și returnează o instanță nouă a Calculatorului. Prin urmare, codul este mai modular și mai ușor de întreținut, deoarece dacă ar fi necesar să se schimbe implementarea Calculatorului în viitor, modificarea ar fi necesară doar în clasa `Calculator` și în clasa `CalculatorFactory`.