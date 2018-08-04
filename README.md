# Assets-Management-System
A Linux Software which helps to keep track of all the assets belonging to a company. The software will keep you updated about the condition of the asset and will frequently remind you about its servicing.

REQUIREMENTS : 
1. Python v3.0+
2. MongoEngine

PYTHON PACKAGES REQUIRED :
1. gi, GTK v3.0
2. datetime
3. smtplib
4. email
5. os
6. MongoEngine

PROCESS :
1. Run GUI_advanced.py
2. Create a new Profile.
3. LOGIN using the user id and password provided.
4. The following menus are currently in working state :
      1. EQUIPMENTS.
      2. SCHEDULE SERVICE.
      3. ASSIGN JOB.
5. Enter the data in the form accordingly.
6. Run Reminder sender, and it will be added as a System Startup operation.
7. The Software will look for reminders to be sent each time the system starts and send a mail to the responsible person accordingly.

