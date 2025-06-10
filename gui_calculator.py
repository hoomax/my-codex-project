import tkinter as tk
from tkinter import ttk, messagebox
from calculator import Calculator


class CalculatorGUI(tk.Tk):
    """Simple GUI for the Calculator using Tkinter."""

    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.calc = Calculator()
        self._create_widgets()

    def _create_widgets(self):
        # operands
        self.entry_a = ttk.Entry(self)
        self.entry_a.grid(row=0, column=0, padx=5, pady=5)

        self.operation = tk.StringVar(value="add")
        ops = [("Add", "add"), ("Subtract", "sub"), ("Multiply", "mul"), ("Divide", "div")]
        row = 1
        for text, mode in ops:
            ttk.Radiobutton(self, text=text, variable=self.operation, value=mode).grid(row=row, column=0, sticky="w")
            row += 1

        self.entry_b = ttk.Entry(self)
        self.entry_b.grid(row=0, column=1, padx=5, pady=5)

        ttk.Button(self, text="Compute", command=self.compute).grid(row=5, column=0, columnspan=2, pady=5)

        self.result_var = tk.StringVar()
        ttk.Label(self, textvariable=self.result_var).grid(row=6, column=0, columnspan=2)

    def compute(self):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            op = self.operation.get()
            ops = {
                "add": self.calc.add,
                "sub": self.calc.subtract,
                "mul": self.calc.multiply,
                "div": self.calc.divide,
            }
            result = ops[op](a, b)
            self.result_var.set(str(result))
        except ValueError as exc:
            messagebox.showerror("Error", str(exc))


def main():
    app = CalculatorGUI()
    app.mainloop()


if __name__ == "__main__":
    main()
