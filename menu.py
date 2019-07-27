# -*- coding: utf-8 -*-
'''Okno menu.'''
from window import Window  # klasa okna
import tkinter as tk
from config import konsultant, font10


class Menu(Window):

    def menu_button(self, wybor):
        konsultant.menu(wybor)
        self.root.destroy()

    def widgets(self):
        '''Widgety, zmienić na self?'''
        page_frame = tk.Frame(self.root)

        #  Informacja kto zalogowany
        zalog_label = tk.Label(page_frame, text='Zalogowany jako:')
        zalog_label.pack()
        kons_label = tk.Label(page_frame, text=konsultant.kto,
                              font=font10, fg='green')
        kons_label.pack()

        # Przycisk umowa
        umowa = tk.Button(page_frame, text='Umowa', font=font10,
                          height=2, width=18,
                          command=lambda: self.menu_button(1))
        umowa.pack()

        # Przycisk sprawy nierozwiązane
        sprawy = tk.Button(page_frame, text='Sprawy nierozwiązane',
                           font=font10, height=2, width=18,
                           command=lambda: self.menu_button(2))
        sprawy.pack()

        # Przycisk aneks
        aneks = tk.Button(page_frame, text='Aneks', font=font10,
                          height=2, width=18,
                          command=lambda: self.menu_button(3))
        aneks.pack()

        # Przycisk wypowiedzenie
        wypo = tk.Button(page_frame, text='Wypowiedzenie', font=font10,
                         height=2, width=18,
                         command=lambda: self.menu_button(4))
        wypo.pack()

        page_frame.pack()
