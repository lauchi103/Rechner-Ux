import tkinter as tk
import customtkinter as ctk

#System Settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#app frame
app = ctk.CTk()
app.geometry("720x480")
app.title("Calculator")

frame = ctk.CTkFrame(app,width=app.winfo_width(),height=app.winfo_height(),bg_color="white")
frame.pack(padx=10,pady=50)
print(app.winfo_height())

#adding UI elements
title = ctk.CTkLabel(app, text="Matrix Calculator")
title.pack(padx=10,pady=10)

#dimension input
rows_var = tk.StringVar()
input_box = ctk.CTkEntry(app,width=40,height=10,textvariable=rows_var)
input_box.pack()

#executable function
def doSomething():
    print(input_box.get())

#function
button = ctk.CTkButton(app, text="Confirm", command = doSomething)
button.pack()
#Run app 
app.mainloop()