import os
import time as time
from datetime import date

# MODULES
import Classes.Event as EventClass
import Classes.Transaction as TransactionClass
import Classes.Account as AccountClass

# UI MODULES
import Classes.UI.MainApp as MainApp

def initmain():
    print("Init Started")
    NewLoginScreen = MainApp.init()

initmain()
