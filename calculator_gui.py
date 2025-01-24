from tkinter import *
import math


class Calculator(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 16 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Advanced Calculator')

        self.is_dark_mode = False  # Default to light mode
        self.light_bg = "#ffffff"
        self.light_fg = "#000000"
        self.dark_bg = "#2c2c2c"
        self.dark_fg = "#f5f5f5"

        # StringVar to hold the display value
        self.display = StringVar()
        self.display.set("")  # Initialize display

        # Entry widget for display
        self.display_entry = Entry(self, relief=RIDGE, textvariable=self.display,
                                   justify='right', bd=20, bg=self.light_bg, fg=self.light_fg)
        self.display_entry.pack(side=TOP, expand=YES, fill=BOTH)

        # Add toggle mode button
        self.toggle_button = Button(self, text="Toggle Mode", command=self.toggle_mode)
        self.toggle_button.pack(side=TOP, expand=YES, fill=BOTH)

        # Add buttons for numbers and functions
        self.create_buttons()

    def create_buttons(self):
        # Button layout
        buttons = [
            ["C", "√", "^", "%"],
            ["sin", "cos", "tan", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "=", ""]
        ]

        for row in buttons:
            button_row = Frame(self, bg=self.light_bg)
            button_row.pack(side=TOP, expand=YES, fill=BOTH)
            for char in row:
                if char:  # Only create buttons for non-empty strings
                    btn = Button(button_row, text=char, command=lambda ch=char: self.on_button_click(ch))
                    btn.pack(side=LEFT, expand=YES, fill=BOTH)

    def toggle_mode(self):
        """Toggle between light and dark modes."""
        self.is_dark_mode = not self.is_dark_mode
        bg_color = self.dark_bg if self.is_dark_mode else self.light_bg
        fg_color = self.dark_fg if self.is_dark_mode else self.light_fg

        # Update all widgets with the new theme
        self.display_entry.config(bg=bg_color, fg=fg_color)
        self.toggle_button.config(bg=bg_color, fg=fg_color)
        for child in self.winfo_children():
            if isinstance(child, Frame):
                child.config(bg=bg_color)
                for btn in child.winfo_children():
                    btn.config(bg=bg_color, fg=fg_color)

    def on_button_click(self, char):
        """Handle button click events."""
        if char == "C":
            self.display.set("")
        elif char == "=":
            try:
                # Evaluate the current expression
                result = self.evaluate_expression(self.display.get())
                self.display.set(result)
            except:
                self.display.set("ERROR")
        elif char == "√":
            # Insert the square root function
            self.display.set(self.display.get() + "sqrt(")
        elif char in ["sin", "cos", "tan"]:
            # Insert trigonometric function
            self.display.set(self.display.get() + f"{char}(")
        elif char == "^":
            # Insert power operator
            self.display.set(self.display.get() + "**")
        elif char == "%":
            # Append percentage symbol
            self.display.set(self.display.get() + "/100")
        else:
            # Append the character to the display
            self.display.set(self.display.get() + char)

    def evaluate_expression(self, expression):
        """Evaluate the given expression with support for math functions."""
        # Replace function names with Python's math module functions
        expression = expression.replace("sqrt", "math.sqrt")
        expression = expression.replace("sin", "math.sin")
        expression = expression.replace("cos", "math.cos")
        expression = expression.replace("tan", "math.tan")

        # Evaluate the expression
        return eval(expression)


if __name__ == '__main__':
    Calculator().mainloop()
