import tkinter
from login_state import LoginWindow
from main_form import MainForm



class GUI:
    """Manage all the gui, ***note use display method and render each state by param given
        or consider making own methods for any state."""

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.login_state = LoginWindow(self.main_window)
        self.main_state = MainForm(self.main_window)

    def display_splash_screen(self):
        pass

    def display_main_screen(self):
        self.main_state.create_bg_layout()

    def display_sign_in_state(self):
        """Use LoginWindow class to create sign in form"""
        self.login_state.create_frame_layer()
        self.login_state.create_sign_in_layer()
        self.login_state.create_logo()
        self.login_state.create_login_button()
        self.login_state.create_forget_password_button()
        self.login_state.create_password_input()
        self.login_state.create_password_logo()
        self.login_state.create_password_show_or_hide_button()
        self.login_state.create_username_input()
        self.login_state.create_username_logo()

    def update(self):
        self.main_window.update()
        self.main_window.mainloop()

    def clear(self):
        self.main_window.destroy()




