# window.py
#
# Copyright 2024 Joshua Elmasri
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
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw, Gtk, Gio
from .models import Item
from .add_repo_window import AddRepoWindow

@Gtk.Template(resource_path='/com/github/WryOpussum/Adwaita64/window.ui')
class Adwaita64Window(Adw.ApplicationWindow):
    __gtype_name__ = 'Adwaita64Window'

    repo_list = Gtk.Template.Child()
    menu_add_repo = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.repo_list_model = Gio.ListStore()
        self.repo_list.bind_model(self.repo_list_model, self.create_entry_func)

    @Gtk.Template.Callback()
    def on_menu_add_repo_action(self, widget):
        add_repo_window = AddRepoWindow()
        add_repo_window.set_transient_for(self)
        add_repo_window.present()

    def create_entry_func(self,item):
        row=Adw.ActionRow(title=item.title)
        return row



    def create_repo_window(clicked, self):
        win = AddRepoWindow()
        win.present()



