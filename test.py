import auth

# if database requires authentication use username and password instead of None, None

newAuth = auth.Authentication('localhost', 27017, 'test-db', None, None)

if __name__ == '__main__':
    if newAuth.reg("Himanshu", "himanshu10nain@gmail.com", "7042856750", "password"):
        print("User Created")
    else:
        print("User Creation Error")

    if newAuth.login("7042856750", "password"):
        print("Login Successful")
    else:
        print("Login Failed")





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
        self.cancel.connect("clicked", self.cancel_form)

        self.add(self.hbox)

        return

    def save_equip_form(self, widget):
        if len(self.department.get_text()) == 0 or \
                len(self.trade.get_text()) == 0 or \
                len(self.equipment_code.get_text()) == 0 or \
                len(self.equipment_sl_no.get_text()) == 0 or \
                len(self.parent_equipment.get_text()) == 0 or \
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



