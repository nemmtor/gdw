'''Okno menu. Aneks i wypowiedzenie do zrobienia później.'''
from window import Window  # klasa okna
import tkinter as tk
from config import font10, version, goldwin, img_resizer
from PIL import ImageTk


# Obiekty
from konsultant import konsultant


class Menu(Window):

    # Funkcje przycisków:
    def menu_button(self, wybor):
        '''Wybór menu, następnie usunięcie okna menu.'''
        konsultant.menu(wybor)
        self.root.destroy()

    def widgets(self):
        '''Widgety'''

        # Główny frame
        page_frame = tk.Frame(self.root)
        img_frame = tk.Frame(self.root)

        # img_frame widgets

        img = ImageTk.PhotoImage(img_resizer(goldwin, 0.5))
        img_Label = tk.Label(img_frame, image=img)
        img_Label.image = img
        img_Label.pack()

        # Informacja kto zalogowany
        # Label
        wersja_label = tk.Label(page_frame, text=f'Wersja {version}',
                                font=font10, fg='green')
        zalog_label = tk.Label(page_frame, text='Zalogowano jako:')
        # Label z imieniem i nazwiskiem
        kons_label = tk.Label(page_frame, text=konsultant.kto,
                              font=font10, fg='green')

        # Przycisk umowa
        umowa = tk.Button(page_frame, text='Umowa', font=font10,
                          height=2, width=20, padx=5,
                          command=lambda: self.menu_button(1))

        # # Przycisk sprawy nierozwiązane
        # sprawy = tk.Button(page_frame, text='Sprawy nierozwiązane',
        #                    font=font10, height=2, width=18,
        #                    command=lambda: self.menu_button(2))

        # Przycisk aneks
        # aneks = tk.Button(page_frame, text='Aneks', font=font10,
        #                   height=2, width=18,
        #                   command=lambda: self.menu_button(2))
        #
        # # Przycisk wypowiedzenie
        # wypo = tk.Button(page_frame, text='Wypowiedzenie', font=font10,
        #                  height=2, width=18,
        #                  command=lambda: self.menu_button(3))

        # Przycisk Mail z ofertą
        oferta = tk.Button(page_frame, text='Mail z ofertą', font=font10,
                           height=2, width=20, padx=5,
                           command=lambda: self.menu_button(4))

        rodo_skrypt = tk.Button(page_frame, text='Mail informacyjny RODO',
                                font=font10, height=2, width=20, padx=5,
                                command=lambda: self.menu_button(5))

        # Pack
        zalog_label.pack()
        kons_label.pack(pady=(0, 10))
        umowa.pack(pady=(0,5))
        # aneks.pack()
        # wypo.pack()
        oferta.pack(pady=(0,5))
        rodo_skrypt.pack(pady=(0,5))
        wersja_label.pack(pady=(5, 0))
        page_frame.pack(side=tk.LEFT, padx=(20,0))
        img_frame.pack(side=tk.LEFT)

if __name__ == '__main__':
    konsultant.kto = 'Developer ON'
    menu = Menu('Goldwin Mailsender')
