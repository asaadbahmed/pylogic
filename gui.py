from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/asaadahmed/Downloads/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("659x409")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
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
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    57.0,
    92.0,
    anchor="nw",
    text="Gates",
    fill="#FFA629",
    font=("Inter Bold", 20 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    329.0,
    40.0,
    image=image_image_1
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
window.resizable(False, False)
window.mainloop()
