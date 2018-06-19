from mongoengine import *

class User(Document):
    email = EmailField(required=True, unique=True)
    name = StringField(required=True)
    phone = StringField(required=True, max_length=10, unique=True)
    password = StringField(required=True)

    def __init__(self, name, email, phone, password, *args, **values):
        super(User, self).__init__(*args, **values)
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password

    def __str__(self):
        return self.name + "--" + self.email + "--" + self.phone


class Authentication:

    def __init__(self, host, port, dbname, username, password):

        if username is None:
            connect(db=dbname, host=host, port=port)
        else:
            connect(db=dbname, host=host, port=port, username=username, password=password)

    def reg(self, name, email, phone, password):
        user = User(name, email, phone, password)
        try :
            user.save()
            return True
        except NotUniqueError:
            return False


    def login(self, phone, password):

        user = User.objects.get(phone=phone)

        if user is None:
            return False
        elif user.password != password:
            return False
        else:
            return True
