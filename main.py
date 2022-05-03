import tkinter as tk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from interpreter.lexer import Lexer
from interpreter.parser_ import Parser
from interpreter.interpreter import Interpreter


class GUIApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x600")
        self.root.minsize(400, 600)
        self.root.maxsize(400, 600)
        self.root.title("Function Plotter")
        self.function_entry = None
        self.min_entry = None
        self.max_entry = None
        self.graph_canvas = None

    def handle_button_click(self):
        try:
            function_string = self.function_entry.get()
            min_val = float(self.min_entry.get()) if self.min_entry.get() else 0.0
            max_val = float(self.max_entry.get()) if self.max_entry.get() else 0.0
            self.plot_function(function_string, min_val, max_val)
        except Exception as e:
            print(e)

    def plot_function(self, function_string: str, min_val: float, max_val: float):
        if function_string:
            try:
                lexer = Lexer(function_string)
                tokens = lexer.generate_tokens()
                p = Parser(tokens)
                tree = p.parse()
                independent_values = list(range(int(min_val), int(max_val + 1), ))
                dependent_values = [Interpreter(x).visit(tree).value for x in independent_values]
                if self.graph_canvas is not None:
                    self.graph_canvas.get_tk_widget().pack_forget()
                fig = Figure(figsize=(5, 4), dpi=100)
                a = fig.add_subplot()
                a.plot(independent_values, dependent_values)
                a.set_xlabel("x")
                a.set_ylabel("f(x)")

                self.graph_canvas = FigureCanvasTkAgg(fig, master=self.root)
                self.graph_canvas.draw()
                self.graph_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            except Exception as e:
                print(e)

    def run(self):
        label = tk.Label(master=self.root, text="Plot a function \nby filling the fields below", font=("Arial", 18))
        label.pack(pady=(15, 0))

        top_frame = tk.Frame(self.root)
        top_frame.pack(pady=15, expand=True)

        function_label = tk.Label(master=top_frame, text="Enter the function: f(x) =")
        function_label.grid(row=0, column=0)
        self.function_entry = tk.Entry(master=top_frame)
        self.function_entry.grid(row=0, column=1)

        min_label = tk.Label(master=top_frame, text="Minimum value of x = ")
        min_label.grid(row=1, column=0)
        self.min_entry = tk.Entry(master=top_frame)
        self.min_entry.grid(row=1, column=1)

        max_label = tk.Label(master=top_frame, text="Maximum value of x = ")
        max_label.grid(row=2, column=0)
        self.max_entry = tk.Entry(master=top_frame)
        self.max_entry.grid(row=2, column=1)

        initial_function = "x^2 + 4"
        initial_min = 400
        initial_max = 3000

        self.function_entry.insert(0, initial_function)
        self.min_entry.insert(0, str(initial_min))
        self.max_entry.insert(0, str(initial_max))

        tk.Button(self.root, text="Plot the function", borderwidth=1, padx=5, pady=5,
                  command=lambda: self.handle_button_click()).pack()
        self.plot_function(initial_function, initial_min, initial_max)
        tk.mainloop()


if __name__ == '__main__':
    app = GUIApp()
    app.run()
