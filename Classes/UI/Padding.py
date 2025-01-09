import customtkinter as ctk

def pad(element,sides):
    for side , amount in sides:
        element.pack(side=side,padx=amount,pady=amount)
    return element