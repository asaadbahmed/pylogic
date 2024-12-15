from pathlib import Path
from tkinter import *
from tkinter import ttk
import gates

# TODO - add expression evaluating & minimizing (convert to NANDS using DeMorgans for least possible transistors)
app = Tk()
app.title("Pylogic v1.0") # use semantic versioning
app.geometry("659x409")
app.configure(bg = "#FFFFFF")

canvas = Canvas(
    app,
    bg = "#FFFFFF",
    height = 409,
    width = 659,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    659.0,
    409.0,
    fill="#1E1E1E",
    outline="")

canvas.create_text(
    368.0,
    92.0,
    anchor="nw",
    text="Design",
    fill="#FFA629",
    font=("SegoeUI", 20)
)

canvas.create_text(
    57.0,
    92.0,
    anchor="nw",
    text="Gates",
    fill="#FFA629",
    font=("SegoeUI", 20)
)

background = PhotoImage(file="./assets/frame0/image_1.png") #file=relative_to_assets("image_1.png")
background_image = canvas.create_image(
    329.0,
    40.0,
    image=background
)

canvas.create_rectangle(
    179.0,
    122.0,
    624.0,
    382.0,
    fill="#2E2E2E",
    outline="")

canvas.create_rectangle(
    30.0,
    122.0,
    140.0,
    382.0,
    fill="#2E2E2E",
    outline="")
app.resizable(False, False)
app.mainloop()

"""
app = Tk()
app.title("Pylogic v1.0") # use semantic versioning
app.geometry("1200x800")

gatesFrame = Canvas(app, width=200, height=600, bg="black")
gatesFrame.pack(anchor="w", padx=50, pady=60)

# gatesLabel = Label(app, text="Gates", font=("SegoeUI", 20))
# gatesLabel.pack(anchor="nw")

app.mainloop()
"""