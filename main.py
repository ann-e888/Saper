from tkinter import *
import time
import settings
import utils
from cell import Cell

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
    root.after(1000, measure_time, root, timer)

timer = Label(
    root, 
    bg = 'LightSkyBlue1', 
    fg = 'midnightblue', 
    font = ('Digital-7', 40)
)
timer.place(x=310, y=10)

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