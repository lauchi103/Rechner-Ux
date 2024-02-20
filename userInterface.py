import tkinter as tk
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
        self.navigation_frame.rowconfigure(4,weight=1)
        self.navigation_frame_width = self.navigation_frame.cget("width")
        
        self.navigation_frame_label = ctk.CTkLabel(master=self.navigation_frame,text="Sidebar",height=40,corner_radius=0,anchor="w")
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

    
    def select_input_frame(self,dim_m1, dim_m2):
        self.matrix_input_Frame = Matrix_input_Frame(self, dim_m1, dim_m2)
        self.matrix_dimension_Frame.grid_forget()
        self.matrix_input_Frame.grid(row=0, column=0, sticky="nsew")

class Matrix_dimension_Frame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        
        self.configure( fg_color = "transparent")

        self.row1=""
        self.column1=""
        self.row2=""
        self.column2=""
        self.matrix1_rows = ctk.CTkEntry(master=self,textvariable=self.row1,height=30,placeholder_text="Rows M1")
        self.matrix1_columns = ctk.CTkEntry(master=self,textvariable=self.column1,height=30,placeholder_text="Columns M1")
        self.matrix2_rows = ctk.CTkEntry(master=self,textvariable=self.row2,height=30,placeholder_text="Rows M2")
        self.matrix2_columns = ctk.CTkEntry(master=self,textvariable=self.column2,height=30,placeholder_text="Columns M2")
        self.rowconfigure(1,weight=1)
        self.columnconfigure(1,weight=1)
        self.matrix1_rows.grid(row=0,column=0 , padx = 20 , pady = 20, sticky = "wn")
        self.matrix1_columns.grid(row=0,column=1 , padx = 20 , pady = 20, sticky = "wn")
        self.matrix2_rows.grid(row=1,column=0 , padx = 20 , pady = 20, sticky = "wn")
        self.matrix2_columns.grid(row=1,column=1 , padx = 20 , pady = 20, sticky = "wn")

        self.select_button = ctk.CTkButton(master = self, height = 30, fg_color = "transparent", text= "Select Dim",hover_color=("gray70","gray30"), command=self.select_input_Frame)
        self.select_button.grid(row=2, column=0, columnspan=2, sticky="nsew")
    def select_input_Frame(self):
        dim_m1 = (self.matrix1_rows.get(), self.matrix1_columns.get())
        dim_m2 = (self.matrix2_rows.get(), self.matrix2_columns.get())
        self.master.select_input_frame(dim_m1, dim_m2)

    
class Matrix_input_Frame(ctk.CTkFrame):
    def __init__(self,master, dim_m1, dim_m2):
        super().__init__(master)
        self.configure( fg_color = "transparent")
        self.master = master
        self.dim_m1 = dim_m1
        self.dim_m2 = dim_m2

        print(dim_m1)
        print(dim_m2)
        
    def create_matrix_input(self,rows_input, columns_input, frame):
        try:
            rows = int(rows_input)
            columns = int(columns_input)
        except ValueError:
            #show Error!
            return
        matrix_input = []
        for i in range(rows):
            row_entries = []
            for j in range(columns):
                entry = ctk.CTkEntry(frame, width=5)
                entry.grid(row=i,column=j)
                row_entries.append(entry)
            matrix_input.append(row_entries)
        return matrix_input
    
def main():
    app = App()

    
    app.mainloop()

if __name__ == "__main__":
    main()
    