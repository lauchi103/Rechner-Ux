import tkinter as tk
from userInterface import MatrixCalculator


def main():
    root = tk.Tk()
    app = MatrixCalculator(root)

    calculate_button = tk.Button(root, text="Calculate", command=app.calculate_matrices)
    calculate_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10)
    root.mainloop()

if __name__ == "__main__":
    main()