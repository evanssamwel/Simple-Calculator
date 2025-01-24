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
        self.current_mode = "Light Mode"

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
                result = eval(self.display.get())
                self.display.set(result)
            except:
                self.display.set("ERROR")
        elif char == "√":
            try:
                # Handle square root; evaluate the display if a number exists, otherwise assume 0
                value = float(self.display.get()) if self.display.get() else 0
                self.display.set(math.sqrt(value))
            except:
                self.display.set("ERROR")
        elif char in ["sin", "cos", "tan"]:
            try:
                # Handle trigonometric functions; assume radians
                value = float(self.display.get()) if self.display.get() else 0
                if char == "sin":
                    self.display.set(math.sin(math.radians(value)))
                elif char == "cos":
                    self.display.set(math.cos(math.radians(value)))
                elif char == "tan":
                    self.display.set(math.tan(math.radians(value)))
            except:
                self.display.set("ERROR")
        elif char == "^":
            # Power (e.g., 2^3 = 2**3)
            self.display.set(self.display.get() + "**")
        elif char == "%":
            try:
                # Percentage
                value = float(self.display.get())
                self.display.set(value / 100)
            except:
                self.display.set("ERROR")
        else:
            # Append the character to the display
            self.display.set(self.display.get() + char)


if __name__ == '__main__':
    Calculator().mainloop()
