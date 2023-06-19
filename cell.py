from tkinter import Button, Label, messagebox
from scoreboard import Scoreboard
import random
import settings
import ctypes
import sys
import time

scoreboard = Scoreboard('scores.txt')

class Cell:
    mines = []
    cell_count = settings.CELL_COUNTER
    cell_count_label_object = None

    def __init__(self, x, y, is_mine=False):
        self.x = x
        self.y = y
        self.is_mine = is_mine
        self.is_potential_mine = False
        self.is_opened = False
        self.cell_button_obj = None
        Cell.mines.append(self)

    def create_btn_obj(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
        )
        btn.bind('<Button-1>', self.left_click)
        btn.bind('<Button-3>', self.right_click)
        self.cell_button_obj = btn

    #Wyświetlanie liczby pozostałych komórek
    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            width=12,
            height=4,
            font=('',15),
            text=f'Cells left: {Cell.cell_count}'
        )
        Cell.cell_count_label_object = lbl

    def left_click(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounding_cells_mines == 0:
                for item in self.surrounding_cells:
                    item.show_neighbours()
            self.show_neighbours()
            #Liczba komórek == Liczba min ==> Wygrana
            if Cell.cell_count == settings.MINES_COUNT:
                self.cell_button_obj.after(500, self.display_win_message)

    def display_win_message(self):
        ctypes.windll.user32.MessageBoxW(0, 'Congratulations, you won!', 'Game Over', 0)
        name = input("Enter your name: ")  
        time_elapsed = time.time() - settings.TIME  
        scoreboard.add_score(name, time_elapsed)
        sys.exit()

        #Po otwarciu komórki blokuję możliwość kliknięć
        self.cell_button_obj.unbind('<Button-1>')
        self.cell_button_obj.unbind('<Button-3>')

    def show_cell_axis(self, x, y):
        for cell in Cell.mines:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounding_cells(self):
        cells= [
            self.show_cell_axis(self.x - 1, self.y - 1),
            self.show_cell_axis(self.x - 1, self.y),
            self.show_cell_axis(self.x - 1, self.y + 2),
            self.show_cell_axis(self.x, self.y - 1),
            self.show_cell_axis(self.x + 1, self.y - 1),
            self.show_cell_axis(self.x + 1, self.y),
            self.show_cell_axis(self.x + 1, self.y + 1),
            self.show_cell_axis(self.x, self.y + 1),
        ]

        cells = [cell for cell in cells if cell is not None]
        return cells
    
    def show_neighbours(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_button_obj.configure(
                text=self.surrounding_cells_mines,
                #font = ('', 13)
            )
            #Aktualizacja lbl po odkryciu nowej komórki
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f'Cells left: {Cell.cell_count}'
                )
            self.cell_button_obj.configure(
                bg='SystemButtonFace'
            )
        self.is_opened = True

    @property 
    def surrounding_cells_mines(self):
        counter = 0
        for cell in self.surrounding_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_mine(self):
        self.cell_button_obj.configure(bg='red')
        self.cell_button_obj.after(500, self.display_game_over_message)
        
    
    def display_game_over_message(self):
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine!', 'Game Over', 0)
        sys.exit()

    def right_click(self, event):
        if not self.is_potential_mine:
            self.cell_button_obj.configure(
               bg='orange' 
            )
            self.is_potential_mine = True
        else:
            self.cell_button_obj.configure(
                bg='SystemButtonFace'
            )
            self.is_potential_mine = False

    @staticmethod
    def set_mines():
        picked_cells = random.sample(
            Cell.mines, settings.MINES_COUNT
        )
        for item in picked_cells:
            item.is_mine = True
        print(picked_cells)

    def __repr__(self):
        return f'Cell({self.x}, {self.y})'
