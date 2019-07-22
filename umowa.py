from window import Window
import tkinter as tk
from pracownik import konsultant

class Umowa(Window):

    def widgets(self):
        page_frame = tk.Frame(self.root)

        left_frame = tk.Frame(page_frame, width=100, height=200, bg='red')
        right_frame = tk.Frame(page_frame, width=100, height=200, bg='blue')
        left_frame.pack(side=tk.RIGHT)
        right_frame.pack(side=tk.LEFT)

        #  Informacja kto zalogowany
        zalog_label = tk.Label(page_frame, text='Zalogowany jako:')
        zalog_label.pack()
        kons_label = tk.Label(page_frame, text=konsultant.kto,
                                font=('Arial 800', 10), fg='green')
        kons_label.pack()



        page_frame.pack()
