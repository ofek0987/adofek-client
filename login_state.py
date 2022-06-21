from dataclasses import dataclass
import tkinter
from PIL import ImageTk, Image


class LoginWindow:
    """Create and init sign in form."""

    def __init__(self, window):
        self.show_icon_panel = None
        self.hide_icon_panel = None
        self.hide_icon = None
        self.forget_pass_btn = None
        self.login_button = None
        self.lgn_icon_panel = None
        self.login_btn = None
        self.password_icon = None
        self.password_icon_panel = None
        self.password_line = None
        self.password_entry = None
        self.password_txt = None
        self.username_icon_panel = None
        self.username_icon = None
        self.username_line = None
        self.username_entry = None
        self.username_txt = None
        self.sign_image = None
        self.show_icon = None
        self.sign_in_txt = None
        self.sign_panel = None
        self.bg_logo = None
        self.heading = None
        self.login_frame = None
        self.txt = None
        self.bg_panel = None
        self.bg_image = None
        self.window = window
        self.window.geometry("1000x700")
        self.window.state("zoomed")
        self.window.resizable(0, 0)
        self.window.title("Login Form")

    def create_background(self):
        self.bg_image = Image.open("image projects\\bg_image.jpg")
        photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_panel = tkinter.Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill="both", expand=1)

    def create_frame_layer(self):
        self.login_frame = tkinter.Frame(self.window, bg="blue", width=950, height=600)
        self.login_frame.place(x=200, y=70)
        self.txt = "WELCOME"
        self.heading = tkinter.Label(self.login_frame, text=self.txt, font=("yu gothic ui", 25, "bold"), fg="white",
                                     bg="blue")
        self.heading.place(x=80, y=50, width=300, height=30)

    def create_logo(self):
        self.bg_logo = Image.open("image projects\\log.png")
        photo = ImageTk.PhotoImage(self.bg_logo)
        self.bg_logo = tkinter.Label(self.login_frame, image=photo, bg="blue")
        self.bg_logo.image = photo
        self.bg_logo.place(x=50, y=160)

    def create_sign_in_layer(self):
        self.sign_image = Image.open("image projects\\images\\hyy.png")
        photo = ImageTk.PhotoImage(self.sign_image)
        self.sign_panel = tkinter.Label(self.login_frame, image=photo, bg="blue")
        self.sign_panel.image = photo
        self.sign_panel.place(x=700, y=30)
        self.sign_in_txt = tkinter.Label(self.login_frame, text="Sign In", font=("yu gothic ui", 18, "bold"),
                                         fg="white", bg="blue")
        self.sign_in_txt.place(x=730, y=150)

    def create_username_input(self):
        self.username_txt = tkinter.Label(self.login_frame, text="Username", font=("yu gothic ui", 15, "bold"),
                                          fg="black", bg="blue")
        self.username_txt.place(x=650, y=220)
        self.username_entry = tkinter.Entry(self.login_frame, highlightthickness=0, relief=tkinter.FLAT, width=25
                                            , font=("yu gothic ui", 13, "bold"), fg="black", bg="blue")
        self.username_entry.place(x=680, y=250)
        self.username_line = tkinter.Canvas(self.login_frame, width=250, height=2.0,
                                            bg="white", highlightthickness=0)
        self.username_line.place(x=660, y=280)

    def create_username_logo(self):
        self.username_icon = Image.open("image projects\\images\\username_icon.png")
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_panel = tkinter.Label(self.login_frame, image=photo, bg="blue")
        self.username_icon_panel.image = photo
        self.username_icon_panel.place(x=650, y=250)

    def create_password_input(self):
        self.password_txt = tkinter.Label(self.login_frame, text="Password", font=("yu gothic ui", 15, "bold"),
                                          fg="black", bg="blue")
        self.password_txt.place(x=650, y=320)
        self.password_entry = tkinter.Entry(self.login_frame, highlightthickness=0, relief=tkinter.FLAT, width=25
                                            , font=("yu gothic ui", 13, "bold"), fg="black", bg="blue", )
        self.password_entry.place(x=680, y=350)
        self.password_line = tkinter.Canvas(self.login_frame, width=250, height=2.0,
                                            bg="white", highlightthickness=0)
        self.password_line.place(x=660, y=380)

    def create_password_logo(self):
        self.password_icon = Image.open("image projects\\images\\password_icon.png")
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_panel = tkinter.Label(self.login_frame, image=photo, bg="blue")
        self.password_icon_panel.image = photo
        self.password_icon_panel.place(x=650, y=350)

    def create_login_button(self):
        self.login_btn = Image.open("image projects\\images\\btn1.png")
        photo = ImageTk.PhotoImage(self.login_btn)
        self.lgn_icon_panel = tkinter.Label(self.login_frame, image=photo, bg="blue")
        self.lgn_icon_panel.image = photo
        self.lgn_icon_panel.place(x=640, y=400)

        self.login_button = tkinter.Button(self.lgn_icon_panel, text="L O G   I N", font=("yu gothic ui", 13, "bold"),
                                           width=25, bd=0, bg="#3047ff", cursor="hand2", activebackground="#3047ff"
                                           , fg="white")
        self.login_button.place(x=20, y=10)

    def create_password_show_or_hide_button(self):
        self.hide_icon = Image.open("image projects\\images\\hide.png")
        photo = ImageTk.PhotoImage(self.hide_icon)
        self.hide_icon_panel = tkinter.Label(self.login_frame, image=photo, bg="blue")
        self.hide_icon_panel.image = photo
        self.hide_icon_panel.place(x=910, y=350)
        self.show_icon = Image.open("image projects\\images\\show.png")
        photo = ImageTk.PhotoImage(self.show_icon)
        self.show_icon_panel = tkinter.Label(self.login_frame, image=photo, bg="blue")
        self.show_icon_panel.image = photo
        # self.show_icon_panel.place(x=910, y=390)

    def create_forget_password_button(self):
        self.forget_pass_btn = tkinter.Button(self.login_frame, text="Forget Password ?",
                                              font=("yu gothic ui", 13, "bold underline"),
                                              width=25, bd=0, cursor="hand2", fg="white", background="blue"
                                              , height=1)
        self.forget_pass_btn.place(x=640, y=470)



