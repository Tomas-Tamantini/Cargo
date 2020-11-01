from tkinter import Tk, Canvas

root = Tk()
root.title('Cargo')
root.iconbitmap('gui/compass.ico')
root.geometry('500x500')

canvas_width = 500
canvas_height = 500
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg='#eae2cc')
canvas.pack()
