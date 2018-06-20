from mongoengine import *

class User(Document):
    name = StringField(required=True)
    Personal_number = StringField(required=True, max_length=6, unique=True)
    password = StringField(required=True)

    def __init__(self, name, Personal_number, password, *args, **values):
        super(User, self).__init__(*args, **values)
        self.name = name
        self.Personal_number = Personal_number
        self.password = password



class Equipment(Document):
    department = StringField(required=True)
    location = StringField(required=True)
    trade = StringField(required=True)
    equip_code = StringField(required=True)
    equip_sl_no = StringField(required=True)
    section = StringField(required=True)
    sub_loc = StringField(required=True)
    category = StringField(required=True)
    equipment_name = StringField(required=True)
    state = BooleanField(required=True)

    def __init__(self, department, location, trade, equip_code, equip_sl_no, section, sub_loc, category, equipment_name, state, *args, **values):
        super(Equipment, self).__init__(*args, **values)
        self.department = department
        self.location = location
        self.trade = trade
        self.equip_code = equip_code
        self.equip_sl_no = equip_sl_no
        self.section = section
        self.sub_loc = sub_loc
        self.category = category
        self.equipment_name = equipment_name
        self.state = state

class Schedule(Document):
    section = StringField(required=True)
    sub_loc = StringField(required=True)
    task = StringField(required=True)
    inform_to = StringField(required=True)
    prev_main = StringField(required=True)
    freq = StringField(required=True)
    reminder = StringField(required=True)
    loc = StringField(required=True)
    equip_name = StringField(required=True)
    owner = StringField(required=True)
    code = StringField(required=True)
    date = StringField(required=True)
    next_date = StringField(required=True)

    def __init__(self, section, sub_loc, task, inform_to, prev_main, freq, reminder, loc, equip_name, owner, code, date, next_date, *args, **values):
        super(Schedule, self).__init__(*args, **values)
        self.section = section
        self.sub_loc = sub_loc
        self.task = task
        self.inform_to = inform_to
        self.prev_main = prev_main
        self.freq = freq
        self.reminder = reminder
        self.loc = loc
        self.equip_name = equip_name
        self.owner = owner
        self.code = code
        self.date = date
        self.next_date = next_date

class Authentication:

    def __init__(self, host, port, dbname, username, password):

        if username is None:
            connect(db=dbname, host=host, port=port)
        else:
            connect(db=dbname, host=host, port=port, username=username, password=password)

    def reg(self, name, Personal_number, password):
        user = User(name, Personal_number, password)
        try:
            user.save()
            return True

        except Exception as e:
            return False


    def login(self, Personal_number, password):

        try:
            user = User.objects.get(Personal_number=Personal_number)
            if user.password != password:
                return False
            else:
                return True

        except Exception as e:
            return False



    def equipment_form(self, department, location, trade, equip_code, equip_sl_no, section, sub_loc, category, equipment_name, state):

        equipment = Equipment(department, location, trade, equip_code, equip_sl_no, section, sub_loc, category, equipment_name, state)
        try:
            equipment.save()
            return True

        except Exception as e:
            return False

    def schedule_form(self, section, sub_loc, task, inform_to, prev_main, freq, reminder, loc, equip_name, owner, code, date, next_date):
        schedule = Schedule(section, sub_loc, task, inform_to, prev_main, freq, reminder, loc, equip_name, owner, code, date, next_date)
        try:
            schedule.save()
            return True

        except Exception as e:
            return False