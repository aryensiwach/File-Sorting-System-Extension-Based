import tkinter as tk
from time import strftime
import random

def update_time():
    current_time = strftime('%H:%M:%S %p')
    time_label.config(text=current_time)
    time_label.config(fg=random_color(), bg=random_color())
    root.after(1000, update_time)  # Schedule the update every 1000 milliseconds (1 second)

def random_color():
    color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color

root = tk.Tk()
root.title("Colorful Animated Clock")
root.geometry("400x200")

time_label = tk.Label(root, font=('calibri', 40, 'bold'))
time_label.pack(anchor='center')

update_time()

root.mainloop()
