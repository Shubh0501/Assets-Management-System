import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import auth
import datetime
import os

newAuth = auth.Authentication("localhost", 27017, 'user_database', None, None)

def send_reminder():

    assign = auth.Assign.objects.all_fields()
    for i in range(0, assign.__len__()):
        person = assign[i].assign
        equip = assign[i].equip_name
        owner = assign[i].owner
        code = assign[i].code
        date = assign[i].next_date
        task = assign[i].task
        loc = assign[i].loc
        sub_loc = assign[i].sub_loc
        section = assign[i].section
        inform_to = assign[i].inform_to

        if(str(datetime.datetime.now().date()) == date):
            sender = 'vegeta.pasari@gmail.com'
            email = auth.User.objects.get(name=person)
            email = email.mail
            receiver = email

            code = section
            message = MIMEMultipart()
            message['Subject'] = 'Job Assignment in '+ code
            message['From'] = sender
            message['To'] = receiver
            html = 'You have assigned the job for the maintenance of '+ equip + ' on '+ date + '.'+ ' The equipment is owned by '+ owner + ' and the location of equipment is '+ sub_loc+ ', '+loc+ '.'+' The equipment code is '+ code +' and the task is '+task+'. After the job you will inform to '+inform_to
            body = MIMEText(html, 'html')
            message.attach(body)

            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(sender, 'JonSnow5')
            server.sendmail(sender, receiver, message.as_string().encode('utf-8'))
            server.quit()


if __name__ == '__main__':
    send_reminder()
