import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("900x900")
        self.root.configure(bg='silver')  ### Change the background color

        self.entry = tk.Entry(root, width=30, borderwidth=5, font=("Timesroman", 24))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.history = []  # List to store calculation history
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/', 'sqrt',
            '4', '5', '6', '*', 'x^2',
            '1', '2', '3', '-', 'x^3',
            '0', '.', '=', '+', 'exp',
            '(', ')', 'sin', 'cos', 'tan',
            'ln', 'log10', 'C', 'History'
        ]

        row = 1
        col = 0
        for button in buttons:
            action = lambda x=button: self.click_event(x)
            tk.Button(self.root, text=button, width=10, height=3, command=action, bg='lightgrey').grid(row=row, column=col)
            col += 1
            if col > 4:
                col = 0
                row += 1

    def click_event(self, key):
        if key == "=":
            try:
                result = str(eval(self.entry.get()))
                self.add_to_history(self.entry.get() + " = " + result)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif key == "C":
            self.entry.delete(0, tk.END)
        elif key == "History":
            self.show_history()
        else:
            try:
                if key == "sqrt":
                    result = math.sqrt(float(self.entry.get()))
                elif key == "x^2":
                    result = float(self.entry.get()) ** 2
                elif key == "x^3":
                    result = float(self.entry.get()) ** 3
                elif key == "exp":
                    result = math.exp(float(self.entry.get()))
                elif key == "sin":
                    result = math.sin(math.radians(float(self.entry.get())))
                elif key == "cos":
                    result = math.cos(math.radians(float(self.entry.get())))
                elif key == "tan":
                    result = math.tan(math.radians(float(self.entry.get())))
                elif key == "ln":
                    result = math.log(float(self.entry.get()))
                elif key == "log10":
                    result = math.log10(float(self.entry.get()))
                else:
                    self.entry.insert(tk.END, key)
                    return

                self.add_to_history(self.entry.get() + " = " + str(result))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")

    def add_to_history(self, entry):
        if len(self.history) >= 5:
            self.history.pop(0)
        self.history.append(entry)

    def show_history(self):
        history_window = tk.Toplevel(self.root)
        history_window.title("History")
        history_window.geometry("300x200")
        history_window.configure(bg='lightblue')

        history_text = tk.Text(history_window, font=("Arial", 14), bg='lightgrey')
        history_text.pack(expand=True, fill='both')

        for item in self.history:
            history_text.insert(tk.END, item + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()
