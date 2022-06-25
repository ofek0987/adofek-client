import tkinter.filedialog

from PIL import Image
from PIL import ImageTk


class MainForm:
    def __init__(self, window: tkinter.Tk):
        self.file_btn = None
        self.btn_send = None
        self.chat_entry = None
        self.win_width = 600
        self.win_height = 600
        self.main_frame = None
        self.window = window
        self.new_image = None
        self.bg_panel = None
        self.bg_image = None
        self.window.title('ADOFEK CHAT')
        self.window.geometry(f'{self.win_width}x{self.win_height}')
        self.window.resizable(False, False)

    def create_bg_layout(self):
        self.bg_image = Image.open('image projects\\bg_image.jpg')
        photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_panel = tkinter.Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand=1)

    def create_image_label(self):
        file = tkinter.filedialog.askopenfile(
            title='send file',
            typevariable='all files',
        )
        self.new_image = Image.open(file.name)

    def create_frame_layer(self):
        self.main_frame = tkinter.Frame(
            self.window, bg='blue', width=self.win_width - 80,
            height=self.win_height - 80,
        )
        self.main_frame.place(x=40, y=40)

    def create_text_entry(self):
        self.chat_entry = tkinter.Entry(
            self.main_frame, width='30',
            borderwidth='3', font='none 10 bold', justify='center',
            highlightthickness=5, highlightcolor='green',
        )
        self.chat_entry.place(x=150, y=450)
        self.btn_send = tkinter.Button(
            self.main_frame, text='Send', font='none 12 bold',
            bg='green', highlightcolor='white',
            highlightthickness=5,
        )
        self.btn_send.place(x=400, y=450)
        self.file_btn = tkinter.Button(
            self.main_frame, text='add file', font='none 12 bold',
            bg='green', highlightcolor='white',
            highlightthickness=5, command=self.create_image_label,
        )
        self.file_btn.place(x=60, y=450)
