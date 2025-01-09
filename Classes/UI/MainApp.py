import customtkinter as ctk
import Classes.UI.LoginScreen as loginClass

class init:
    def __init__(self):
        self.Main = ctk.CTk
        loginClass.init(self.Main)
