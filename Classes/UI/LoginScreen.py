import customtkinter as ctk
import re
import Classes.UI.Padding as pd
import Classes.UI.CTkplace as ctPlace

class init():

    def __init__(self,app):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue") 

        app = ctk.CTk()
        app.geometry("400x240")
        app.title("Login Screen")

        MainFrame = ctk.CTkFrame(master=app)
        ctPlace.place(0.5,0.5,ctk.CENTER)

        self.EZBankingTitle = ctk.CTkLabel(MainFrame, text="EZ Banking", fg_color="transparent")
        ctPlace.place(0.5,0.05,ctk.CENTER)
        pd.pad(self.SlimeBanking, {ctk.TOP: 5, ctk.BOTTOM: 0, ctk.LEFT: 5, ctk.RIGHT: 5})

        self.usernameInput = ctk.CTkEntry(MainFrame, placeholder_text="Username")
        ctPlace.place(0.5,0.3,ctk.CENTER)
        pd.pad(self.usernameInput, {ctk.TOP: 5, ctk.BOTTOM: 0, ctk.LEFT: 5, ctk.RIGHT: 5})

        self.passwordInput = ctk.CTkEntry(MainFrame, placeholder_text="Password", show="*")
        ctPlace.place(0.5,0.4,ctk.CENTER)
        pd.pad(self.passwordInput, {ctk.TOP: 5, ctk.BOTTOM: 0, ctk.LEFT: 5, ctk.RIGHT: 5})
        
        self.LoginButton = ctk.CTkButton(MainFrame, text="Log in", command=self.login_request)
        ctPlace.place(0.5,0.1,ctk.CENTER)
        pd.pad(self.LoginButton, {ctk.TOP: 20, ctk.BOTTOM: 10, ctk.LEFT: 5, ctk.RIGHT: 5})

        app.mainloop()

    def fetchLoginInformation(self):
        
        username = self.usernameInput.get()
        password = self.passwordInput.get()
        
        return (username,password)

    def login_request(self):
        print("Log in request")
        username , password = self.fetchLoginInformation()

        print("Attempted information" + " " + username + " & " + password)
