import tkinter as tk
from tkinter import *
import os
import customtkinter as ctk
from PIL import Image

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Matrix-Rechner")
        self.geometry("720x480")
        ctk.set_appearance_mode("dark")

        self.frame_list = []

        #set grid layout 1x2
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)

        #load images
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.image_cube = ctk.CTkImage(dark_image=Image.open(os.path.join(image_path,"cube.png")),size=(30,30))
        self.image_systemth = ctk.CTkImage(dark_image=Image.open(os.path.join(image_path,"systemtheorie.jpg")),size=(30,30))

        #sidebar frame
        self.navigation_frame = ctk.CTkFrame(master=self,corner_radius=0)
        self.navigation_frame.grid(row=0,column=0,sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4,weight=1)
        self.navigation_frame_width = self.navigation_frame.cget("width")
        
        self.navigation_frame_label = ctk.CTkLabel(master=self.navigation_frame,text="Sidebar",height=40,corner_radius=0)
        self.navigation_frame_label.grid(row=0,column=0,padx=20,pady=20)

        self.matrix_multipl_button = ctk.CTkButton(master=self.navigation_frame,corner_radius=0,height=40,border_spacing=10,
                                           fg_color="transparent",hover_color=("gray70","gray30"),text="Matrix",
                                           text_color=("gray30","gray90"),image=self.image_cube,anchor="w",command=self.matrix_button_event)
        self.matrix_multipl_button.grid(row=1,column=0,sticky="ew")
        self.matrix_multipl_button.configure(width=self.navigation_frame_width)

        self.systemth_button = ctk.CTkButton(master=self.navigation_frame,corner_radius=0,height=40,border_spacing=10,
                                           fg_color="transparent",hover_color=("gray70","gray30"),text="Systemth.",
                                           text_color=("gray30","gray90"),image=self.image_systemth,anchor="w",command=self.systemth_button_event)
        self.systemth_button.grid(row=2,column=0,sticky="ew")
        self.systemth_button.configure(width=self.navigation_frame_width)

        #Matrix Frame
        self.matrix_frame = Matrix_Frame(master = self)
        self.matrix_frame.grid(row=0,column=1,sticky="nsew")


        self.select_frame_by_name("matrix")#bearbeiten


    def select_frame_by_name(self,name):
        pass

    def matrix_button_event(self):
        self.select_frame_by_name("matrix")

    def systemth_button_event(self):
        self.select_frame_by_name("systemth")

class Matrix_Frame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)    
        self.configure( fg_color = "transparent" )
        self.master = master

        self.dim_m1 = ()
        self.dim_m2 = ()

        self.matrix_dimension_Frame = Matrix_dimension_Frame(self)
        self.matrix_dimension_Frame.grid(row=0,column=0, sticky = "nsew")
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)

    
    def select_input_frame(self,dim_m1 = 0, dim_m2 = 0):
        self.matrix_input_Frame = Matrix_input_Frame(self, dim_m1, dim_m2)
        self.matrix_dimension_Frame.grid_forget()
        self.matrix_input_Frame.grid(row=0, column=0, sticky="nsew")

class Matrix_dimension_Frame(ctk.CTkFrame):
    def __init__(self ,master:Matrix_Frame):
        super().__init__(master)
        self.master = master
        
        self.configure( fg_color = "transparent")

        self.matrix1_rows = ctk.CTkEntry(master=self,height=30,placeholder_text="Rows M1")
        self.matrix1_columns = ctk.CTkEntry(master=self,height=30,placeholder_text="Columns M1")
        self.matrix2_rows = ctk.CTkEntry(master=self,height=30,placeholder_text="Rows M2")
        self.matrix2_columns = ctk.CTkEntry(master=self,height=30,placeholder_text="Columns M2")
        self.grid_rowconfigure(1,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.matrix1_rows.grid(row=0,column=0 , padx = 20 , pady = 20, sticky = "wn")
        self.matrix1_columns.grid(row=0,column=1 , padx = 20 , pady = 20, sticky = "wn")
        self.matrix2_rows.grid(row=1,column=0 , padx = 20 , pady = 20, sticky = "wn")
        self.matrix2_columns.grid(row=1,column=1 , padx = 20 , pady = 20, sticky = "wn")

        self.select_button = ctk.CTkButton(master = self, height = 30, fg_color = "transparent", text= "Select Dim",hover_color=("gray70","gray30"), command=self.select_input_Frame)
        self.select_button.grid(row=2, column=0, columnspan=2, sticky="nsew")
    def select_input_Frame(self):
        try:
            dim_m1 = (int(self.matrix1_rows.get()),int( self.matrix1_columns.get()))
            dim_m2 = (int(self.matrix2_rows.get()), int(self.matrix2_columns.get()))

            if dim_m1[1] == dim_m2[0]:
                self.master.select_input_frame(dim_m1, dim_m2)
            else:
                self.pop_message = ctk.CTkToplevel(self.master)
                self.pop_message.title("Popup")
                self.pop_message.geometry("300x300")
                pop_Label = ctk.CTkLabel(self.pop_message ,text="You choose wrong dimensions for matrices!")
                pop_Label.grid(row=0 ,column=0)
                self.matrix1_columns.delete(0 ,END)
                self.matrix1_rows.delete(0 ,END)
                self.matrix2_columns.delete(0 ,END)
                self.matrix2_rows.delete(0 ,END)
                self.pop_message.focus_set()
        except ValueError:
            raise Exception("Only numbers are valid input")




        

    
class Matrix_input_Frame(ctk.CTkFrame):
    def __init__(self,master, dim_m1, dim_m2):
        super().__init__(master)
        self.configure( fg_color = "transparent")
        self.master = master
        self.dim_m1 = dim_m1
        self.dim_m2 = dim_m2
        self.grid_rowconfigure(0,weight=5)
        self.grid_columnconfigure(0,weight=4)
        self.grid_columnconfigure(2,weight=4)
        self.grid_columnconfigure(1,weight=1)
        self.grid_rowconfigure(1,weight=1)

        self.m1_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.m1_frame.grid_rowconfigure(0,weight=1)
        self.m1_frame.grid_columnconfigure(0,weight=1)
        self.m1_frame.grid(row=0, column=0, sticky="nsew")
        self.m2_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.m2_frame.grid_rowconfigure(0,weight=1)
        self.m2_frame.grid_columnconfigure(0,weight=1)
        self.m2_frame.grid(row=0, column=2, sticky="nsew")

        self.m1_entry = self.create_matrix_input(self.m1_frame ,dim_m1)
        self.label = ctk.CTkLabel(self,text="x", font=("Arial CE",20), fg_color="transparent")
        self.label.grid(row=0, column=1, sticky="nsew")
        self.m2_entry = self.create_matrix_input(self.m2_frame, dim_m2)

        self.m1_frame.configure(width = self.master.cget("width")//9 * 4)
        self.m2_frame.configure(width = self.master.cget("width")//9 * 4)
        
        self.calculate_button = ctk.CTkButton(self, width=80, height=40, fg_color="grey30", hover_color="grey70", command=self.calculate_mult)
        self.calculate_button.grid(row=1, column=0, columnspan=3)

    def calculate_mult(self, matrix1, matrix2):
        result = []

        # Check if dimensions are compatible for matrix multiplication
        if len(matrix1[0]) != len(matrix2):
            raise Exception^("Wrong dimension of the matrices, not multipliable!")

        # Perform matrix multiplication
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix2[0])):
                element = 0
                for k in range(len(matrix2)):
                    if isinstance(matrix1[i][k], str) or isinstance(matrix2[k][j], str):
                        # If an element is a variable, leave it as it is
                        element += str(matrix1[i][k]) + "*" + str(matrix2[k][j]) + " "
                    else:
                        element += matrix1[i][k] * matrix2[k][j]
                row.append(element)
            result.append(row)

        return result

    def create_matrix_input(self ,frame:ctk.CTkFrame ,dim_input):
        try:
            rows = int(dim_input[0])
            columns = int(dim_input[1])
        except ValueError:
            raise Exception("Not a number, not a valid input")
        matrix_input = []
        for i in range(rows):
            row_entries = []
            #frame.grid_rowconfigure(i, weight=1)
            for j in range(columns):
                entry = ctk.CTkEntry(frame, width=50)
                entry.grid(row=i,column=j)
                #frame.grid_columnconfigure(j, weight=1)
                row_entries.append(entry)
            matrix_input.append(row_entries)
        for i in range(rows):
            frame.grid_rowconfigure(i, weight=1)
        for i in range(columns):
            frame.grid_columnconfigure(i, weight=1)
        return matrix_input
    
def main():
    app = App()

    
    app.mainloop()

if __name__ == "__main__":
    main()
    