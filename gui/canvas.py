from tkinter import Tk, Canvas

canvas_width = 500
canvas_height = 500
dimensions = f'{canvas_width}x{canvas_height}'

root = Tk()
root.title('Cargo')
root.iconbitmap('gui/compass.ico')
root.geometry(dimensions)

canvas = Canvas(root, width=canvas_width, height=canvas_height, bg='#eae2cc')
canvas.pack()
