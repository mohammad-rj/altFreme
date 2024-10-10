import tkinter as tk
import keyboard
import screeninfo

# Get the screen width to position the window at the right edge
screen = screeninfo.get_monitors()[0]
screen_width = screen.width

# Create the main window
root = tk.Tk()
root.overrideredirect(True)  # Remove window title and control buttons
root.geometry(f"5x10+{screen_width - 5}+0")  # Set size and position at the top-right corner
root.attributes("-topmost", True)  # Keep the window always on top
root.attributes("-transparentcolor", "white")  # Set transparency for white background

# Create a Frame widget to display the Alt key color
frame_alt = tk.Frame(root, bg="white", width=5, height=5)
frame_alt.pack()

# Create a Frame widget to display the Shift key color
frame_shift = tk.Frame(root, bg="white", width=5, height=5)
frame_shift.pack()

# Function to change the frame colors based on the pressed keys
def check_keys():
    if keyboard.is_pressed('alt'):
        frame_alt.config(bg="red")  # Change color to red for Alt
    else:
        frame_alt.config(bg="white")  # Revert to transparent for Alt

    if keyboard.is_pressed('shift'):
        frame_shift.config(bg="green")  # Change color to green for Shift
    else:
        frame_shift.config(bg="white")  # Revert to transparent for Shift

    root.after(100, check_keys)  # Check every 100 milliseconds

# Start checking keys
check_keys()

# Run the application
root.mainloop()
