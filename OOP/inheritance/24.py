class Loggable:
    def Log(self):
         print("Logging")


class Database:
    def Connect (self):
        print("Connecting")

class LogData(Loggable,Database):
    def Process(self):

        self.Log()
        self.Connect()

