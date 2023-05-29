# LAB-4-TMPS

[**`Condiția lucrării de laborator nr.4`**](https://github.com/MihaiGaidau/TMPS-LABs/blob/9aeeeeb68abfb9d749f7b0c296fb914972139f86/Lab%234/README.md)

## Explicarea codului din fișierul `BehavioralDesignPatterns.py`

Acest cod folosește două design pattern-uri:<br>
* Șablonul Command

În acest cod, există un șablon `Behavioral Design Pattern`, anume șablonul `Command`. Acesta este utilizat pentru a decupla comanda de acțiunea specifică pe care o execută. În cadrul acestui șablon, sunt definite următoarele secvențe de cod:

>> Definirea clasei de comandă de bază (Command):

```python
class Command:
    def execute(self):
        pass
```
Aceasta reprezintă clasa de bază pentru toate comenzile și conține o metodă abstractă, `execute()`, care va fi implementată în clasele derivate.

>> Definirea clasei de comandă de tăiere (CutCommand):

```python
class CutCommand(Command):
    def __init__(self, editor):
        self.editor = editor
        self.backup = None

    def execute(self):
        self.backup = self.editor.get_selection()
        self.editor.delete_selection()
```
Această clasă extinde clasa `Command` și implementează metoda `execute()`. Aici se realizează comanda de tăiere, unde se salvează o copie a selecției curente în variabila `backup` și se elimină selecția din editor.

---

`Sigleton Pattern` și `Factory Pattern` sunt două modele de design utilizate în programare pentru a rezolva anumite probleme comune.

> Singleton Pattern:
> 
**Singleton Pattern** este un model de design care se asigură că o clasă are o singură instanță și oferă un punct global de acces la acea instanță. Scopul său principal este de a restricționa crearea de instanțe multiple ale unei clase și de a asigura că toate referințele la acea clasă se referă la aceeași instanță.

În codul dat, clasa `Calculator` utilizează Singleton Pattern pentru a se asigura că există o singură instanță a sa. Acest lucru este realizat prin utilizarea unei variabile de clasă `_instance` care reține instanța și prin suprascrierea metodei `__new__` pentru a returna întotdeauna aceeași instanță. Astfel, indiferent de câte instanțe ale clasei `Calculator` sunt create, întotdeauna se va referi la aceeași instanță.

> Factory Pattern:
> 
**Factory Pattern** este un model de design care furnizează o metodă de creare a obiectelor fără a expune logica de creare a acestora direct în codul client. În loc să utilizeze constructorii obișnuiți pentru a crea obiecte, Factory Pattern oferă o metodă separată, numită fabrică, pentru a crea și returna obiectele necesare.

În codul dat, clasa `CalculatorFactory` reprezintă o fabrică care are o singură responsabilitate: crearea de instanțe ale clasei `Calculator`. Aceasta oferă metoda `create_calculator()` care creează și returnează o nouă instanță a clasei `Calculator`. Prin utilizarea acestei fabrici, codul client nu trebuie să cunoască detaliile interne ale creării unei instanțe de `Calculator`, ci doar utilizează metoda fabricii pentru a obține o instanță pregătită. Acest lucru adaugă flexibilitate și ușurință în gestionarea creării obiectelor, permițând, de exemplu, schimbarea logică de creare a obiectelor fără a modifica codul client.
