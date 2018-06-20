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

    def __str__(self):
        return self.name + "--"  + "--" + self.Personal_number


class Authentication:

    def __init__(self, host, port, dbname, username, password):

        if username is None:
            connect(db=dbname, host=host, port=port)
        else:
            connect(db=dbname, host=host, port=port, username=username, password=password)

    def reg(self, name, Personal_number, password):
        user = User(name, Personal_number, password)
        try:
            result = user.save()
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

