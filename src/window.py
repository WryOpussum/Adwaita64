# window.py
#
# Copyright 2022 Wry Opussum
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gi
from gi.repository import Gtk, Gio, GObject, Adw
from pathlib import Path

global execBuffer
execBuffer = Gtk.EntryBuffer()
global nameBuffer
nameBuffer = Gtk.EntryBuffer()
global descBuffer
descBuffer = Gtk.EntryBuffer()
global listbox
listbox=Gtk.ListBox()
listbox.get_style_context().add_class(class_name='boxed-list')
listbox.set_selection_mode(Gtk.SelectionMode.NONE)
global liststore # We have to define liststore here instead of one line below because liststore is in the bind model
liststore = Gio.ListStore()
listbox.bind_model(liststore)
global RowWidget
RowWidget = Adw.ActionRow()
RowWidget.add_suffix(Gtk.Button(label="Launch"))


class Adwaita64Window(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #window setup
        self.header = Gtk.HeaderBar()
        self.set_titlebar(self.header)
        self.set_default_size(700, 500)
        self.set_title("Adwaita64")


        self.box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(self.box1)


        # Create Gio Header Menu

        headerMenu = Gio.Menu.new()
        headerMenu.append("About Adwaita64", "win.about")

        # Create Gio About Action

        aboutAction = Gio.SimpleAction.new("about", None)
        aboutAction.connect("activate", self.show_about)
        self.add_action(aboutAction)

        # Create Popover

        self.headerPopover = Gtk.PopoverMenu() # Create the popover Menu
        self.headerPopover.set_menu_model(headerMenu)

        # Create a menu button
        self.headerMenuButton = Gtk.MenuButton()
        self.headerMenuButton.set_popover(self.headerPopover)
        self.headerMenuButton.set_icon_name("open-menu-symbolic")
        self.header.pack_end(self.headerMenuButton)

        # Create the Add Repo Button

        self.addRepoButton = Gtk.Button()
        self.addRepoButton.set_icon_name("value-increase")
        self.addRepoButton.connect("clicked", self.show_add_repo)
        self.header.pack_start(self.addRepoButton)

        # Create a GtkListBox that stores them repos



        self.box1.append(listbox)


    global ExecutableDir



    def show_add_repo(self, action):
        addRepoDialog(parent=self)

    def show_about(self, aboutAction, param):
        self.about = Gtk.AboutDialog()
        self.about.set_modal(self)
        self.about.set_transient_for(self)
        self.about.set_program_name('Adwaita64')
        self.about.set_version("2.0.0")
        self.about.set_authors(['Wry Opussum'])
        self.about.set_copyright('2022 Wry Opussum')
        self.about.set_logo_icon_name('com.github.WryOpussum.Adwaita64')
        self.about.show()



class addRepoDialog(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(transient_for=parent, use_header_bar=True)
        self.parent = parent

        self.set_title(title='Add a Repository')
        self.use_header_bar = True
        self.set_modal(modal=True)
        self.set_default_size(600, 400)

        content_area = self.get_content_area()
        content_area.set_orientation(orientation=Gtk.Orientation.VERTICAL)
        content_area.set_spacing(spacing=12)
        content_area.set_margin_top(margin=12)
        content_area.set_margin_end(margin=12)
        content_area.set_margin_bottom(margin=12)
        content_area.set_margin_start(margin=12)


        sm64exaloText = Gtk.Text()
        # Build the Combo Box
        self.repoSelectComboBox = Gtk.ComboBoxText.new()
        self.repoSelectComboBox.append("ex", "sm64ex")
        self.repoSelectComboBox.append("coop", "sm64ex-coop")
        # Build the Check Button
        self.checkCustomRepo = Gtk.CheckButton()
        self.checkCustomRepo.set_label("Using a custom repo")
        self.checkCustomRepo.connect("toggled", self.checkCustomRepoState)
        # Build a directory Entry with a Browse button
        self.customRepoExecutable = Gtk.Entry()
        self.customRepoExecutable.set_sensitive(False)
        self.customRepoExecutable.set_placeholder_text("sm64 executable directory")
        self.customRepoExecutable.set_buffer(execBuffer)
        self.customRepoExecutable.set_icon_from_icon_name(Gtk.EntryIconPosition.SECONDARY, "folder-documents-symbolic")
        self.customRepoExecutable.connect("icon-press", self.loadExecutableSelection)  # Add the widgets to the Dialog
        # Name Entry
        self.nameEntry = Gtk.Entry()
        self.nameEntry.set_placeholder_text("Name of the repo")
        self.nameEntry.set_buffer(nameBuffer)
        # Description Entry
        self.descEntry = Gtk.Entry()
        self.descEntry.set_placeholder_text("A description. Like 'online multiplayer'.")
        self.descEntry.set_buffer(descBuffer)
        # Add the OK button witch does the magic
        self.okButton = Gtk.Button()
        self.okButton.set_label("OK")
        self.okButton.get_style_context().add_class(class_name='suggested-action')
        self.okButton.connect("clicked", self.onOK)
        # add everything to content
        content_area.append(self.repoSelectComboBox)
        content_area.append(self.checkCustomRepo)
        content_area.append(self.customRepoExecutable)
        content_area.append(self.nameEntry)
        content_area.append(self.descEntry)
        content_area.append(self.okButton)
        # Show the Dialog
        self.show()
    #create a function that disables the combobox
    def checkCustomRepoState(self, action):
        if (self.checkCustomRepo.get_active()):
            self.repoSelectComboBox.set_sensitive(False)
            self.customRepoExecutable.set_sensitive(True)

        else:
            self.repoSelectComboBox.set_sensitive(True)
            self.customRepoExecutable.set_sensitive(False)
    def loadExecutableSelection(self, action, hi):
        executableSelection(parent=self)
        customRepoExecutable.set_placeholder_text("")
    def onOK(self, action):
        listbox.insert(Adw.ActionRow(title=f"{nameBuffer.get_text()}", subtitle=f"{descBuffer.get_text()}"), -1)
        self.close()


class executableSelection(Gtk.FileChooserDialog):
     home = Path.home()
     def __init__(self, parent,):
        super().__init__(transient_for=parent, use_header_bar=True)


        self.set_action(action=Gtk.FileChooserAction.OPEN)
        title = 'Select a Executable'
        self.set_title(title=title)
        self.set_modal(modal=True)
        self.set_default_size(600, 400)
        self.connect('response', self.dialog_response)
        self.set_current_folder(
            Gio.File.new_for_path(path=str(self.home)),
        )
        # Add stupid button lol
        self.add_buttons(
            '_Cancel', Gtk.ResponseType.CANCEL,
            '_Select', Gtk.ResponseType.OK
        )
        btn_select = self.get_widget_for_response(
            response_id=Gtk.ResponseType.OK,
        )
        # Ah a comment. i am assign styles to the buttons.
        btn_select.get_style_context().add_class(class_name='suggested-action')
        btn_cancel = self.get_widget_for_response(
            response_id=Gtk.ResponseType.CANCEL,
        )


        self.show()

     def dialog_response(self, widget, response):

        if response == Gtk.ResponseType.OK:
            glocalfile = self.get_file()
            execBuffer.set_text(f"{glocalfile.get_path()}", -1)
            print(f'Selected Exec: {glocalfile.get_basename()}')
            print(f'Selected Exec Path: {glocalfile.get_path()}')

        widget.close()


