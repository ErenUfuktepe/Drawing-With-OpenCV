import tkinter as tk
from tkinter.colorchooser import askcolor
import pyautogui


class Settings:
    window = None
    # Window components, e.g., button and entry.
    # Index 0 represents Rectangle button.
    # Index 1 represents Circle button.
    # Index 2 represents Pen button.
    # Index 3 represents Color button.
    # Index 4 represents Pen Thickness entry.
    # Index 5 represents Circle Size entry.
    window_components = [object, object, object, object, object, object]
    width, height = pyautogui.size()
    # Default variables.
    dynamic_setting = ['pen', (0, 255, 0), 3, 50]

    # Creates main window for settings bar.
    def start(self):
        self.window = tk.Tk()
        self.window.title("Settings")
        self.window.geometry(self.initialize_window_size(450, 100))
        self.set_main_window_buttons()

    # Close windows
    def close(self):
        self.window.destroy()

    # Setting main window components.
    def set_main_window_buttons(self):
        app = tk.Frame(self.window)
        app.grid()

        self.window_components[0] = tk.Button(app, text="Rectangle",
                                              command=lambda: self.set_operation('rectangle', self.dynamic_setting[2],
                                                                                 self.dynamic_setting[3]), bg='red')
        self.window_components[0].pack(side=tk.LEFT)

        self.window_components[1] = tk.Button(app, text="Circle",
                                              command=lambda: self.set_operation('circle', self.dynamic_setting[2],
                                                                                 self.dynamic_setting[3]), bg='red')
        self.window_components[1].pack(side=tk.LEFT)

        self.window_components[2] = tk.Button(app, text="Pen",
                                              command=lambda: self.set_operation('pen', self.dynamic_setting[2],
                                                                                 self.dynamic_setting[3]), bg='green')
        self.window_components[2].pack(side=tk.LEFT)

        self.window_components[3] = tk.Button(app, text="Color", command=self.change_color)
        self.window_components[3].pack(side=tk.LEFT)

        label1 = tk.Label(self.window, text="Pen Thickness")
        label1.grid(row=1, column=0, pady=10, sticky="W")
        label2 = tk.Label(self.window, text="Circle Size")
        label2.grid(row=1, column=0, pady=10, sticky="E")

        self.window_components[4] = tk.Entry(self.window, width=5)
        self.window_components[4].grid(row=1, column=0, pady=10)
        self.window_components[4].insert(0, 3)

        self.window_components[5] = tk.Entry(self.window, width=5)
        self.window_components[5].grid(row=1, column=2, pady=0)
        self.window_components[5].insert(0, 50)

        submit = tk.Button(app, text="Submit Size", command=lambda: self.set_operation(self.dynamic_setting[0],
                                                                                       self.dynamic_setting[2],
                                                                                       self.dynamic_setting[3]))
        submit.pack(side=tk.LEFT)

        self.window.mainloop()

    # Puts the settings bar into the middle of the screen.
    def initialize_window_size(self, width, height):
        width_x = int((self.width / 2) - int(width / 2))
        height_x = int((self.height / 2) - int(height / 2))
        return str(width) + "x" + str(height) + "+" + str(width_x) + "+" + str(height_x)

    # Change color action. Changes the drawing color.
    def change_color(self):
        result = askcolor(color="#6A9662", title="Change Color")
        self.window_components[3].configure(bg=result[1])
        if result[0] is not None:
            res = [(sub[2], sub[1], sub[0]) for sub in result[0:]]
            self.dynamic_setting[1] = res[0]

    # Returns settings such as operation(rectangle, circle, pen), thickness of pen, circle size and color.
    def get_dynamic_settings(self):
        return self.dynamic_setting

    # Setting operation, thickness of pen and size of the circle size.
    def set_operation(self, operation, thickness, size):
        self.show_active_button(operation)
        thickness = self.window_components[4].get()
        size = self.window_components[5].get()
        if thickness.isdigit():
            self.dynamic_setting[2] = int(thickness)
        if size.isdigit():
            self.dynamic_setting[3] = int(size)
        self.dynamic_setting[0] = operation

    # Shows active button. Changes the button's color to green if it is active otherwise change the color to red.
    def show_active_button(self, operation):
        flag = 0
        if operation == 'rectangle':
            flag = 0
        elif operation == 'circle':
            flag = 1
        elif operation == 'pen':
            flag = 2
        for index in range(0, 3):
            if flag == index:
                self.window_components[index].configure(bg='green')
            else:
                self.window_components[index].configure(bg='red')

