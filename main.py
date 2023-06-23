from tkinter import *
from tkinter import messagebox
import time
import settings
import utils
from cell import Cell
from scoreboard import ScoreSave
from scorewindow import ScoresWindow

root = Tk()

#Ustawienia okna
root.configure(bg='SteelBlue4')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Saper")
root.resizable(False, False)

#Inicjalizacja i rozmieszczenie frameów
top_frame = Frame(
    root,
    bg='SteelBlue4',
    width=settings.WIDTH,
    height=utils.height_prct(20 )
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='SteelBlue4',
    width=utils.width_prct(20),
    height=utils.height_prct(80)
)
left_frame.place(x=0, y=utils.height_prct(20))

center_frame = Frame(
    root,
    bg='SteelBlue4',
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)
center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25)
)

def measure_time(root, timer): 
    hours = settings.TIME // 3600
    minutes = (settings.TIME % 3600) // 60
    seconds = settings.TIME % 60
    time_string = f'{hours:02d}:{minutes:02d}:{seconds:02d}'
    timer['text'] = time_string
    settings.TIME += 1
    settings.time_elapsed = settings.TIME
    root.after(1000, measure_time, root, timer)

timer = Label(
    root, 
    bg = 'LightSkyBlue1', 
    fg = 'midnightblue', 
    font = ('Digital-7', 40)
)
timer.place(x=310, y=10)

def show_scores():
    scoreboard = ScoreSave('scores.txt')
    scores = scoreboard.load_scores()

    if scores is not None:
        scores_window = ScoresWindow(scores)


scores_button = Button(
    left_frame,
    width=12,
    height=4,
    font=('',15),
    text="Scores",
    command=show_scores,
    bd=0,
    bg='LightSkyBlue1',
    activebackground='LightSkyBlue4'
)
scores_button.place(x=10, y=150)

#Tworzenie komórek
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_obj(center_frame)
        c.cell_button_obj.grid(
            column=x,
            row=y
        )

#Wywołanie lbl z klasy Cell
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=10, y=30)

   
Cell.set_mines()
measure_time(root, timer)

root.mainloop()