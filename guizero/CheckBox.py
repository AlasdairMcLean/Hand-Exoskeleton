from tkinter import Checkbutton, IntVar
from . import utilities as utils
from .base import TextWidget

class CheckBox(TextWidget):

    def __init__(self, master, text, command=None, grid=None, align=None, args=None, visible=True, enabled=True):
        
        description = "[CheckBox] object with text \"" + text + "\""
        
        self._text = str(text)
        self._value = IntVar()
        tk = Checkbutton(master.tk, text=text, variable=self._value)
        
        super(CheckBox, self).__init__(master, tk, description, grid, align, visible, enabled)

        # Set the command callback
        self.tk.config(command=self._command_callback)
        self.update_command(command, args)

    # PROPERTIES
    # ----------------------------------
    # Whether the box is checked or not
    @property
    def value(self):
        return (self._value.get())

    # Set whether the box is checked or not
    @value.setter
    def value(self, value):
        try:
            value = int(value)
            if value in [0, 1]:
                self._value.set(value)

        except ValueError:
            utils.error_format("You can only set the value of " + self.description + " to either 0 (not checked) or 1 (checked)")

    # The text associated with this box
    @property
    def text(self):
        return (self._text)

    # Set whether the box is checked or not
    @text.setter
    def text(self, text):
        self._text = str(text)
        self.tk.config(text=self._text)
        self.description = "[CheckBox] object with text \"" + str(self._text) + "\""

    # METHODS
    # -------------------------------------------

    def toggle(self):
        self.tk.toggle()

    def update_command(self, command, args=None):
        if command is None:
            self._command = lambda: None
        else:
            if args is None:
                self._command = command
            else:
                self._command = utils.with_args(command, *args)
    
    def _command_callback(self):
        self._command()
        
    # DEPRECATED METHODS
    # --------------------------------------------
    # Return text associated with this checkbox
    def get_text(self):
        return self._text
        utils.deprecated("CheckBox get_text() is deprecated. Please use the text property instead.")

    # Return the value (1 or 0) of the box
    def get_value(self):
        return self._value.get()
        utils.deprecated("CheckBox get_value() is deprecated. Please use the value property instead.")

    # Change text
    def change_text(self, newtext):
        self._text = str(newtext)
        self.tk.config(text=self._text)
        self.description = "[CheckBox] object with text " + str(self._text)
        utils.deprecated("CheckBox change_text() is deprecated. Please use the text property instead.")
