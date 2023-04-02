# LAB-1-TMPS
[**`Condiția lucrării de laborator nr.1`**](https://github.com/MihaiGaidau/TMPS-LABs/blob/main/Lab%231/README.md)

## Explicarea codului din fișierul `SOLID.py`
1. Principiul responsabilității unice **(Single Responsibility Principle)**: Clasa `Calculator` are o singură responsabilitate, aceea de a efectua operații matematice. Această responsabilitate este îndeplinită de cele patru metode ale clasei.

2. Principiul deschis-închis **(Open-Closed Principle)**: Clasa `Calculator` este deschisă pentru extensii (adăugarea de noi operații), dar închisă pentru modificări. Dacă dorim să adăugăm o nouă operație, putem crea o nouă metodă în clasa `Calculator`, fără a modifica codul existent.

3. Principiul substituției Liskov **(Liskov Substitution Principle)**: Clasa `Calculator` nu extinde nicio altă clasă, dar poate fi folosită în locul unei clase de bază. Astfel, dacă avem o altă clasă care folosește un calculator, putem înlocui instanța clasei `Calculator` cu o altă clasă care extinde clasa `Calculator` fără a afecta comportamentul programului.

4. Principiul segregării interfețelor **(Interface Segregation Principle)**: Clasa `Calculator` nu implementează nicio interfață, dar metodele sale sunt bine delimitate și îndeplinesc funcționalități distincte.

5. Principiul inversiunii dependențelor **(Dependency Inversion Principle)**: Clasa `Calculator` nu depinde de alte clase, ci este independentă. Această clasă poate fi folosită de alte clase fără a fi necesară modificarea codului existent.
