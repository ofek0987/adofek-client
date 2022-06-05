from abc import ABC, abstractmethod

import tkinter


class IMessage(ABC):
    """Interface representing all the messages that can be sent/received, for example a text message"""
    def __init__(self, identifier: str):
        self.identifier = identifier

    @abstractmethod
    def display(self) -> tkinter.Label:
        """Will be used by the GUI in order to display the message"""
        pass
