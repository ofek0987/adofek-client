import tkinter
from login_state import LoginWindow


class GUI:
    """Manage all the gui, ***note use display method and render each state by param given
        or consider making own methods for any state."""

    def __init__(self):
        self.main_window = None
        self.login_state = None

    def display_splash_screen(self):
        pass

    def display_sign_in_state(self):
        """Use LoginWindow class to create sign in form"""
        self.main_window = tkinter.Tk()
        self.login_state = LoginWindow(self.main_window)
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

    @staticmethod
    def create_text_message_label(text) -> tkinter.Label:
        pass

    @staticmethod
    def create_image_message_label(text) -> tkinter.Label:
        pass

    @staticmethod
    def create_file_message_label(text) -> tkinter.Label:
        pass

