import tkinter as tk

# Clasa de comandă de bază
class Command:
    def execute(self):
        pass

# Comanda de tăiere
class CutCommand(Command):
    def __init__(self, editor):
        self.editor = editor
        self.backup = None

    def execute(self):
        self.backup = self.editor.get_selection()
        self.editor.delete_selection()

# Comanda de copiere
class CopyCommand(Command):
    def __init__(self, editor):
        self.editor = editor

    def execute(self):
        self.editor.copy_selection()

# Comanda de lipire
class PasteCommand(Command):
    def __init__(self, editor):
        self.editor = editor
        self.backup = None

    def execute(self):
        self.backup = self.editor.get_selection()
        self.editor.insert_from_clipboard()

# Editorul de text
class TextEditor(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.text = tk.Text(self)
        self.text.pack()

        self.button_frame = tk.Frame(self)
        self.button_frame.pack()

        self.cut_button = tk.Button(self.button_frame, text="Tăiere", command=self.cut)
        self.cut_button.pack(side="left", padx=5, pady=5)

        self.copy_button = tk.Button(self.button_frame, text="Copiere", command=self.copy)
        self.copy_button.pack(side="left", padx=5, pady=5)

        self.paste_button = tk.Button(self.button_frame, text="Lipire", command=self.paste)
        self.paste_button.pack(side="left", padx=5, pady=5)

        self.clipboard = ""

    def get_selection(self):
        return self.text.selection_get()

    def delete_selection(self):
        self.text.delete("sel.first", "sel.last")

    def copy_selection(self):
        self.clipboard = self.get_selection()

    def insert_from_clipboard(self):
        self.text.insert("insert", self.clipboard)

    def cut(self):
        cut_command = CutCommand(self)
        cut_command.execute()

    def copy(self):
        copy_command = CopyCommand(self)
        copy_command.execute()

    def paste(self):
        paste_command = PasteCommand(self)
        paste_command.execute()

# Crearea ferestrei principale
root = tk.Tk()
root.title("Editor de text")

# Crearea editorului de text
text_editor = TextEditor(master=root)

# Rularea buclei principale a aplicației
text_editor.mainloop()
