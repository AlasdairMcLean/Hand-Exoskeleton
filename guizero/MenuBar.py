from tkinter import Menu
from .tkmixins import ScheduleMixin, DestroyMixin, FocusMixin
from . import utilities as utils
from .base import Base
from .App import App
from .Window import Window

class MenuBar(Base):

    def __init__(self, master, toplevel, options):

        if not isinstance(master, (App, Window)):
            utils.error_format("The [MenuBar] must have an [App] or [Window] object as its master")

        description = "[MenuBar] object "

        # Create a tk Menu object within this object
        tk = Menu(master.tk)

        super(MenuBar, self).__init__(master, tk, description)

        # Keep track of submenu objects
        self._sub_menus = []

        # Create all the top level menus
        for i in range(len(toplevel)):
            # Create this submenu
            new_menu = Menu(self.tk, tearoff=0)

            # Populate the drop down menu with the items/commands from the list
            for menu_item in options[i]:
                new_menu.add_command(label=menu_item[0], command=menu_item[1])

            # Append to the submenus list
            self._sub_menus.append(new_menu)

            # Add to the menu bar
            self.tk.add_cascade(label=toplevel[i], menu=self._sub_menus[i])

       	# Set this as the menu for the master object
       	master.tk.config(menu=self.tk)
