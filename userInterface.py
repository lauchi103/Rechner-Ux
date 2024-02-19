import tkinter as tk
import os
import customtkinter as ctk
from PIL import Image

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Matrix-Rechner")
        self.geometry("720x480")

        #set grid layout 4x6
        self.grid_rowconfigure(3,weight=1)
        self.grid_columnconfigure(5,weight=1)

        #load images
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.cube_image = ctk.CTkImage