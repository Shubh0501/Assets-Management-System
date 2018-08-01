import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import auth
import datetime


newAuth = auth.Authentication("localhost", 27017, 'user_database', None, None)
equip_sl_no = None
owner = None
search_equip = None
search_schedule = None
search_assign = None

#MAIN WINDOW LOGIN PAGE
class Main_Window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Login Page")
        self.set_border_width(10)
        self.set_default_size(1920, 1080)

        self.box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 10)

        self.title = Gtk.Label()
        self.title.set_markup("<big><big><big><big><big><big><big><big><b>Login Page</b></big></big></big></big></big></big></big></big>")
        self.box.pack_start(self.title, False, False, 40)
        self.username_label = Gtk.Label()
        self.username_label.set_markup("<big>Username :</big>")
        self.box.pack_start(self.username_label, False, False, 0)
        self.username = Gtk.Entry()
        self.username.set_property("margin_left", 80)
        self.username.set_property("margin_right", 80)
        self.box.pack_start(self.username, False, False, 0)
        self.password_label = Gtk.Label()
        self.password_label.set_markup("<big>Password :</big>")
        self.box.pack_start(self.password_label, False, False, 0)
        self.password = Gtk.Entry()
        self.password.set_property("margin_left", 80)
        self.password.set_property("margin_right", 80)
        self.password.set_visibility(False)
        self.box.pack_start(self.password, False, False, 0)

        self.login_button = Gtk.Button("Login")
        #self.login_button.connect("clicked", self.login_button_clicked)
        self.box.pack_start(self.login_button, False, False, 10)
        self.login_button.set_property("margin_left", 40)
        self.login_button.set_property("margin_right", 40)

        self.create_account = Gtk.Button("Create new account")
        self.create_account.set_property("margin_left", 40)
        self.create_account.set_property("margin_right", 40)
        #self.create_account.connect("clicked", self.create_account_clicked)
        self.box.pack_start(self.create_account, False, False, 10)

        self.box.set_halign(Gtk.Align.CENTER)
        self.box.set_valign(Gtk.Align.CENTER)
        self.box.set_vexpand(True)
        self.box.set_hexpand(True)
        self.create_account.connect("clicked", self.create_account_clicked)
        self.login_button.connect("clicked", self.login_button_clicked)

        self.add(self.box)
        return


    def login_button_clicked(self, widget):
        if len(self.username.get_text()) == 0 or len(self.password.get_text()) == 0 :
            dialog_details = Details(self)
            response = dialog_details.run()

            dialog_details.destroy()
            return

        try:

            pqr = int(self.username.get_text())
            if (pqr < 100000 or pqr > 999999):
                pqr = (int)("abc")
        except Exception as e:
            dialog_number = Number(self)
            response = dialog_number.run()
            dialog_number.destroy()
            return

        else:
            check = newAuth.login(self.username.get_text(), self.password.get_text())

            if check == True:
                self.destroy()
                equipment_details = User_profile()
                equipment_details.set_position(Gtk.WindowPosition.CENTER)
                equipment_details.connect("delete-event", Gtk.main_quit)
                equipment_details.show_all()
                Gtk.main()
                return
            else:
                dialog_details = Details(self)
                response = dialog_details.run()

                dialog_details.destroy()
                return

    def create_account_clicked(self, widget):
        dialog_new_account = New_account()
        dialog_new_account.set_position(Gtk.WindowPosition.CENTER)
        dialog_new_account.connect("delete-event", Gtk.main_quit)
        dialog_new_account.show_all()
        Gtk.main()
        return

#NEW ACCOUNT CREATE FORM
class New_account(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self, title = "Create New Account")
        self.set_border_width(10)
        self.set_default_size(1920,1080)

        self.hbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        self.personal_number_label = Gtk.Label()
        self.personal_number_label.set_markup("<big><b>Personal Number :</b></big>")
        self.personal_number = Gtk.Entry()
        self.personal_number.set_placeholder_text("compulsory")
        self.hbox.pack_start(self.personal_number_label, False, False, 5)
        self.hbox.pack_start(self.personal_number, False, False, 5)

        self.name_label = Gtk.Label()
        self.name_label.set_markup("<big><b>Name :</b></big>")
        self.name = Gtk.Entry()
        self.name.set_placeholder_text("compulsory")
        self.hbox.pack_start(self.name_label, False, False, 5)
        self.hbox.pack_start(self.name, False, False, 5)

        self.mail_label = Gtk.Label()
        self.mail_label.set_markup("<big><b>Mail : </b></big>")
        self.mail = Gtk.Entry()
        self.mail.set_placeholder_text("compulsory")
        self.hbox.pack_start(self.mail_label, False, False, 5)
        self.hbox.pack_start(self.mail, False,False, 5)

        self.password_label = Gtk.Label()
        self.password_label.set_markup("<big><b>Password :</b></big>")
        self.password = Gtk.Entry()
        self.password.set_visibility(False)
        self.password.set_placeholder_text("compulsory")
        self.hbox.pack_start(self.password_label, False, False, 5)
        self.hbox.pack_start(self.password, False, False, 5)

        self.create_account_button = Gtk.Button("Create Account")
        self.create_account_button.connect("clicked", self.create_account_button_clicked)
        self.hbox.pack_start(self.create_account_button, False, False, 10)

        self.hbox.set_halign(Gtk.Align.CENTER)
        self.hbox.set_valign(Gtk.Align.CENTER)
        self.hbox.set_hexpand(True)
        self.hbox.set_vexpand(True)

        self.add(self.hbox)
        return

    def create_account_button_clicked(self, widget):
        if len(self.personal_number.get_text()) == 0 or len(self.name.get_text()) == 0 or len(
                self.password.get_text()) == 0 or len(self.mail.get_text()) == 0:
            dialog_error = Error(self)
            response = dialog_error.run()

            dialog_error.destroy()
            return
        try:

            pqr = int(self.personal_number.get_text())
            if (pqr < 100000 or pqr > 999999):
                pqr = (int)("abc")
        except Exception as e:
            dialog_number = Number(self)
            response = dialog_number.run()
            dialog_number.destroy()
            return
        else:

            result = newAuth.reg(self.name.get_text(), self.personal_number.get_text(), self.mail.get_text(),
                                 self.password.get_text())

            if result:
                self.destroy()
                dialog_created_account = Account_created(self)
                response = dialog_created_account.run()

                dialog_created_account.destroy()
                return
            else:
                dialog_exists = Exists(self)
                response = dialog_exists.run()

                dialog_exists.destroy()
                return

#USER PROFILE PAGE
class User_profile(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self, title = "Your Profile")
        self.set_border_width(5)
        self.set_default_size(1920,1080)
        self.box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 0)
        self.hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)

        self.box.pack_start(self.hbox1, False, False, 0)
        self.box.pack_start(self.hbox2, False, False, 0)

        image = Gtk.Image()
        image.set_from_file('jusco_titl.jpg')
        self.hbox1.add(image)
        self.hbox1.set_hexpand(True)
        self.hbox1.set_halign(Gtk.Align.CENTER)
        self.hbox1.show_all()

        self.menu = Gtk.MenuBar()
        self.dashboard = Gtk.Menu()
        self.dashboard_dropdown = Gtk.MenuItem("DASHBOARD")
        self.dashboard_dropdown.set_submenu(self.dashboard)
        self.dashboard_menu1 = Gtk.MenuItem("Menu Item 1")
        self.dashboard.append(self.dashboard_menu1)
        self.dashboard_menu2 = Gtk.MenuItem("Menu Item 2")
        self.dashboard.append(self.dashboard_menu2)
        self.dashboard_menu3 = Gtk.MenuItem("Menu Item 3")
        self.dashboard.append(self.dashboard_menu3)
        self.menu.append(self.dashboard_dropdown)
        self.admin = Gtk.Menu()
        self.admin_dropdown = Gtk.MenuItem("ADMIN")
        self.admin_dropdown.set_submenu(self.admin)
        self.admin_menu1 = Gtk.MenuItem("Menu Item 1")
        self.admin.append(self.admin_menu1)
        self.admin_menu2 = Gtk.MenuItem("Menu Item 2")
        self.admin.append(self.admin_menu2)
        self.admin_menu3 = Gtk.MenuItem("Menu Item 3")
        self.admin.append(self.admin_menu3)
        self.menu.append(self.admin_dropdown)
        self.master = Gtk.Menu()
        self.master_dropdown = Gtk.MenuItem("MASTER")
        self.master_dropdown.set_submenu(self.master)
        self.master_company = Gtk.MenuItem("Company")
        self.master.append(self.master_company)
        self.master_department = Gtk.MenuItem("Department")
        self.master.append(self.master_department)
        self.master_equipment = Gtk.MenuItem("Equipment")
        self.master_equipment.connect("activate", self.call_equipment_list)
        self.master.append(self.master_equipment)
        self.menu.append(self.master_dropdown)
        self.Schedule_menu = Gtk.Menu()
        self.schedule_dropdown = Gtk.MenuItem("SCHEDULE")
        self.schedule_dropdown.set_submenu(self.Schedule_menu)
        self.schedule_schedule = Gtk.MenuItem("Schedule")
        self.schedule_schedule.connect("activate", self.call_schedule_list)
        self.assign_schedule = Gtk.MenuItem("Assign Job")
        self.assign_schedule.connect("activate", self.call_assign_list)
        self.Schedule_menu.append(self.schedule_schedule)
        self.Schedule_menu.append(Gtk.SeparatorMenuItem())
        self.Schedule_menu.append(self.assign_schedule)
        self.menu.append(self.schedule_dropdown)
        self.complain = Gtk.Menu()
        self.complain_dropdown = Gtk.MenuItem("COMPLAIN")
        self.complain_dropdown.set_submenu(self.complain)
        self.complain_menu1 = Gtk.MenuItem("Menu Item 1")
        self.complain.append(self.complain_menu1)
        self.complain_menu2 = Gtk.MenuItem("Menu Item 2")
        self.complain.append(self.complain_menu2)
        self.menu.append(self.complain_dropdown)
        self.reports = Gtk.Menu()
        self.reports_dropdown = Gtk.MenuItem("REPORTS")
        self.reports_dropdown.set_submenu(self.reports)
        self.reports_menu1 = Gtk.MenuItem("Menu Item 1")
        self.reports.append(self.reports_menu1)
        self.menu.append(self.reports_dropdown)
        self.logout_dropdown = Gtk.MenuItem("LOGOUT")
        self.menu.append(self.logout_dropdown)
        self.logout_dropdown.connect("activate", self.logout_call)

        self.hbox2.set_hexpand(True)
        self.dashboard_dropdown.set_property("margin_left", 20)
        self.dashboard_dropdown.set_property("margin_right", 10)
        self.admin_dropdown.set_property("margin_left", 10)
        self.admin_dropdown.set_property("margin_right", 10)
        self.master_dropdown.set_property("margin_left", 10)
        self.master_dropdown.set_property("margin_right", 10)
        self.schedule_dropdown.set_property("margin_left", 10)
        self.schedule_dropdown.set_property("margin_right", 10)
        self.complain_dropdown.set_property("margin_left", 10)
        self.complain_dropdown.set_property("margin_right", 10)
        self.reports_dropdown.set_property("margin_left", 10)
        self.reports_dropdown.set_property("margin_right", 1158)
        self.logout_dropdown.set_property("margin_right", 30)

        self.hbox2.set_halign(Gtk.Align.START)
        self.hbox2.pack_start(self.menu, True, True, 0)

        self.add(self.box)
        return

    def call_equipment_list(self, widget):
        self.destroy()
        new_window = Equipment_list()
        new_window.set_position(Gtk.WindowPosition.CENTER)
        new_window.connect("delete-event", Gtk.main_quit)
        new_window.show_all()
        Gtk.main()
        return

    def call_schedule_list(self, widget):
        self.destroy()
        new_window = Schedule_list()
        new_window.set_position(Gtk.WindowPosition.CENTER)
        new_window.connect("delete-event", Gtk.main_quit)
        new_window.show_all()
        Gtk.main()
        return

    def call_assign_list(self, widget):
        self.destroy()
        new_window = Assign_list()
        new_window.set_position(Gtk.WindowPosition.CENTER)
        new_window.connect("delete-event", Gtk.main_quit)
        new_window.show_all()
        Gtk.main()
        return

    def logout_call(self, widget):
        self.destroy()
        window = Main_Window()
        window.set_position(Gtk.WindowPosition.CENTER)
        window.connect("delete-event", Gtk.main_quit)
        window.show_all()
        Gtk.main()
        return

#EQUIPMENTS LIST
class Equipment_list(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self, title = "Equipment List")

        self.set_border_width(5)
        self.set_default_size(1920,1080)
        self.box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 0)
        self.hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.hbox3 = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 0)

        image = Gtk.Image()
        image.set_from_file('')
        self.hbox1.add(image)
        self.hbox1.set_hexpand(True)
        self.hbox1.set_halign(Gtk.Align.CENTER)
        self.hbox1.show_all()

        self.label = Gtk.Label()
        self.label.set_markup("<big><big><big><big><big><big><big><b>EQUIPMENTS</b></big></big></big></big></big></big></big>")
        self.box.pack_start(self.hbox1, False, False, 0)
        self.box.pack_start(self.hbox2, False, False, 0)
        self.box.pack_start(self.label, False, False, 0)
        self.box.pack_start(self.hbox3, False, False, 0)

        self.menu = Gtk.MenuBar()
        self.dashboard = Gtk.Menu()
        self.dashboard_dropdown = Gtk.MenuItem("DASHBOARD")
        self.dashboard_dropdown.set_submenu(self.dashboard)
        self.dashboard_menu1 = Gtk.MenuItem("Menu Item 1")
        self.dashboard.append(self.dashboard_menu1)
        self.dashboard_menu2 = Gtk.MenuItem("Menu Item 2")
        self.dashboard.append(self.dashboard_menu2)
        self.dashboard_menu3 = Gtk.MenuItem("Menu Item 3")
        self.dashboard.append(self.dashboard_menu3)
        self.menu.append(self.dashboard_dropdown)
        self.admin = Gtk.Menu()
        self.admin_dropdown = Gtk.MenuItem("ADMIN")
        self.admin_dropdown.set_submenu(self.admin)
        self.admin_menu1 = Gtk.MenuItem("Menu Item 1")
        self.admin.append(self.admin_menu1)
        self.admin_menu2 = Gtk.MenuItem("Menu Item 2")
        self.admin.append(self.admin_menu2)
        self.admin_menu3 = Gtk.MenuItem("Menu Item 3")
        self.admin.append(self.admin_menu3)
        self.menu.append(self.admin_dropdown)
        self.master = Gtk.Menu()
        self.master_dropdown = Gtk.MenuItem("MASTER")
        self.master_dropdown.set_submenu(self.master)
        self.master_company = Gtk.MenuItem("Company")
        self.master.append(self.master_company)
        self.master_department = Gtk.MenuItem("Department")
        self.master.append(self.master_department)
        self.master_equipment = Gtk.MenuItem("Equipment")
        self.master_equipment.connect("activate", self.call_equipment_list)
        self.master.append(self.master_equipment)
        self.menu.append(self.master_dropdown)
        self.Schedule_menu = Gtk.Menu()
        self.schedule_dropdown = Gtk.MenuItem("SCHEDULE")
        self.schedule_dropdown.set_submenu(self.Schedule_menu)
        self.schedule_schedule = Gtk.MenuItem("Schedule")
        self.schedule_schedule.connect("activate", self.call_schedule_list)
        self.assign_schedule = Gtk.MenuItem("Assign Job")
        self.assign_schedule.connect("activate", self.call_assign_list)
        self.Schedule_menu.append(self.schedule_schedule)
        self.Schedule_menu.append(Gtk.SeparatorMenuItem())
        self.Schedule_menu.append(self.assign_schedule)
        self.menu.append(self.schedule_dropdown)
        self.complain = Gtk.Menu()
        self.complain_dropdown = Gtk.MenuItem("COMPLAIN")
        self.complain_dropdown.set_submenu(self.complain)
        self.complain_menu1 = Gtk.MenuItem("Menu Item 1")
        self.complain.append(self.complain_menu1)
        self.complain_menu2 = Gtk.MenuItem("Menu Item 2")
        self.complain.append(self.complain_menu2)
        self.menu.append(self.complain_dropdown)
        self.reports = Gtk.Menu()
        self.reports_dropdown = Gtk.MenuItem("REPORTS")
        self.reports_dropdown.set_submenu(self.reports)
        self.reports_menu1 = Gtk.MenuItem("Menu Item 1")
        self.reports.append(self.reports_menu1)
        self.menu.append(self.reports_dropdown)
        self.logout_dropdown = Gtk.MenuItem("LOGOUT")
        self.menu.append(self.logout_dropdown)
        self.logout_dropdown.connect("activate", self.logout_call)

        self.hbox2.set_hexpand(True)
        self.dashboard_dropdown.set_property("margin_left", 20)
        self.dashboard_dropdown.set_property("margin_right", 10)
        self.admin_dropdown.set_property("margin_left", 10)
        self.admin_dropdown.set_property("margin_right", 10)
        self.master_dropdown.set_property("margin_left", 10)
        self.master_dropdown.set_property("margin_right", 10)
        self.schedule_dropdown.set_property("margin_left", 10)
        self.schedule_dropdown.set_property("margin_right", 10)
        self.complain_dropdown.set_property("margin_left", 10)
        self.complain_dropdown.set_property("margin_right", 10)
        self.reports_dropdown.set_property("margin_left", 10)
        self.reports_dropdown.set_property("margin_right", 1158)
        self.logout_dropdown.set_property("margin_right", 30)

        self.hbox2.set_halign(Gtk.Align.START)
        self.hbox2.pack_start(self.menu, True, True, 0)

        self.search_label = Gtk.Label("Enter the equipment to be searched :")
        self.search_label.set_property("margin_top", 100)
        self.search_label.set_property("margin_bottom", 10)
        self.hbox3.pack_start(self.search_label, False, False, 0)
        self.search = Gtk.Entry()
        self.search.set_property("margin_top", 10)
        self.search.set_property("margin_bottom", 10)
        self.hbox3.pack_start(self.search, False, False, 0)
        self.search_button = Gtk.Button("Search")
        self.search_button.set_property("margin_top", 10)
        self.search_button.set_property("margin_bottom", 10)
        self.search_button.set_property("margin_left", 40)
        self.search_button.set_property("margin_right", 40)
        self.hbox3.pack_start(self.search_button, False, False, 0)

        self.hbox3.set_halign(Gtk.Align.CENTER)

        self.new_button = Gtk.Button("New Equipment")
        self.new_button.set_property("margin_top", 10)
        self.new_button.set_property("margin_left", 40)
        self.new_button.set_property("margin_right", 40)
        self.hbox3.pack_start(self.new_button, False, False, 0)

        self.new_button.connect("clicked", self.call_equipment_form)
        self.search_button.connect("clicked", self.search_button_clicked)

        self.add(self.box)
        self.show_all()
        return

    def call_equipment_form(self, widget):
        new_window = Equipment_form()
        new_window.set_position(Gtk.WindowPosition.CENTER)
        new_window.connect("delete-event", Gtk.main_quit)
        new_window.show_all()
        Gtk.main()
        return

    def search_button_clicked(self, widget):
        global search_equip
        search_equip = self.search.get_text()
        try:
            details = auth.Equipment.objects.get(equipment_name=search_equip)
        except Exception as e:
            dialog_number = Search_error(self)
            response = dialog_number.run()
            dialog_number.destroy()
            return

        new_window = Search_equip()
        new_window.set_position(Gtk.WindowPosition.CENTER)
        new_window.connect("delete-event", Gtk.main_quit)
        new_window.show_all()
        Gtk.main()
        return

    def call_equipment_list(self, widget):
        self.destroy()
        new_window = Equipment_list()
        new_window.set_position(Gtk.WindowPosition.CENTER)
        new_window.connect("delete-event", Gtk.main_quit)
        new_window.show_all()
        Gtk.main()
        return

    def call_schedule_list(self, widget):
        self.destroy()
        new_window = Schedule_list()
        new_window.set_position(Gtk.WindowPosition.CENTER)
        new_window.connect("delete-event", Gtk.main_quit)
        new_window.show_all()
        Gtk.main()
        return

    def call_assign_list(self, widget):
        self.destroy()
        new_window = Assign_list()
        new_window.set_position(Gtk.WindowPosition.CENTER)
        new_window.connect("delete-event", Gtk.main_quit)
        new_window.show_all()
        Gtk.main()
        return

    def logout_call(self, widget):
        self.destroy()
        window = Main_Window()
        window.set_position(Gtk.WindowPosition.CENTER)
        window.connect("delete-event", Gtk.main_quit)
        window.show_all()
        Gtk.main()
        return

#SCHEDULE JOB LIST
class Schedule_list(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self, title = "Schedule List")

        self.set_border_width(5)
        self.set_default_size(1920,1080)
        self.box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 0)
        self.hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.hbox3 = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 0)

        image = Gtk.Image()
        image.set_from_file('')
        self.hbox1.add(image)
        self.hbox1.set_hexpand(True)
        self.hbox1.set_halign(Gtk.Align.CENTER)
        self.hbox1.show_all()

        self.label = Gtk.Label()
        self.label.set_markup("<big><big><big><big><big><big><big><b>SCHEDULED SERVICES</b></big></big></big></big></big></big></big>")
        self.box.pack_start(self.hbox1, False, False, 0)
        self.box.pack_start(self.hbox2, False, False, 0)
        self.box.pack_start(self.label, False, False, 0)
        self.box.pack_start(self.hbox3, False, False, 0)

        self.menu = Gtk.MenuBar()
        self.dashboard = Gtk.Menu()
        self.dashboard_dropdown = Gtk.MenuItem("DASHBOARD")
        self.dashboard_dropdown.set_submenu(self.dashboard)
        self.dashboard_menu1 = Gtk.MenuItem("Menu Item 1")
        self.dashboard.append(self.dashboard_menu1)
        self.dashboard_menu2 = Gtk.MenuItem("Menu Item 2")
        self.dashboard.append(self.dashboard_menu2)
        self.dashboard_menu3 = Gtk.MenuItem("Menu Item 3")
        self.dashboard.append(self.dashboard_menu3)
        self.menu.append(self.dashboard_dropdown)
        self.admin = Gtk.Menu()
        self.admin_dropdown = Gtk.MenuItem("ADMIN")
        self.admin_dropdown.set_submenu(self.admin)
        self.admin_menu1 = Gtk.MenuItem("Menu Item 1")
        self.admin.append(self.admin_menu1)
        self.admin_menu2 = Gtk.MenuItem("Menu Item 2")
        self.admin.append(self.admin_menu2)
        self.admin_menu3 = Gtk.MenuItem("Menu Item 3")
        self.admin.append(self.admin_menu3)
        self.menu.append(self.admin_dropdown)
        self.master = Gtk.Menu()
        self.master_dropdown = Gtk.MenuItem("MASTER")
        self.master_dropdown.set_submenu(self.master)
        self.master_company = Gtk.MenuItem("Company")
        self.master.append(self.master_company)
        self.master_department = Gtk.MenuItem("Department")
        self.master.append(self.master_department)
        self.master_equipment = Gtk.MenuItem("Equipment")
        self.master_equipment.connect("activate", self.call_equipment_list)
        self.master.append(self.master_equipment)
        self.menu.append(self.master_dropdown)
        self.Schedule_menu = Gtk.Menu()
        self.schedule_dropdown = Gtk.MenuItem("SCHEDULE")
        self.schedule_dropdown.set_submenu(self.Schedule_menu)
        self.schedule_schedule = Gtk.MenuItem("Schedule")
        self.schedule_schedule.connect("activate", self.call_schedule_list)
        self.assign_schedule = Gtk.MenuItem("Assign Job")
        self.assign_schedule.connect("activate", self.call_assign_list)
        self.Schedule_menu.append(self.schedule_schedule)
        self.Schedule_menu.append(Gtk.SeparatorMenuItem())
        self.Schedule_menu.append(self.assign_schedule)
        self.menu.append(self.schedule_dropdown)
        self.complain = Gtk.Menu()
        self.complain_dropdown = Gtk.MenuItem("COMPLAIN")
        self.complain_dropdown.set_submenu(self.complain)
        self.complain_menu1 = Gtk.MenuItem("Menu Item 1")
        self.complain.append(self.complain_menu1)
        self.complain_menu2 = Gtk.MenuItem("Menu Item 2")
        self.complain.append(self.complain_menu2)
        self.menu.append(self.complain_dropdown)
        self.reports = Gtk.Menu()
        self.reports_dropdown = Gtk.MenuItem("REPORTS")
        self.reports_dropdown.set_submenu(self.reports)
        self.reports_menu1 = Gtk.MenuItem("Menu Item 1")
        self.reports.append(self.reports_menu1)
        self.menu.append(self.reports_dropdown)
        self.logout_dropdown = Gtk.MenuItem("LOGOUT")
        self.menu.append(self.logout_dropdown)
        self.logout_dropdown.connect("activate", self.logout_call)

        self.hbox2.set_hexpand(True)
        self.dashboard_dropdown.set_property("margin_left", 20)
        self.dashboard_dropdown.set_property("margin_right", 10)
        self.admin_dropdown.set_property("margin_left", 10)
        self.admin_dropdown.set_property("margin_right", 10)
        self.master_dropdown.set_property("margin_left", 10)
        self.master_dropdown.set_property("margin_right", 10)
        self.schedule_dropdown.set_property("margin_left", 10)
        self.schedule_dropdown.set_property("margin_right", 10)
        self.complain_dropdown.set_property("margin_left", 10)
        self.complain_dropdown.set_property("margin_right", 10)
        self.reports_dropdown.set_property("margin_left", 10)
        self.reports_dropdown.set_property("margin_right", 1158)
        self.logout_dropdown.set_property("margin_right", 30)

        self.hbox2.set_halign(Gtk.Align.START)
        self.hbox2.pack_start(self.menu, True, True, 0)

        self.search_label = Gtk.Label("Enter the equipment to be searched :")
        self.search_label.set_property("margin_top", 100)
        self.search_label.set_property("margin_bottom", 10)
        self.hbox3.pack_start(self.search_label, False, False, 0)
        self.search = Gtk.Entry()
        self.search.set_property("margin_top", 10)
        self.search.set_property("margin_bottom", 10)
        self.hbox3.pack_start(self.search, False, False, 0)
        self.search_button = Gtk.Button("Search")
        self.search_button.set_property("margin_top", 10)
        self.search_button.set_property("margin_bottom", 10)
        self.search_button.set_property("margin_left", 40)
        self.search_button.set_property("margin_right", 40)
        self.hbox3.pack_start(self.search_button, False, False, 0)

        self.hbox3.set_halign(Gtk.Align.CENTER)

        self.new_button = Gtk.Button("Schedule new service")
        self.new_button.set_property("margin_top", 10)
        self.new_button.set_property("margin_left", 40)
        self.new_button.set_property("margin_right", 40)
        self.hbox3.pack_start(self.new_button, False, False, 0)

        self.new_button.connect("clicked", self.call_schedule_form)
        self.search_button.connect("clicked", self.search_button_clicked)

        self.add(self.box)
        self.show_all()
        return

    def call_schedule_form(self, widget):
        global equip_sl_no
        if equip_sl_no == None:
            dialog_empty_form = equipment_form_empty(self)
            response = dialog_empty_form.run()
            dialog_empty_form.destroy()
            return
        new_window = Schedule_service()
        new_window.set_position(Gtk.WindowPosition.CENTER)
        new_window.connect("delete-event", Gtk.main_quit)
        new_window.show_all()
        Gtk.main()
        return

    def search_button_clicked(self, widget):
        global search_schedule
        search_schedule = self.search.get_text()
        try:
            details = auth.Schedule.objects.get(equip_name=search_schedule)
        except Exception as e:
            dialog_number = Search_error(self)
            response = dialog_number.run()
            dialog_number.destroy()
            return

        new_window = Search_schedule()
        new_window.set_position(Gtk.WindowPosition.CENTER)
        new_window.connect("delete-event", Gtk.main_quit)
        new_window.show_all()
        Gtk.main()
        return

    def call_equipment_list(self, widget):
        self.destroy()
        new_window = Equipment_list()
        new_window.set_position(Gtk.WindowPosition.CENTER)
        new_window.connect("delete-event", Gtk.main_quit)
        new_window.show_all()
        Gtk.main()
        return

    def call_schedule_list(self, widget):
        self.destroy()
        new_window = Schedule_list()
        new_window.set_position(Gtk.WindowPosition.CENTER)
        new_window.connect("delete-event", Gtk.main_quit)
        new_window.show_all()
        Gtk.main()
        return

    def call_assign_list(self, widget):
        self.destroy()
        new_window = Assign_list()
        new_window.set_position(Gtk.WindowPosition.CENTER)
        new_window.connect("delete-event", Gtk.main_quit)
        new_window.show_all()
        Gtk.main()
        return

    def logout_call(self, widget):
        self.destroy()
        window = Main_Window()
        window.set_position(Gtk.WindowPosition.CENTER)
        window.connect("delete-event", Gtk.main_quit)
        window.show_all()
        Gtk.main()
        return

#ASSIGN JOB LIST
class Assign_list(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self, title = "Job Assign List")

        self.set_border_width(5)
        self.set_default_size(1920,1080)
        self.box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 0)
        self.hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.hbox3 = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 0)

        image = Gtk.Image()
        image.set_from_file('')
        self.hbox1.add(image)
        self.hbox1.set_hexpand(True)
        self.hbox1.set_halign(Gtk.Align.CENTER)
        self.hbox1.show_all()

        self.label = Gtk.Label()
        self.label.set_markup("<big><big><big><big><big><big><big><b>ASSIGNED JOBS</b></big></big></big></big></big></big></big>")
        self.box.pack_start(self.hbox1, False, False, 0)
        self.box.pack_start(self.hbox2, False, False, 0)
        self.box.pack_start(self.label, False, False, 0)
        self.box.pack_start(self.hbox3, False, False, 0)

        self.menu = Gtk.MenuBar()
        self.dashboard = Gtk.Menu()
        self.dashboard_dropdown = Gtk.MenuItem("DASHBOARD")
        self.dashboard_dropdown.set_submenu(self.dashboard)
        self.dashboard_menu1 = Gtk.MenuItem("Menu Item 1")
        self.dashboard.append(self.dashboard_menu1)
        self.dashboard_menu2 = Gtk.MenuItem("Menu Item 2")
        self.dashboard.append(self.dashboard_menu2)
        self.dashboard_menu3 = Gtk.MenuItem("Menu Item 3")
        self.dashboard.append(self.dashboard_menu3)
        self.menu.append(self.dashboard_dropdown)
        self.admin = Gtk.Menu()
        self.admin_dropdown = Gtk.MenuItem("ADMIN")
        self.admin_dropdown.set_submenu(self.admin)
        self.admin_menu1 = Gtk.MenuItem("Menu Item 1")
        self.admin.append(self.admin_menu1)
        self.admin_menu2 = Gtk.MenuItem("Menu Item 2")
        self.admin.append(self.admin_menu2)
        self.admin_menu3 = Gtk.MenuItem("Menu Item 3")
        self.admin.append(self.admin_menu3)
        self.menu.append(self.admin_dropdown)
        self.master = Gtk.Menu()
        self.master_dropdown = Gtk.MenuItem("MASTER")
        self.master_dropdown.set_submenu(self.master)
        self.master_company = Gtk.MenuItem("Company")
        self.master.append(self.master_company)
        self.master_department = Gtk.MenuItem("Department")
        self.master.append(self.master_department)
        self.master_equipment = Gtk.MenuItem("Equipment")
        self.master_equipment.connect("activate", self.call_equipment_list)
        self.master.append(self.master_equipment)
        self.menu.append(self.master_dropdown)
        self.Schedule_menu = Gtk.Menu()
        self.schedule_dropdown = Gtk.MenuItem("SCHEDULE")
        self.schedule_dropdown.set_submenu(self.Schedule_menu)
        self.schedule_schedule = Gtk.MenuItem("Schedule")
        self.schedule_schedule.connect("activate", self.call_schedule_list)
        self.assign_schedule = Gtk.MenuItem("Assign Job")
        self.assign_schedule.connect("activate", self.call_assign_list)
        self.Schedule_menu.append(self.schedule_schedule)
        self.Schedule_menu.append(Gtk.SeparatorMenuItem())
        self.Schedule_menu.append(self.assign_schedule)
        self.menu.append(self.schedule_dropdown)
        self.complain = Gtk.Menu()
        self.complain_dropdown = Gtk.MenuItem("COMPLAIN")
        self.complain_dropdown.set_submenu(self.complain)
        self.complain_menu1 = Gtk.MenuItem("Menu Item 1")
        self.complain.append(self.complain_menu1)
        self.complain_menu2 = Gtk.MenuItem("Menu Item 2")
        self.complain.append(self.complain_menu2)
        self.menu.append(self.complain_dropdown)
        self.reports = Gtk.Menu()
        self.reports_dropdown = Gtk.MenuItem("REPORTS")
        self.reports_dropdown.set_submenu(self.reports)
        self.reports_menu1 = Gtk.MenuItem("Menu Item 1")
        self.reports.append(self.reports_menu1)
        self.menu.append(self.reports_dropdown)
        self.logout_dropdown = Gtk.MenuItem("LOGOUT")
        self.menu.append(self.logout_dropdown)
        self.logout_dropdown.connect("activate", self.logout_call)

        self.hbox2.set_hexpand(True)
        self.dashboard_dropdown.set_property("margin_left", 20)
        self.dashboard_dropdown.set_property("margin_right", 10)
        self.admin_dropdown.set_property("margin_left", 10)
        self.admin_dropdown.set_property("margin_right", 10)
        self.master_dropdown.set_property("margin_left", 10)
        self.master_dropdown.set_property("margin_right", 10)
        self.schedule_dropdown.set_property("margin_left", 10)
        self.schedule_dropdown.set_property("margin_right", 10)
        self.complain_dropdown.set_property("margin_left", 10)
        self.complain_dropdown.set_property("margin_right", 10)
        self.reports_dropdown.set_property("margin_left", 10)
        self.reports_dropdown.set_property("margin_right", 1158)
        self.logout_dropdown.set_property("margin_right", 30)

        self.hbox2.set_halign(Gtk.Align.START)
        self.hbox2.pack_start(self.menu, True, True, 0)

        self.search_label = Gtk.Label("Enter the equipment to be searched :")
        self.search_label.set_property("margin_top", 100)
        self.search_label.set_property("margin_bottom", 10)
        self.hbox3.pack_start(self.search_label, False, False, 0)
        self.search = Gtk.Entry()
        self.search.set_property("margin_top", 10)
        self.search.set_property("margin_bottom", 10)
        self.hbox3.pack_start(self.search, False, False, 0)
        self.search_button = Gtk.Button("Search")
        self.search_button.set_property("margin_top", 10)
        self.search_button.set_property("margin_bottom", 10)
        self.search_button.set_property("margin_left", 40)
        self.search_button.set_property("margin_right", 40)
        self.hbox3.pack_start(self.search_button, False, False, 0)

        self.hbox3.set_halign(Gtk.Align.CENTER)

        self.new_button = Gtk.Button("Assign New Job")
        self.new_button.set_property("margin_top", 10)
        self.new_button.set_property("margin_left", 40)
        self.new_button.set_property("margin_right", 40)
        self.hbox3.pack_start(self.new_button, False, False, 0)

        self.new_button.connect("clicked", self.call_assign_form)
        self.search_button.connect("clicked", self.search_button_clicked)

        self.add(self.box)
        self.show_all()
        return

    def call_assign_form(self, widget):
        global owner
        if owner == None:
            dialog_empty_form = schedule_form_empty(self)
            response = dialog_empty_form.run()
            dialog_empty_form.destroy()

            return
        new_window = Assign_Job()
        new_window.set_position(Gtk.WindowPosition.CENTER)
        new_window.connect("delete-event", Gtk.main_quit)
        new_window.show_all()
        Gtk.main()
        return

    def search_button_clicked(self, widget):
        global search_assign
        search_assign = self.search.get_text()
        try:
            details = auth.Assign.objects.get(equip_name=search_assign)
        except Exception as e:
            dialog_number = Search_error(self)
            response = dialog_number.run()
            dialog_number.destroy()
            return

        new_window = Search_assign()
        new_window.set_position(Gtk.WindowPosition.CENTER)
        new_window.connect("delete-event", Gtk.main_quit)
        new_window.show_all()
        Gtk.main()
        return

    def call_equipment_list(self, widget):
        self.destroy()
        new_window = Equipment_list()
        new_window.set_position(Gtk.WindowPosition.CENTER)
        new_window.connect("delete-event", Gtk.main_quit)
        new_window.show_all()
        Gtk.main()
        return

    def call_schedule_list(self, widget):
        self.destroy()
        new_window = Schedule_list()
        new_window.set_position(Gtk.WindowPosition.CENTER)
        new_window.connect("delete-event", Gtk.main_quit)
        new_window.show_all()
        Gtk.main()
        return

    def call_assign_list(self, widget):
        self.destroy()
        new_window = Assign_list()
        new_window.set_position(Gtk.WindowPosition.CENTER)
        new_window.connect("delete-event", Gtk.main_quit)
        new_window.show_all()
        Gtk.main()
        return

    def logout_call(self, widget):
        self.destroy()
        window = Main_Window()
        window.set_position(Gtk.WindowPosition.CENTER)
        window.connect("delete-event", Gtk.main_quit)
        window.show_all()
        Gtk.main()
        return

#EQUIPMENT FORM
class Equipment_form(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Equipment Details Form")
        self.set_border_width(10)
        self.set_default_size(850, 300)

        self.hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)

        self.hbox.pack_start(self.vbox_left, True, True, 0)
        self.hbox.pack_start(self.vbox_right, True, True, 0)

        self.department_label = Gtk.Label()
        self.department_label.set_markup("<b>Department</b>")
        self.vbox_left.pack_start(self.department_label, True, True, 3)
        self.department = Gtk.Entry()
        self.vbox_left.pack_start(self.department, True, True, 3)

        self.department_list = ["A", "B", "C", "D"]
        completion_department = Gtk.EntryCompletion()
        self.department_liststore = Gtk.ListStore(str)
        for text in self.department_list:
            self.department_liststore.append([text])

        completion_department.set_model(self.department_liststore)
        completion_department.set_text_column(0)
        self.department.set_completion(completion_department)

        self.location_label = Gtk.Label()
        self.location_label.set_markup("<b>Location</b>")
        self.vbox_left.pack_start(self.location_label, True, True, 3)
        self.location = Gtk.Entry()
        self.vbox_left.pack_start(self.location, True, True, 3)
        self.trade_label = Gtk.Label()
        self.trade_label.set_markup("<b>Trade</b>")
        self.vbox_left.pack_start(self.trade_label, True, True, 3)
        self.trade = Gtk.Entry()
        self.vbox_left.pack_start(self.trade, True, True, 3)
        self.equipment_code_label = Gtk.Label()
        self.equipment_code_label.set_markup("<b>Equipment Code</b>")
        self.vbox_left.pack_start(self.equipment_code_label, True, True, 3)
        self.equipment_code = Gtk.Entry()
        self.vbox_left.pack_start(self.equipment_code, True, True, 3)
        self.equipment_sl_no_label = Gtk.Label()
        self.equipment_sl_no_label.set_markup("<b>Equipment Sl. No.</b>")
        self.vbox_left.pack_start(self.equipment_sl_no_label, True, True, 3)
        self.equipment_sl_no = Gtk.Entry()
        self.vbox_left.pack_start(self.equipment_sl_no, True, True, 3)

        self.section_label = Gtk.Label()
        self.section_label.set_markup("<b>Section</b>")
        self.vbox_right.pack_start(self.section_label, False, True, 3)
        self.section = Gtk.Entry()

        self.section_list = ["A1", "A2","A3","B1","B2","B3","C1","C2","C3","D1","D2","D3"]
        completion_section = Gtk.EntryCompletion()
        self.section_liststore = Gtk.ListStore(str)
        for text in self.section_list:
            self.section_liststore.append([text])
        completion_section.set_model(self.section_liststore)
        completion_section.set_text_column(0)
        self.section.set_completion(completion_section)

        self.vbox_right.pack_start(self.section, False, True, 3)
        self.sub_location_label = Gtk.Label()
        self.sub_location_label.set_markup("<b>Sub Location</b>")
        self.vbox_right.pack_start(self.sub_location_label, False, True, 3)
        self.sub_location = Gtk.Entry()
        self.vbox_right.pack_start(self.sub_location, False, True, 3)
        self.category_label = Gtk.Label()
        self.category_label.set_markup("<b>Category</b>")
        self.vbox_right.pack_start(self.category_label, False, True, 3)
        self.category = Gtk.Entry()
        self.vbox_right.pack_start(self.category, False, True, 3)
        self.equipment_label = Gtk.Label()
        self.equipment_label.set_markup("<b>Equipment</b>")
        self.vbox_right.pack_start(self.equipment_label, False, True, 3)
        self.equipment = Gtk.Entry()
        self.vbox_right.pack_start(self.equipment, False, True, 3)
        self.state_label = Gtk.Label()
        self.state_label.set_markup("<b>State</b>")
        self.vbox_right.pack_start(self.state_label, False, True, 3)
        self.state = Gtk.Switch()
        self.vbox_right.pack_start(self.state, False, True, 3)

        self.save = Gtk.Button("Save")
        self.cancel = Gtk.Button("Cancel")
        self.vbox_right.pack_start(self.save, True, True, 3)
        self.vbox_right.pack_start(self.cancel, True, True, 3)

        self.save.connect("clicked", self.save_equip_form)
        self.cancel.connect("clicked", self.cancel_form)

        self.add(self.hbox)

        return

    def save_equip_form(self, widget):
        if len(self.department.get_text()) == 0 or \
                len(self.trade.get_text()) == 0 or \
                len(self.equipment_code.get_text()) == 0 or \
                len(self.equipment_sl_no.get_text()) == 0 or \
                len(self.section.get_text()) == 0 or \
                len(self.sub_location.get_text()) == 0 or \
                len(self.category.get_text()) == 0 or \
                len(self.equipment.get_text()) == 0:
            dialog_error = Error(self)
            response = dialog_error.run()

            dialog_error.destroy()
            return

        else:

            result = newAuth.equipment_form(
                self.department.get_text(),
                self.location.get_text(),
                self.trade.get_text(),
                self.equipment_code.get_text(),
                self.equipment_sl_no.get_text(),
                self.section.get_text(),
                self.sub_location.get_text(),
                self.category.get_text(),
                self.equipment.get_text(),
                self.state.get_state())
            if result:

                global equip_sl_no
                equip_sl_no = self.equipment_sl_no.get_text()
                self.destroy()
                dialog_equip_form_saved = form_saved(self)
                response = dialog_equip_form_saved.run()

                dialog_equip_form_saved.destroy()
                return
            else:
                dialog_equip_form_save_error = form_save_error(self)
                response = dialog_equip_form_save_error.run()

                dialog_equip_form_save_error.destroy()
                return

    def cancel_form(self, widget):
        self.destroy()
        return

#SEARCH EQUIPMENT FORM
class Search_equip(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self, title="Equipment Details")
        self.set_border_width(10)
        self.set_default_size(850, 300)

        self.hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)

        self.hbox.pack_start(self.vbox_left, True, True, 0)
        self.hbox.pack_start(self.vbox_right, True, True, 0)

        global search_equip
        try:
            details = auth.Equipment.objects.get(equipment_name=search_equip)
        except Exception as e:
            dialog_number = Search_error(self)
            response = dialog_number.run()
            dialog_number.destroy()
            return

        self.department_label = Gtk.Label()
        self.department_label.set_markup("<b>Department</b>")
        self.vbox_left.pack_start(self.department_label, True, True, 3)
        self.department = Gtk.Entry()
        self.department.set_text(details.department)
        self.vbox_left.pack_start(self.department, True, True, 3)
        self.location_label = Gtk.Label()
        self.location_label.set_markup("<b>Location</b>")
        self.vbox_left.pack_start(self.location_label, True, True, 3)
        self.location = Gtk.Entry()
        self.location.set_text(details.location)
        self.vbox_left.pack_start(self.location, True, True, 3)
        self.trade_label = Gtk.Label()
        self.trade_label.set_markup("<b>Trade</b>")
        self.vbox_left.pack_start(self.trade_label, True, True, 3)
        self.trade = Gtk.Entry()
        self.trade.set_text(details.trade)
        self.vbox_left.pack_start(self.trade, True, True, 3)
        self.equipment_code_label = Gtk.Label()
        self.equipment_code_label.set_markup("<b>Equipment Code</b>")
        self.vbox_left.pack_start(self.equipment_code_label, True, True, 3)
        self.equipment_code = Gtk.Entry()
        self.equipment_code.set_text(details.equip_code)
        self.vbox_left.pack_start(self.equipment_code, True, True, 3)
        self.equipment_sl_no_label = Gtk.Label()
        self.equipment_sl_no_label.set_markup("<b>Equipment Sl. No.</b>")
        self.vbox_left.pack_start(self.equipment_sl_no_label, True, True, 3)
        self.equipment_sl_no = Gtk.Entry()
        self.equipment_sl_no.set_text(details.equip_sl_no)
        self.vbox_left.pack_start(self.equipment_sl_no, True, True, 3)

        self.section_label = Gtk.Label()
        self.section_label.set_markup("<b>Section</b>")
        self.vbox_right.pack_start(self.section_label, False, True, 3)
        self.section = Gtk.Entry()
        self.section.set_text(details.section)
        self.vbox_right.pack_start(self.section, False, True, 3)
        self.sub_location_label = Gtk.Label()
        self.sub_location_label.set_markup("<b>Sub Location</b>")
        self.vbox_right.pack_start(self.sub_location_label, False, True, 3)
        self.sub_location = Gtk.Entry()
        self.sub_location.set_text(details.sub_loc)
        self.vbox_right.pack_start(self.sub_location, False, True, 3)
        self.category_label = Gtk.Label()
        self.category_label.set_markup("<b>Category</b>")
        self.vbox_right.pack_start(self.category_label, False, True, 3)
        self.category = Gtk.Entry()
        self.category.set_text(details.category)
        self.vbox_right.pack_start(self.category, False, True, 3)
        self.equipment_label = Gtk.Label()
        self.equipment_label.set_markup("<b>Equipment</b>")
        self.vbox_right.pack_start(self.equipment_label, False, True, 3)
        self.equipment = Gtk.Entry()
        self.equipment.set_text(search_equip)
        self.vbox_right.pack_start(self.equipment, False, True, 3)
        self.state_label = Gtk.Label()
        self.state_label.set_markup("<b>State</b>")
        self.vbox_right.pack_start(self.state_label, False, True, 3)
        self.state = Gtk.Switch()
        self.state.set_state(details.state)
        self.vbox_right.pack_start(self.state, False, True, 3)

        self.ok_button = Gtk.Button("OK")
        self.vbox_right.pack_start(self.ok_button, False, False, 3)
        self.ok_button.connect("clicked", self.ok_button_clicked)

        self.add(self.hbox)

        return

    def ok_button_clicked(self, widget):
        self.destroy()
        return

#SCHEDULE FORM
class Schedule_service(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self, title = "Schedule Service")
        self.set_border_width(10)
        self.set_default_size(850, 300)

        self.hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)

        self.hbox.pack_start(self.vbox_left, True, True, 0)
        self.hbox.pack_start(self.vbox_right, True, True, 0)

        global equip_sl_no
        details = auth.Equipment.objects.get(equip_sl_no = equip_sl_no)
        section = details.section
        sub_loc = details.sub_loc

        self.section_label = Gtk.Label("Section")
        self.section = Gtk.Entry()
        self.section.set_text(section)
        self.vbox_left.pack_start(self.section_label, True, True, 3)
        self.vbox_left.pack_start(self.section, True, True, 3)
        self.sub_loc_label = Gtk.Label("Sub Location")
        self.sub_loc = Gtk.Entry()
        self.sub_loc.set_text(sub_loc)
        self.vbox_left.pack_start(self.sub_loc_label, True, True, 3)
        self.vbox_left.pack_start(self.sub_loc, True, True, 3)
        self.task_label = Gtk.Label("Task")
        self.task = Gtk.Entry()
        self.vbox_left.pack_start(self.task_label, True,True, 3)
        self.vbox_left.pack_start(self.task, True,True, 3)
        self.inform_to_label = Gtk.Label("Inform to (If any)")
        self.inform_to =Gtk.Entry()
        self.vbox_left.pack_start(self.inform_to_label, True, True, 3)
        self.vbox_left.pack_start(self.inform_to, True, True, 3)
        self.prev_main_label = Gtk.Label("Preventive Maintenance")
        self.prev_main = Gtk.Entry()
        self.vbox_left.pack_start(self.prev_main_label, True, True, 3)
        self.vbox_left.pack_start(self.prev_main, True, True, 3)
        self.freque_label  = Gtk.Label("PM Frequency(in days)")
        self.freque = Gtk.Entry()
        self.vbox_left.pack_start(self.freque_label, True, True, 3)
        self.vbox_left.pack_start(self.freque, True, True, 3)
        self.reminder_label = Gtk.Label("Reminder before PM date(in days)")
        self.reminder = Gtk.Entry()
        self.vbox_left.pack_start(self.reminder_label, True, True, 3)
        self.vbox_left.pack_start(self.reminder, True, True, 3)

        loc = details.location
        equip = details.equipment_name

        self.loc_label = Gtk.Label("Location")
        self.loc = Gtk.Entry()
        self.loc.set_text(loc)
        self.vbox_right.pack_start(self.loc_label, True, True, 3)
        self.vbox_right.pack_start(self.loc, True, True, 3)
        self.equip_label = Gtk.Label("Equipment")
        self.equip = Gtk.Entry()
        self.equip.set_text(equip)
        self.vbox_right.pack_start(self.equip_label, True, True, 3)
        self.vbox_right.pack_start(self.equip, True, True, 3)
        self.owner_label = Gtk.Label("PM Owner")
        self.owner = Gtk.Entry()
        self.vbox_right.pack_start(self.owner_label, True, True, 3)
        self.vbox_right.pack_start(self.owner, True, True, 3)
        self.code_label = Gtk.Label("PM Code")
        self.code = Gtk.Entry()
        self.vbox_right.pack_start(self.code_label, True, True, 3)
        self.vbox_right.pack_start(self.code, True, True, 3)
        self.date_label = Gtk.Label("PM Date")
        self.date = Gtk.Entry()
        self.date.set_text("yyyy/mm/dd")
        self.vbox_right.pack_start(self.date_label, True, True, 3)
        self.vbox_right.pack_start(self.date, True, True, 3)
        self.next_date_label = Gtk.Label("Next PM Date")
        self.vbox_right.pack_start(self.next_date_label, True, True, 3)
        self.next_date = Gtk.Entry()
        self.next_date.set_text("yyyy/mm/dd")
        self.vbox_right.pack_start(self.next_date, True, True, 3)

        self.calculate = Gtk.Button("Calculate")
        self.save_button = Gtk.Button("Save")
        self.cancel_button = Gtk.Button("Cancel")
        self.vbox_right.pack_start(self.calculate, True, True, 3)
        self.vbox_right.pack_start(self.save_button, True, True, 3)
        self.vbox_right.pack_start(self.cancel_button, True, True, 3)
        self.calculate.connect("clicked", self.Calculate)
        self.save_button.connect("clicked", self.save_form)
        self.cancel_button.connect("clicked", self.cancel_form)

        self.add(self.hbox)
        return

    def Calculate(self, widget):
        year = int(self.date.get_text()[0:4])
        month = int(self.date.get_text()[5:7])
        day = int(self.date.get_text()[8:])
        freq = int(self.freque.get_text())
        entered_date = datetime.date(year, month, day)
        diff = datetime.timedelta(days=freq)
        new_date = entered_date + diff
        self.next_date.set_text(str(new_date))
        return


    def save_form(self, widget):
        if len(self.section.get_text()) == 0 or \
            len(self.sub_loc.get_text()) == 0 or\
            len(self.task.get_text()) == 0 or\
            len(self.prev_main.get_text()) == 0 or\
            len(self.freque.get_text()) == 0 or\
            len(self.reminder.get_text()) == 0 or\
            len(self.loc.get_text()) == 0 or\
            len(self.equip.get_text()) == 0 or\
            len(self.owner.get_text()) == 0 or\
            len(self.code.get_text()) == 0 or\
            len(self.date.get_text()) == 0 or\
            len(self.next_date.get_text()) == 0:
            dialog_error = Error(self)
            response = dialog_error.run()

            dialog_error.destroy()
            return
        else:
            result = newAuth.schedule_form(
                self.section.get_text(),
                self.sub_loc.get_text(),
                self.task.get_text(),
                self.inform_to.get_text(),
                self.prev_main.get_text(),
                self.freque.get_text(),
                self.reminder.get_text(),
                self.loc.get_text(),
                self.equip.get_text(),
                self.owner.get_text(),
                self.code.get_text(),
                self.date.get_text(),
                self.next_date.get_text())
            if result:
                global owner
                owner = self.owner.get_text()
                self.destroy()
                dialog_equip_form_saved = form_saved(self)
                response = dialog_equip_form_saved.run()

                dialog_equip_form_saved.destroy()
                return
            else:
                dialog_schedule_form_save_error = form_save_error(self)
                response = dialog_schedule_form_save_error.run()

                dialog_schedule_form_save_error.destroy()
                return

    def cancel_form(self, widget):
        self.destroy()
        return

#SEARCH SCHEDULE FORM
class Search_schedule(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self, title="Equipment Details")
        self.set_border_width(10)
        self.set_default_size(850, 300)

        self.hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)

        self.hbox.pack_start(self.vbox_left, True, True, 0)
        self.hbox.pack_start(self.vbox_right, True, True, 0)

        global search_schedule
        try:
            details = auth.Schedule.objects.get(equip_name=search_schedule)
        except Exception as e:
            dialog_number = Search_error(self)
            response = dialog_number.run()
            dialog_number.destroy()
            return

        self.section_label = Gtk.Label("Section")
        self.section = Gtk.Entry()
        self.section.set_text(details.section)
        self.vbox_left.pack_start(self.section_label, True, True, 3)
        self.vbox_left.pack_start(self.section, True, True, 3)
        self.sub_loc_label = Gtk.Label("Sub Location")
        self.sub_loc = Gtk.Entry()
        self.sub_loc.set_text(details.sub_loc)
        self.vbox_left.pack_start(self.sub_loc_label, True, True, 3)
        self.vbox_left.pack_start(self.sub_loc, True, True, 3)
        self.task_label = Gtk.Label("Task")
        self.task = Gtk.Entry()
        self.task.set_text(details.task)
        self.vbox_left.pack_start(self.task_label, True, True, 3)
        self.vbox_left.pack_start(self.task, True, True, 3)
        self.inform_to_label = Gtk.Label("Inform to (If any)")
        self.inform_to = Gtk.Entry()
        self.inform_to.set_text(details.inform_to)
        self.vbox_left.pack_start(self.inform_to_label, True, True, 3)
        self.vbox_left.pack_start(self.inform_to, True, True, 3)
        self.prev_main_label = Gtk.Label("Preventive Maintenance")
        self.prev_main = Gtk.Entry()
        self.prev_main.set_text(details.prev_main)
        self.vbox_left.pack_start(self.prev_main_label, True, True, 3)
        self.vbox_left.pack_start(self.prev_main, True, True, 3)
        self.freque_label = Gtk.Label("PM Frequency(in days)")
        self.freque = Gtk.Entry()
        self.freque.set_text(details.freq)
        self.vbox_left.pack_start(self.freque_label, True, True, 3)
        self.vbox_left.pack_start(self.freque, True, True, 3)
        self.reminder_label = Gtk.Label("Reminder before PM date(in days)")
        self.reminder = Gtk.Entry()
        self.reminder.set_text(details.reminder)
        self.vbox_left.pack_start(self.reminder_label, True, True, 3)
        self.vbox_left.pack_start(self.reminder, True, True, 3)

        self.loc_label = Gtk.Label("Location")
        self.loc = Gtk.Entry()
        self.loc.set_text(details.loc)
        self.vbox_right.pack_start(self.loc_label, True, True, 3)
        self.vbox_right.pack_start(self.loc, True, True, 3)
        self.equip_label = Gtk.Label("Equipment")
        self.equip = Gtk.Entry()
        self.equip.set_text(details.equip_name)
        self.vbox_right.pack_start(self.equip_label, True, True, 3)
        self.vbox_right.pack_start(self.equip, True, True, 3)
        self.owner_label = Gtk.Label("PM Owner")
        self.owner = Gtk.Entry()
        self.owner.set_text(details.owner)
        self.vbox_right.pack_start(self.owner_label, True, True, 3)
        self.vbox_right.pack_start(self.owner, True, True, 3)
        self.code_label = Gtk.Label("PM Code")
        self.code = Gtk.Entry()
        self.code.set_text(details.code)
        self.vbox_right.pack_start(self.code_label, True, True, 3)
        self.vbox_right.pack_start(self.code, True, True, 3)
        self.date_label = Gtk.Label("PM Date")
        self.date = Gtk.Entry()
        self.date.set_text(details.date)
        self.vbox_right.pack_start(self.date_label, True, True, 3)
        self.vbox_right.pack_start(self.date, True, True, 3)
        self.next_date_label = Gtk.Label("Next PM Date")
        self.vbox_right.pack_start(self.next_date_label, True, True, 3)
        self.next_date = Gtk.Entry()
        self.next_date.set_text(details.next_date)
        self.vbox_right.pack_start(self.next_date, True, True, 3)

        self.ok_button = Gtk.Button("OK")
        self.vbox_right.pack_start(self.ok_button, False, False, 3)
        self.ok_button.connect("clicked", self.ok_button_clicked)

        self.add(self.hbox)

        return

    def ok_button_clicked(self, widget):
        self.destroy()
        return

#ASSIGN JOB FORM
class Assign_Job(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Assign Job")
        self.set_border_width(10)
        self.set_default_size(850, 300)

        self.hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)

        self.hbox.pack_start(self.vbox_left, True, True, 0)
        self.hbox.pack_start(self.vbox_right, True, True, 0)

        global owner
        details = auth.Schedule.objects.get(owner= owner)

        section = details.section
        sub_loc = details.sub_loc
        task = details.task
        inform_to = details.inform_to
        prev_main = details.prev_main
        freque = details.freq
        reminder = details.reminder

        self.section_label = Gtk.Label("Section")
        self.section = Gtk.Entry()
        self.section.set_text(section)
        self.vbox_left.pack_start(self.section_label, True, True, 3)
        self.vbox_left.pack_start(self.section, True, True, 3)
        self.sub_loc_label = Gtk.Label("Sub Location")
        self.sub_loc = Gtk.Entry()
        self.sub_loc.set_text(sub_loc)
        self.vbox_left.pack_start(self.sub_loc_label, True, True, 3)
        self.vbox_left.pack_start(self.sub_loc, True, True, 3)
        self.task_label = Gtk.Label("Task")
        self.task = Gtk.Entry()
        self.task.set_text(task)
        self.vbox_left.pack_start(self.task_label, True, True, 3)
        self.vbox_left.pack_start(self.task, True, True, 3)
        self.inform_to_label = Gtk.Label("Inform to (If any)")
        self.inform_to = Gtk.Entry()
        self.inform_to.set_text(inform_to)
        self.vbox_left.pack_start(self.inform_to_label, True, True, 3)
        self.vbox_left.pack_start(self.inform_to, True, True, 3)
        self.prev_main_label = Gtk.Label("Preventive Maintenance")
        self.prev_main = Gtk.Entry()
        self.prev_main.set_text(prev_main)
        self.vbox_left.pack_start(self.prev_main_label, True, True, 3)
        self.vbox_left.pack_start(self.prev_main, True, True, 3)
        self.freque_label = Gtk.Label("PM Frequency(in days)")
        self.freque = Gtk.Entry()
        self.freque.set_text(freque)
        self.vbox_left.pack_start(self.freque_label, True, True, 3)
        self.vbox_left.pack_start(self.freque, True, True, 3)
        self.reminder_label = Gtk.Label("Reminder before PM date(in days)")
        self.reminder = Gtk.Entry()
        self.reminder.set_text(reminder)
        self.vbox_left.pack_start(self.reminder_label, True, True, 3)
        self.vbox_left.pack_start(self.reminder, True, True, 3)

        loc = details.loc
        equip = details.equip_name
        code = details.code
        date = details.date
        next_date = details.next_date

        self.loc_label = Gtk.Label("Location")
        self.loc = Gtk.Entry()
        self.loc.set_text(loc)
        self.vbox_right.pack_start(self.loc_label, True, True, 3)
        self.vbox_right.pack_start(self.loc, True, True, 3)
        self.equip_label = Gtk.Label("Equipment")
        self.equip = Gtk.Entry()
        self.equip.set_text(equip)
        self.vbox_right.pack_start(self.equip_label, True, True, 3)
        self.vbox_right.pack_start(self.equip, True, True, 3)
        self.owner_label = Gtk.Label("PM Owner")
        self.owner = Gtk.Entry()
        self.owner.set_text(owner)
        self.vbox_right.pack_start(self.owner_label, True, True, 3)
        self.vbox_right.pack_start(self.owner, True, True, 3)
        self.code_label = Gtk.Label("PM Code")
        self.code = Gtk.Entry()
        self.code.set_text(code)
        self.vbox_right.pack_start(self.code_label, True, True, 3)
        self.vbox_right.pack_start(self.code, True, True, 3)
        self.date_label = Gtk.Label("PM Date")
        self.date = Gtk.Entry()
        self.date.set_text(date)
        self.vbox_right.pack_start(self.date_label, True, True, 3)
        self.vbox_right.pack_start(self.date, True, True, 3)
        self.next_date_label = Gtk.Label("Next PM Date")
        self.vbox_right.pack_start(self.next_date_label, True, True, 3)
        self.next_date = Gtk.Entry()
        self.next_date.set_text(next_date)
        self.vbox_right.pack_start(self.next_date, True, True, 3)
        self.assign_label = Gtk.Label("Assign Job to")
        self.vbox_right.pack_start(self.assign_label, True, True, 3)
        self.assign = Gtk.Entry()
        self.vbox_right.pack_start(self.assign, True, True, 3)

        self.calculate = Gtk.Button("Calculate")
        self.save_button = Gtk.Button("Save")
        self.cancel_button = Gtk.Button("Cancel")
        self.vbox_left.pack_start(self.save_button, True, True, 3)
        self.vbox_right.pack_start(self.calculate, True, True, 3)
        self.vbox_right.pack_start(self.cancel_button, True, True, 3)
        self.calculate.connect("clicked", self.Calculate)
        self.save_button.connect("clicked", self.save_form)
        self.cancel_button.connect("clicked", self.cancel_form)

        self.add(self.hbox)
        return

    def Calculate(self, widget):
        year = int(self.date.get_text()[0:4])
        month = int(self.date.get_text()[5:7])
        day = int(self.date.get_text()[8:])
        freq = int(self.freque.get_text())
        entered_date = datetime.date(year, month, day)
        diff = datetime.timedelta(days=freq)
        new_date = entered_date + diff
        self.next_date.set_text(str(new_date))
        return

    def save_form(self, widget):
        if len(self.section.get_text()) == 0 or \
            len(self.sub_loc.get_text()) == 0 or\
            len(self.task.get_text()) == 0 or\
            len(self.prev_main.get_text()) == 0 or\
            len(self.freque.get_text()) == 0 or\
            len(self.reminder.get_text()) == 0 or\
            len(self.loc.get_text()) == 0 or\
            len(self.equip.get_text()) == 0 or\
            len(self.owner.get_text()) == 0 or\
            len(self.code.get_text()) == 0 or\
            len(self.date.get_text()) == 0 or\
            len(self.next_date.get_text()) == 0 or\
            len(self.assign.get_text()) == 0:
            dialog_error = Error(self)
            response = dialog_error.run()

            dialog_error.destroy()
            return
        else:
            result = newAuth.assign_form(
                self.section.get_text(),
                self.sub_loc.get_text(),
                self.task.get_text(),
                self.inform_to.get_text(),
                self.prev_main.get_text(),
                self.freque.get_text(),
                self.reminder.get_text(),
                self.loc.get_text(),
                self.equip.get_text(),
                self.owner.get_text(),
                self.code.get_text(),
                self.date.get_text(),
                self.next_date.get_text(),
                self.assign.get_text())
            if result:
                self.destroy()
                dialog_equip_form_saved = form_saved(self)
                response = dialog_equip_form_saved.run()

                dialog_equip_form_saved.destroy()
                return
            else:
                dialog_schedule_form_save_error = form_save_error(self)
                response = dialog_schedule_form_save_error.run()

                dialog_schedule_form_save_error.destroy()
                return

    def cancel_form(self, widget):
        self.destroy()
        return

#SEARCH ASSIGN JOB
class Search_assign(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self, title="Equipment Details")
        self.set_border_width(10)
        self.set_default_size(850, 300)

        self.hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)

        self.hbox.pack_start(self.vbox_left, True, True, 0)
        self.hbox.pack_start(self.vbox_right, True, True, 0)

        global search_assign
        try:
            details = auth.Assign.objects.get(equip_name=search_assign)
        except Exception as e:
            dialog_number = Search_error(self)
            response = dialog_number.run()
            dialog_number.destroy()
            return

        self.section_label = Gtk.Label("Section")
        self.section = Gtk.Entry()
        self.section.set_text(details.section)
        self.vbox_left.pack_start(self.section_label, True, True, 3)
        self.vbox_left.pack_start(self.section, True, True, 3)
        self.sub_loc_label = Gtk.Label("Sub Location")
        self.sub_loc = Gtk.Entry()
        self.sub_loc.set_text(details.sub_loc)
        self.vbox_left.pack_start(self.sub_loc_label, True, True, 3)
        self.vbox_left.pack_start(self.sub_loc, True, True, 3)
        self.task_label = Gtk.Label("Task")
        self.task = Gtk.Entry()
        self.task.set_text(details.task)
        self.vbox_left.pack_start(self.task_label, True, True, 3)
        self.vbox_left.pack_start(self.task, True, True, 3)
        self.inform_to_label = Gtk.Label("Inform to (If any)")
        self.inform_to = Gtk.Entry()
        self.inform_to.set_text(details.inform_to)
        self.vbox_left.pack_start(self.inform_to_label, True, True, 3)
        self.vbox_left.pack_start(self.inform_to, True, True, 3)
        self.prev_main_label = Gtk.Label("Preventive Maintenance")
        self.prev_main = Gtk.Entry()
        self.prev_main.set_text(details.prev_main)
        self.vbox_left.pack_start(self.prev_main_label, True, True, 3)
        self.vbox_left.pack_start(self.prev_main, True, True, 3)
        self.freque_label = Gtk.Label("PM Frequency(in days)")
        self.freque = Gtk.Entry()
        self.freque.set_text(details.freq)
        self.vbox_left.pack_start(self.freque_label, True, True, 3)
        self.vbox_left.pack_start(self.freque, True, True, 3)
        self.reminder_label = Gtk.Label("Reminder before PM date(in days)")
        self.reminder = Gtk.Entry()
        self.reminder.set_text(details.reminder)
        self.vbox_left.pack_start(self.reminder_label, True, True, 3)
        self.vbox_left.pack_start(self.reminder, True, True, 3)

        self.loc_label = Gtk.Label("Location")
        self.loc = Gtk.Entry()
        self.loc.set_text(details.loc)
        self.vbox_right.pack_start(self.loc_label, True, True, 3)
        self.vbox_right.pack_start(self.loc, True, True, 3)
        self.equip_label = Gtk.Label("Equipment")
        self.equip = Gtk.Entry()
        self.equip.set_text(details.equip_name)
        self.vbox_right.pack_start(self.equip_label, True, True, 3)
        self.vbox_right.pack_start(self.equip, True, True, 3)
        self.owner_label = Gtk.Label("PM Owner")
        self.owner = Gtk.Entry()
        self.owner.set_text(details.owner)
        self.vbox_right.pack_start(self.owner_label, True, True, 3)
        self.vbox_right.pack_start(self.owner, True, True, 3)
        self.code_label = Gtk.Label("PM Code")
        self.code = Gtk.Entry()
        self.code.set_text(details.code)
        self.vbox_right.pack_start(self.code_label, True, True, 3)
        self.vbox_right.pack_start(self.code, True, True, 3)
        self.date_label = Gtk.Label("PM Date")
        self.date = Gtk.Entry()
        self.date.set_text(details.date)
        self.vbox_right.pack_start(self.date_label, True, True, 3)
        self.vbox_right.pack_start(self.date, True, True, 3)
        self.next_date_label = Gtk.Label("Next PM Date")
        self.vbox_right.pack_start(self.next_date_label, True, True, 3)
        self.next_date = Gtk.Entry()
        self.next_date.set_text(details.next_date)
        self.vbox_right.pack_start(self.next_date, True, True, 3)
        self.assign_label = Gtk.Label("Assign Job to")
        self.vbox_right.pack_start(self.assign_label, True, True, 3)
        self.assign = Gtk.Entry()
        self.assign.set_text(details.assign)
        self.vbox_right.pack_start(self.assign, True, True, 3)

        self.ok_button = Gtk.Button("OK")
        self.vbox_right.pack_start(self.ok_button, False, False, 3)
        self.ok_button.connect("clicked", self.ok_button_clicked)

        self.add(self.hbox)

        return

    def ok_button_clicked(self, widget):
        self.destroy()
        return

#DIALOG BOXES
class Details(Gtk.Dialog):

    def __init__(self, parent):

        Gtk.Dialog.__init__(self, "Error", parent, Gtk.DialogFlags.MODAL,(Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.set_default_size(130, 80)
        self.set_border_width(20)
        self.set_position(Gtk.WindowPosition.CENTER)
        area = self.get_content_area()
        area.add(Gtk.Label("Username or Password Incorrect"))
        self.show_all()
        return


class Number(Gtk.Dialog):

    def __init__(self, parent):

        Gtk.Dialog.__init__(self, "Error", parent, Gtk.DialogFlags.MODAL, (Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.set_default_size(130, 80)
        self.set_border_width(20)
        self.set_position(Gtk.WindowPosition.CENTER)
        area = self.get_content_area()
        area.add(Gtk.Label("Invalid Personal Number or Password "))
        self.show_all()
        return


class Error(Gtk.Dialog):

    def __init__(self, parent):

        Gtk.Dialog.__init__(self, "Error", parent, Gtk.DialogFlags.MODAL,(Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.set_default_size(130, 80)
        self.set_border_width(20)
        self.set_position(Gtk.WindowPosition.CENTER)
        area = self.get_content_area()
        area.add(Gtk.Label("Please enter all the details"))
        self.show_all()
        return


class Exists(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Error", parent, Gtk.DialogFlags.MODAL, (Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.set_default_size(130, 80)
        self.set_border_width(20)
        self.set_position(Gtk.WindowPosition.CENTER)
        area = self.get_content_area()
        area.add(Gtk.Label("User already exists."))
        self.show_all()
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
        return


class equipment_form_empty(Gtk.Dialog):

    def __init__(self, parent):

        Gtk.Dialog.__init__(self, "Error", parent, Gtk.DialogFlags.MODAL, (Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.set_default_size(130, 80)
        self.set_border_width(20)
        self.set_position(Gtk.WindowPosition.CENTER)
        area = self.get_content_area()
        area.add(Gtk.Label("Please fill the equipment form before filling the Schedule form."))
        self.show_all()
        return


class schedule_form_empty(Gtk.Dialog):

    def __init__(self, parent):

        Gtk.Dialog.__init__(self, "Error", parent, Gtk.DialogFlags.MODAL, (Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.set_default_size(130, 80)
        self.set_border_width(20)
        self.set_position(Gtk.WindowPosition.CENTER)
        area = self.get_content_area()
        area.add(Gtk.Label("Please fill the Schedule form before filling the Assign form."))
        self.show_all()
        return


class form_saved(Gtk.Dialog):

    def __init__(self, parent):

        Gtk.Dialog.__init__(self, "Equipment form saved.", parent, Gtk.DialogFlags.MODAL, (Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.set_default_size(130, 80)
        self.set_border_width(20)
        self.set_position(Gtk.WindowPosition.CENTER)
        area = self.get_content_area()
        area.add(Gtk.Label("Form saved successfully."))
        self.show_all()
        return


class form_save_error(Gtk.Dialog):

    def __init__(self, parent):

        Gtk.Dialog.__init__(self, "Error", parent, Gtk.DialogFlags.MODAL, (Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.set_default_size(130, 80)
        self.set_border_width(20)
        self.set_position(Gtk.WindowPosition.CENTER)
        area = self.get_content_area()
        area.add(Gtk.Label("There is a problem in saving the form. Please try again."))
        self.show_all()
        return


class Search_error(Gtk.Dialog):
    def __init__(self, parent):

        Gtk.Dialog.__init__(self, "Error", parent, Gtk.DialogFlags.MODAL, (Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.set_default_size(130, 80)
        self.set_border_width(20)
        self.set_position(Gtk.WindowPosition.CENTER)
        area = self.get_content_area()
        area.add(Gtk.Label("Please enter a valid equipment name."))
        self.show_all()
        return


window = Main_Window()
window.set_position(Gtk.WindowPosition.CENTER)
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
