# LAB-4-TMPS

[**`Condiția lucrării de laborator nr.4`**](https://github.com/MihaiGaidau/TMPS-LABs/blob/9aeeeeb68abfb9d749f7b0c296fb914972139f86/Lab%234/README.md)

## Explicarea codului din fișierul `BehavioralDesignPatterns.py`

Acest cod folosește două design pattern-uri:<br>
* Șablonul Command

În acest cod, există un șablon `Behavioral Design Pattern`, anume șablonul `Command`. Acesta este utilizat pentru a decupla comanda de acțiunea specifică pe care o execută. În cadrul acestui șablon, sunt definite următoarele secvențe de cod:

> Definirea clasei de comandă de bază (Command):

```python
class Command:
    def execute(self):
        pass
```
Aceasta reprezintă clasa de bază pentru toate comenzile și conține o metodă abstractă, `execute()`, care va fi implementată în clasele derivate.

> Definirea clasei de comandă de tăiere (CutCommand):

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

> Definirea clasei de comandă de copiere (CopyCommand):

```python
class CopyCommand(Command):
    def __init__(self, editor):
        self.editor = editor

    def execute(self):
        self.editor.copy_selection()
```

Această clasă extinde clasa `Command` și implementează metoda `execute()`. Aici se realizează comanda de copiere a selecției curente în editor.

> Definirea clasei de comandă de lipire (PasteCommand):

```python
class PasteCommand(Command):
    def __init__(self, editor):
        self.editor = editor
        self.backup = None

    def execute(self):
        self.backup = self.editor.get_selection()
        self.editor.insert_from_clipboard()
```

Această clasă extinde clasa `Command` și implementează metoda `execute()`. Aici se realizează comanda de lipire a conținutului din clipboard în editor, salvându-se în același timp o copie a selecției curente în variabila `backup`.

---

> Definirea clasei de editor de text (TextEditor):

```python
class TextEditor(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        # Codul pentru crearea interfeței grafice

    # Metode pentru manipularea textului și interacțiunea cu comenzile

    def cut(self):
        cut_command = CutCommand(self)
        cut_command.execute()

    def copy(self):
        copy_command = CopyCommand(self)
        copy_command.execute()

    def paste(self):
        paste_command = PasteCommand(self)
        paste_command.execute()
```

Aceasta reprezintă clasa de editor de text, care acționează ca invocator pentru comenzile de tăiere, copiere și lipire. În metodele `cut()`, `copy()` și `paste()`, se creează obiecte de comandă corespunzătoare și se apelează metoda execute() pentru fiecare comandă.

---

`ScreenShot` :arrow_down: :arrow_down: :arrow_down:

![My Remote Image](https://github.com/rzvn332/TMPS/blob/debec02a03fd0e189d70c5d6fcdfb864b26c499d/LAB-3-TMPS/ScreenShot/all_screenshot.png)
