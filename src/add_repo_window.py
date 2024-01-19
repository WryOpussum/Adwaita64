from gi.repository import Adw, Gtk, Gio
from .models import Repo

@Gtk.Template(resource_path='/com/github/WryOpussum/Adwaita64/add_repo.ui')
class AddRepoWindow(Adw.Window):
    __gtype_name__ = 'AddRepoWindow'

    btn_cancel = Gtk.Template.Child()
    btn_create = Gtk.Template.Child()
    repo_selection = Gtk.Template.Child()
    compile_speed = Gtk.Template.Child()
    str_list_repo = Gtk.Template.Child()
    str_list_speed = Gtk.Template.Child()
    entry_name = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.item1 = Repo(title="sm64ex-coop", url="https://github.com/djoslin0/sm64ex-coop.git", path="sm64ex-coop")
        self.item2 = Repo(title="sm64ex")
        self.item3 = Repo(title="sm64ex-alo")
        self.item4 = Repo(title="render96ex")
        self.str_list_repo.append(self.item1.title)
        self.str_list_repo.append(self.item2.title)
        self.str_list_repo.append(self.item3.title)
        self.str_list_repo.append(self.item4.title)
        self.str_list_speed.append('Slow')
        self.str_list_speed.append('Medium')
        self.str_list_speed.append('Fast')
        self.str_list_speed.append('Uncapped')

    @Gtk.Template.Callback()

    def on_entry_row_change(self, entry):
        entry_name_str = str(self.entry_name.get_text())
        if entry_name_str != "":
            self.btn_create.set_sensitive(True)
        else:
            self.btn_create.set_sensitive(False)

    @Gtk.Template.Callback()
    def on_cancel_clicked(self, button):
        AddRepoWindow.close(self)

    @Gtk.Template.Callback()
    def on_create_clicked(self, button):
        print(self.entry_name.get_text())

    def create_repo_selection(self,item):
        repo=Label(text=item.title)
        return row
        
