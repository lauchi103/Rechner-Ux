import tkinter as tk
from tkinter import messagebox

class MatrixCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Matrix Calculator")

        self.matrices = []  # Liste für Matrizen
        self.matrix_frames = []  # Liste für Frame-Widgets der Matrizen

        self.operation_var = tk.StringVar()
        self.operation_var.set("Matrix Multiplication")

        self.dimension_label = tk.Label(master, text="Matrix Dimensions:")
        self.dimension_label.grid(row=0, column=0, padx=10, pady=10)

        self.rows_label = tk.Label(master, text="Rows:")
        self.rows_label.grid(row=1, column=0, padx=10, pady=5)
        self.rows_entry = tk.Entry(master)
        self.rows_entry.grid(row=1, column=1, padx=10, pady=5)

        self.cols_label = tk.Label(master, text="Columns:")
        self.cols_label.grid(row=2, column=0, padx=10, pady=5)
        self.cols_entry = tk.Entry(master)
        self.cols_entry.grid(row=2, column=1, padx=10, pady=5)

        self.operation_label = tk.Label(master, text="Matrix Operation:")
        self.operation_label.grid(row=3, column=0, padx=10, pady=5)

        self.operation_menu = tk.OptionMenu(master, self.operation_var, "Matrix Multiplication", "Matrix Addition")
        self.operation_menu.grid(row=3, column=1, padx=10, pady=5)

        self.confirm_button = tk.Button(master, text="Confirm", command=self.create_matrix_input)
        self.confirm_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def create_matrix_input(self):
        try:
            rows = int(self.rows_entry.get())
            cols = int(self.cols_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid dimensions.")
            return

        matrix_frame = tk.Frame(self.master)
        matrix_frame.grid(row=len(self.matrices) + 5, column=0, columnspan=2, padx=10, pady=10)

        matrix = []
        for i in range(rows):
            row_entries = []
            for j in range(cols):
                entry = tk.Entry(matrix_frame, width=5)
                entry.grid(row=i, column=j, padx=5, pady=5)
                row_entries.append(entry)
            matrix.append(row_entries)

        self.matrices.append(matrix)
        self.matrix_frames.append(matrix_frame)

    def calculate_matrices(self):
        operation = self.operation_var.get()
        if operation == "Matrix Multiplication":
            self.matrix_multiplication()
        elif operation == "Matrix Addition":
            self.matrix_addition()

    def matrix_multiplication(self):
        # Implementiere hier die Matrixmultiplikation
        print("multiplication")

    def matrix_addition(self):
        # Implementiere hier die Matrixaddition
        print("addition")

# def main():
#     root = tk.Tk()
#     app = MatrixCalculator(root)

#     calculate_button = tk.Button(root, text="Calculate", command=app.calculate_matrices)
#     calculate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

#     root.mainloop()

# if __name__ == "__main__":
#     main()
