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

            result = newAuth.reg(self.name.get_text(),self.personal_number.get_text(),self.password.get_text())

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


class Number(Gtk.Dialog):

    def __init__(self, parent):

        Gtk.Dialog.__init__(self, "Error", parent, Gtk.DialogFlags.MODAL, (Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.set_default_size(130, 80)
        self.set_border_width(20)
        self.set_position(Gtk.WindowPosition.CENTER)
        area = self.get_content_area()
        area.add(Gtk.Label("Invalid Personal Number or Password "))
        self.show_all()






class Exists(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Error", parent, Gtk.DialogFlags.MODAL, (Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.set_default_size(130, 80)
        self.set_border_width(20)
        self.set_position(Gtk.WindowPosition.CENTER)
        area = self.get_content_area()
        area.add(Gtk.Label("User already exists."))
        self.show_all()

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
        self.parent_equipment_label = Gtk.Label()
        self.parent_equipment_label.set_markup("<b>Parent Equipment</b>")
        self.vbox_left.pack_start(self.parent_equipment_label, True, True, 3)
        self.parent_equipment = Gtk.Entry()
        self.vbox_left.pack_start(self.parent_equipment, True, True, 3)


        self.section_label = Gtk.Label()
        self.section_label.set_markup("<b>Section</b>")
        self.vbox_right.pack_start(self.section_label, False, True, 3)
        self.section = Gtk.Entry()
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

        self.add(self.hbox)

        return

    def save_equip_form(self, widget):
        if len(self.department.get_text()) == 0 or len(self.location.get_text()) == 0 or len(self.trade.get_text()) == 0 or len(self.equipment_code.get_text()) == 0 or len(self.equipment_sl_no.get_text()) == 0 or len(self.parent_equipment.get_text()) == 0 or len(self.section.get_text()) == 0 or len(self.sub_location.get_text()) == 0 or len(self.category.get_text()) == 0 or len(self.equipment.get_text()) == 0:
            dialog_error = Error(self)
            response = dialog_error.run()

            dialog_error.destroy()
            return

        else:
            result = newAuth.equipment_form(self.department, self.location, self.trade, self.equipment_code, self.equipment_sl_no, self.section, self.sub_location, self.category, self.equipment, self.state)
            if result:
                self.destroy()
                dialog_equip_form_saved = Equip_form_saved(self)
                response = dialog_equip_form_saved.run()

                dialog_equip_form_saved.destroy()
                return
            else:
                print("Error")


class Equip_form_saved(Gtk.Dialog):

    def __init__(self, parent):

        Gtk.Dialog.__init__(self, "Equipment form saved.", parent, Gtk.DialogFlags.MODAL, (Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.set_default_size(130, 80)
        self.set_border_width(20)
        self.set_position(Gtk.WindowPosition.CENTER)
        area = self.get_content_area()
        area.add(Gtk.Label("Equipment details form saved successfully."))
        self.show_all()



class User_profile(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self, title = "Your Profile")
        self.set_border_width(25)
        self.set_default_size(400, 50)

        self.hbox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)

        self.equipment_form = Gtk.Button("Equipment Details")
        self.schedule_service = Gtk.Button("Schedule Service")
        self.assign_job = Gtk.Button("Assign Job")
        self.hbox.pack_start(self.equipment_form, True, True, 10)
        self.hbox.pack_start(self.schedule_service, True, True, 10)
        self.hbox.pack_start(self.assign_job, True, True, 10)

        self.equipment_form.connect("clicked", self.call_equipment_form)
        self.schedule_service.connect("clicked", self.call_schedule_service)
        self.assign_job.connect("clicked", self.call_assign_job)

        self.add(self.hbox)


    def call_equipment_form(self, widget):
        new_window = Equipment_form()
        new_window.set_position(Gtk.WindowPosition.CENTER)
        new_window.connect("delete-event", Gtk.main_quit)
        new_window.show_all()
        Gtk.main()

    def call_schedule_service(self, widget):
        new_window = Schedule_service()
        new_window.set_position(Gtk.WindowPosition.CENTER)
        new_window.connect("delete-event", Gtk.main_quit)
        new_window.show_all()
        Gtk.main()

    def call_assign_job(self, widget):
        new_window = Assign_Job()
        new_window.set_position(Gtk.WindowPosition.CENTER)
        new_window.connect("delete-event", Gtk.main_quit)
        new_window.show_all()
        Gtk.main()



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

        self.section_label = Gtk.Label("Section")
        self.section = Gtk.Entry()
        self.vbox_left.pack_start(self.section_label, True, True, 3)
        self.vbox_left.pack_start(self.section, True, True, 3)
        self.sub_loc_label = Gtk.Label("Sub Location")
        self.sub_loc = Gtk.Entry()
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
        self.freque_label  = Gtk.Label("PM Frequency(in month)")
        self.freque = Gtk.Entry()
        self.vbox_left.pack_start(self.freque_label, True, True, 3)
        self.vbox_left.pack_start(self.freque, True, True, 3)
        self.reminder_label = Gtk.Label("Reminder before PM date(in days)")
        self.reminder = Gtk.Entry()
        self.vbox_left.pack_start(self.reminder_label, True, True, 3)
        self.vbox_left.pack_start(self.reminder, True, True, 3)


        self.loc_label = Gtk.Label("Location")
        self.loc = Gtk.Entry()
        self.vbox_right.pack_start(self.loc_label, True, True, 3)
        self.vbox_right.pack_start(self.loc, True, True, 3)
        self.equip_label = Gtk.Label("Equipment")
        self.equip = Gtk.Entry()
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
        self.vbox_right.pack_start(self.date_label, True, True, 3)
        self.vbox_right.pack_start(self.date, True, True, 3)
        self.next_date_label = Gtk.Label("Next PM Date")
        self.vbox_right.pack_start(self.next_date_label, True, True, 3)
        self.next_date = Gtk.Entry()
        self.vbox_right.pack_start(self.next_date, True, True, 3)

        self.save_button = Gtk.Button("Save")
        self.cancel_button = Gtk.Button("Cancel")
        self.vbox_right.pack_start(self.save_button, True, True, 3)
        self.vbox_right.pack_start(self.cancel_button, True, True, 3)


        self.add(self.hbox)


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

        self.section_label = Gtk.Label("Section")
        self.section = Gtk.Entry()
        self.vbox_left.pack_start(self.section_label, True, True, 3)
        self.vbox_left.pack_start(self.section, True, True, 3)
        self.sub_loc_label = Gtk.Label("Sub Location")
        self.sub_loc = Gtk.Entry()
        self.vbox_left.pack_start(self.sub_loc_label, True, True, 3)
        self.vbox_left.pack_start(self.sub_loc, True, True, 3)
        self.task_label = Gtk.Label("Task")
        self.task = Gtk.Entry()
        self.vbox_left.pack_start(self.task_label, True, True, 3)
        self.vbox_left.pack_start(self.task, True, True, 3)
        self.inform_to_label = Gtk.Label("Inform to (If any)")
        self.inform_to = Gtk.Entry()
        self.vbox_left.pack_start(self.inform_to_label, True, True, 3)
        self.vbox_left.pack_start(self.inform_to, True, True, 3)
        self.prev_main_label = Gtk.Label("Preventive Maintenance")
        self.prev_main = Gtk.Entry()
        self.vbox_left.pack_start(self.prev_main_label, True, True, 3)
        self.vbox_left.pack_start(self.prev_main, True, True, 3)
        self.freque_label = Gtk.Label("PM Frequency(in month)")
        self.freque = Gtk.Entry()
        self.vbox_left.pack_start(self.freque_label, True, True, 3)
        self.vbox_left.pack_start(self.freque, True, True, 3)
        self.reminder_label = Gtk.Label("Reminder before PM date(in days)")
        self.reminder = Gtk.Entry()
        self.vbox_left.pack_start(self.reminder_label, True, True, 3)
        self.vbox_left.pack_start(self.reminder, True, True, 3)

        self.loc_label = Gtk.Label("Location")
        self.loc = Gtk.Entry()
        self.vbox_right.pack_start(self.loc_label, True, True, 3)
        self.vbox_right.pack_start(self.loc, True, True, 3)
        self.equip_label = Gtk.Label("Equipment")
        self.equip = Gtk.Entry()
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
        self.vbox_right.pack_start(self.date_label, True, True, 3)
        self.vbox_right.pack_start(self.date, True, True, 3)
        self.next_date_label = Gtk.Label("Next PM Date")
        self.vbox_right.pack_start(self.next_date_label, True, True, 3)
        self.next_date = Gtk.Entry()
        self.vbox_right.pack_start(self.next_date, True, True, 3)
        self.assign_label = Gtk.Label("Assign Job to")
        self.vbox_right.pack_start(self.assign_label, True, True, 3)
        self.assign = Gtk.Entry()
        self.vbox_right.pack_start(self.assign, True, True, 3)



        self.save_button = Gtk.Button("Save")
        self.cancel_button = Gtk.Button("Cancel")
        self.vbox_left.pack_start(self.save_button, True, True, 3)
        self.vbox_right.pack_start(self.cancel_button, True, True, 3)

        self.add(self.hbox)






window = Main_Window()
window.set_position(Gtk.WindowPosition.CENTER)
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
