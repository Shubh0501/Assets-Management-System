import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import auth

newAuth = auth.Authentication("localhost", 27017, 'user_database', None, None)

class Main_Window(Gtk.Window):
    
    def __init__(self):
        
        Gtk.Window.__init__(self, title = "Login Page")
        self.set_border_width(10)
        self.set_default_size(850, 300)
        
        self.hbox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 0)
        self.vbox_left = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 5)
        self.vbox_centre = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 5)
        self.vbox_right = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 5)

        self.hbox.pack_start(self.vbox_left, True, True, 0)
        self.hbox.pack_start(self.vbox_centre, True, True, 0)
        self.hbox.pack_start(self.vbox_right, True, True, 0)

        self.title = Gtk.Label()
        self.title.set_markup("<big><big><big><b>Login Page</b></big></big></big>")
        self.vbox_centre.pack_start(self.title, True, True, 0)

        self.username_label = Gtk.Label("Username :")
        self.vbox_centre.pack_start(self.username_label, True, True, 0)
        self.username = Gtk.Entry()
        self.vbox_centre.pack_start(self.username, True, True, 0)
        self.password_label = Gtk.Label("Password :")
        self.vbox_centre.pack_start(self.password_label, True, True, 0)
        self.password = Gtk.Entry()
        self.password.set_visibility(False)
        self.vbox_centre.pack_start(self.password, True, True, 0)

        self.login_button = Gtk.Button("Login")
        self.login_button.connect("clicked", self.login_button_clicked)
        self.vbox_centre.pack_start(self.login_button, True, True, 0)

        self.create_account = Gtk.Button("Create new account")
        self.create_account.connect("clicked", self.create_account_clicked)
        self.vbox_centre.pack_start(self.create_account, True, True, 0)

        self.add(self.hbox)


    def login_button_clicked(self, widget):
        if len(self.username.get_text()) == 0 or len(self.password.get_text()) == 0 :
            dialog_details = Details(self)
            response = dialog_details.run()

            dialog_details.destroy()
            return
        else:
            check = newAuth.login(self.username.get_text(), self.password.get_text())

            if check == True:
                print("Login Successfull")
                return
            else:
                print("Login Error")
                return



    def create_account_clicked(self, widget):
        dialog_new_account = New_account()
        dialog_new_account.set_position(Gtk.WindowPosition.CENTER)
        dialog_new_account.connect("delete-event", Gtk.main_quit)
        dialog_new_account.show_all()
        Gtk.main()
        return


class Details(Gtk.Dialog):

    def __init__(self, parent):

        Gtk.Dialog.__init__(self, "Error", parent, Gtk.DialogFlags.MODAL,(Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.set_default_size(130, 80)
        self.set_border_width(20)
        self.set_position(Gtk.WindowPosition.CENTER)
        area = self.get_content_area()
        area.add(Gtk.Label("Username or Password Incorrect"))
        self.show_all()


class New_account(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self, title = "Create New Account")
        self.set_border_width(10)
        self.set_default_size(850, 300)

        self.hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.vbox_centre = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)

        self.hbox.pack_start(self.vbox_left, True, True, 0)
        self.hbox.pack_start(self.vbox_centre, True, True, 0)
        self.hbox.pack_start(self.vbox_right, True, True, 0)

        self.personal_number_label = Gtk.Label("Personal Number :")
        self.personal_number = Gtk.Entry()
        self.personal_number.set_placeholder_text("compulsory")
        self.vbox_centre.pack_start(self.personal_number_label, True, True, 0)
        self.vbox_centre.pack_start(self.personal_number, True, True, 0)

        self.name_label = Gtk.Label("Name :")
        self.name = Gtk.Entry()
        self.name.set_placeholder_text("compulsory")
        self.vbox_centre.pack_start(self.name_label, True, True, 0)
        self.vbox_centre.pack_start(self.name, True, True, 0)

        self.password_label = Gtk.Label("Password :")
        self.password = Gtk.Entry()
        self.password.set_visibility(False)
        self.password.set_placeholder_text("compulsory")
        self.vbox_centre.pack_start(self.password_label, True, True, 0)
        self.vbox_centre.pack_start(self.password, True, True, 0)

        self.create_account_button = Gtk.Button("Create Account")
        self.create_account_button.connect("clicked", self.create_account_button_clicked)
        self.vbox_centre.pack_start(self.create_account_button, True, True, 0)

        self.add(self.hbox)



    def create_account_button_clicked(self, widget):
        if len(self.personal_number.get_text()) == 0 or len(self.name.get_text()) == 0 or len(self.password.get_text()) == 0:
            dialog_error = Error(self)
            response = dialog_error.run()

            dialog_error.destroy()
            return
        else:

            result = newAuth.reg(self.name.get_text(),self.personal_number.get_text(),self.password.get_text())

            if result:
                print ("registrations successful")
            else:
                print ("registration failed")

            self.destroy()
            dialog_created_account = Account_created(self)
            response = dialog_created_account.run()

            dialog_created_account.destroy()
            return


class Account_created(Gtk.Dialog):

    def __init__(self, parent):

        Gtk.Dialog.__init__(self, "Account Created", parent, Gtk.DialogFlags.MODAL, (Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.set_default_size(130, 80)
        self.set_border_width(20)
        self.set_position(Gtk.WindowPosition.CENTER)
        area = self.get_content_area()
        area.add(Gtk.Label("New Account Created. Please Login to Continue."))
        self.show_all()


class Error(Gtk.Dialog):

    def __init__(self, parent):

        Gtk.Dialog.__init__(self, "Error", parent, Gtk.DialogFlags.MODAL,(Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.set_default_size(130, 80)
        self.set_border_width(20)
        self.set_position(Gtk.WindowPosition.CENTER)
        area = self.get_content_area()
        area.add(Gtk.Label("Please enter all the details"))
        self.show_all()



window = Main_Window()
window.set_position(Gtk.WindowPosition.CENTER)
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
