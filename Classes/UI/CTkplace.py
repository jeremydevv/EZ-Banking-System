import customtkinter as ctk

def place(element,x,y,anchorPlacement):
    element.place(x,y,anchor=anchorPlacement)
    return element