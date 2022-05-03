import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from interpreter.arithmetic_interpreter import ArithmeticInterpreter


class GUIApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x600")
        self.root.minsize(400, 600)
        self.root.maxsize(400, 600)
        self.root.title("Function Plotter")
        self.independent_values, self.dependent_values = [], []

        # Headline
        label = tk.Label(master=self.root, text="Plot a function \nby filling the fields below", font=("Arial", 18))
        label.pack(pady=(15, 0))

        # Inputs field
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

        # Plotting button
        tk.Button(self.root, text="Plot the function", borderwidth=1, padx=5, pady=5,
                  command=lambda: self.handle_button_click()).pack()

        # Error label
        self.error_message_label = tk.Label(master=self.root, text="", fg="#FF0000", highlightcolor="#FF0000")
        self.error_message_label.pack()

        # Function Plot
        initial_function = "x^2 + 4"
        initial_min = 400
        initial_max = 3000

        self.function_entry.insert(0, initial_function)
        self.min_entry.insert(0, str(initial_min))
        self.max_entry.insert(0, str(initial_max))

        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.plot(self.independent_values, self.dependent_values)
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("f(x)")

        graph_canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        graph_canvas.draw()
        graph_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.plot_function(initial_function, initial_min, initial_max)

        tk.mainloop()

    def handle_error(self, message: str = ""):
        self.error_message_label.config(text=message)

    @staticmethod
    def evaluate_function_string(function_string: str, min_val: float, max_val: float) -> (list, list):
        independent_values = list(range(int(min_val), int(max_val + 1)))
        dependent_values = [ArithmeticInterpreter.evaluate(function_string, x) for x in independent_values]
        return independent_values, dependent_values

    def handle_button_click(self):
        self.handle_error()
        try:
            function_string = self.function_entry.get()
            if function_string.strip() == "":
                raise Exception("Please enter a function expression e.g: 'x^2 + 4'")
            if not self.min_entry.get().isnumeric() or not self.max_entry.get().isnumeric():
                raise Exception("Please enter a valid numeric range for minimum and maximum")
            min_val = float(self.min_entry.get()) if self.min_entry.get() else 0.0
            max_val = float(self.max_entry.get()) if self.max_entry.get() else 0.0
            if min_val > max_val:
                raise Exception("The minimum value should be less that the maximum")
            self.plot_function(function_string, min_val, max_val)
        except Exception as e:
            self.handle_error(str(e))

    def plot_function(self, function_string: str, min_val: float, max_val: float):
        self.ax.clear()
        self.independent_values, self.dependent_values = \
            self.evaluate_function_string(function_string, min_val, max_val)
        self.ax.plot(self.independent_values, self.dependent_values)
        self.fig.canvas.draw()
