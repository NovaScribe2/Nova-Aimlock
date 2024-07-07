import tkinter as tk
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Listener, KeyCode

mouse = MouseController()
aimlock_key = KeyCode(char='e')
target_locked = False

def find_target():
    # Placeholder function: Replace with actual logic to find the target
    return (400, 300)  # Example: Fixed screen position

def aimlock():
    global target_locked
    target_locked = not target_locked
    if target_locked:
        target_pos = find_target()
        mouse.position = target_pos

def on_press(key):
    if key == aimlock_key:
        aimlock()

def create_gui():
    window = tk.Tk()
    window.title("Da Hood Camlock")

    frame = tk.Frame(window)
    frame.pack(pady=20)

    toggle_btn = tk.Button(frame, text="Toggle Aimlock (E)", command=aimlock)
    toggle_btn.pack()

    window.mainloop()

# Setup the key listener
with Listener(on_press=on_press) as listener:
    create_gui()
    listener.join()
