import ctypes
import random
import tkinter as tk
from time import sleep
import pyautogui

user32 = ctypes.windll.user32
screensize = [user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)]
pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False


class AutoMoveMouse(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Auto Move Mouse")
        self.resizable(False, False)
        self.geometry("350x100")
        self.title = tk.Label(text="Auto Move Mouse",
                              font=("Arial", 26)).grid(row=0, column=0, pady=20, sticky='ew',)
        self.config(bg='grey')
        self.bind('<KeyPress>', lambda e: self.pressed_button(e))
        self.looprun = False

    def pressed_button(self, event):
        print(event.char.upper())
        if event.char.upper() == 'Q':
            self.config(bg='green')
            self.update()
            self.looprun = True
            self.loop()
        elif event.char.upper() == 'Z':
            self.config(bg='grey')
            self.looprun = False
            self.update()
        else:
            pass

    def loop(self):
        time_sleep = random.randrange(3)
        self.bind('<KeyPress>', lambda e: self.pressed_button(e))
        if self.looprun:
            self.after(time_sleep, self.loop)
        pyautogui.moveTo(random.randrange(screensize[0]), random.randrange(screensize[1]), duration=1)
        sleep(time_sleep)


if __name__ == '__main__':
    AutoMoveMouse().mainloop()
