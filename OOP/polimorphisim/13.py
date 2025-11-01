#Create a Notification base class with subclasses EmailNotification and SMSNotification—each overrides send().

class Notification:
    def send(self):
        print("bla bla")


class EmailNotification(Notification):
    def send(self):
        print("Sending a generic notification.. ")

class SMSNotificaion(Notification):
    def send(self):
        print("Sending an email notification to the user")

Notifications=[EmailNotification(),SMSNotificaion()]
for n in Notifications:
    n.send()