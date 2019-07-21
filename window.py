import tkinter as tk
import sys


class Window():
    def __init__(self, title, size):
        self.title = title
        self.size = size

        self.root = tk.Tk()
        self.root.title(self.title)
        self.root.geometry(self.size)

        """Ustawienie na środku ekranu oraz ikonka."""
        self.root.protocol("WM_DELETE_WINDOW", lambda: sys.exit())
        self.root.tk.call('wm', 'iconphoto', self.root._w,
                          tk.PhotoImage(file='pliki/ikona.gif'))
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        self.create_frames()

        self.root.mainloop()  # główny loop

    def create_frames(self):
        pass
