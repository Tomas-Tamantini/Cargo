from tkinter import Tk, Canvas

from gui.colors import background_color

canvas_width = 1000
canvas_height = 700
dimensions = f'{canvas_width}x{canvas_height}'

root = Tk()
root.title('Cargo')
root.iconbitmap('gui/compass.ico')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
screen_x = int(screen_width / 2 - canvas_width / 2)
screen_y = int(screen_height / 2 - canvas_height / 2)

root.geometry(f'{canvas_width}x{canvas_height}+{screen_x}+{screen_y}')

canvas = Canvas(root, width=canvas_width, height=canvas_height, bg=background_color)
canvas.pack()
