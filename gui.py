import tkinter


class GUI:
    """Manage all the gui, ***note use display method and render each state by param given
        or consider making own methods for any state."""

    def display(self,target,state):  # optimal
        """
            Display the current form from state stack. (optimal)
        :param target: Target windows to render.
        :param state: State form to render (sign_in_state,logged_state,...).
        """

    def display_sign_in_state(self):  # optimal
        """Use LoginWindow class to create sign in form (optimal)"""
        pass

    @staticmethod
    def create_text_message_label(text) -> tkinter.Label:
        pass

    @staticmethod
    def create_image_message_label(text) -> tkinter.Label:
        pass

    @staticmethod
    def create_file_message_label(text) -> tkinter.Label:
        pass
