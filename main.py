from PIL import Image
from tkinter import *


def main():
    # create the canvas, size in pixels
    canvas = Canvas(width=300, height=200, bg='black')

    # pack the canvas into a frame/form
    canvas.pack(expand=YES, fill=BOTH)

    # load the .gif image file
    gif1 = PhotoImage(file='hiclipart.com.png')

    # put gif image on canvas
    # pic's upper left corner (NW) on the canvas is at x=50 y=10
    canvas.create_image(50, 10, image=gif1, anchor=NW)

    # run it ...
    mainloop()


if __name__ == "__main__":
    main()
