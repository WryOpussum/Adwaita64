from gi.repository import Adw, Gtk, Gio, GObject

class Item(GObject.GObject):

    title = GObject.property(type = str)

    def __init__(self):
        GObject.GObject.__init__(self)

class Repo(GObject.GObject):
    title = GObject.property(type = str)
    url = GObject.property(type = str)
    path = GObject.property(type = str)
