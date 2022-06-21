import tkinter
from PIL import ImageTk,Image


class MainForm:
    def __init__(self, window: tkinter.Tk):
        self.bg_panel = None
        self.bg_image = None
        window.title("ADOFEK CHAT")
        window.geometry("600x600")

    def create_bg_layout(self):
        self.bg_image = Image.open("image projects\\bg_image.jpg")
        photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_panel = tkinter.Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill="both", expand=1)