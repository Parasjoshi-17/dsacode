import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Simple Text Editor with Undo/Redo")
root.geometry("700x450")

# Global stacks for undo and redo
undo_stack = []
redo_stack = []

# ----------------- Undo Function -----------------
def undo_action(event=None):
    if undo_stack:
        current_text = textarea.get("1.0", tk.END).strip()
        redo_stack.append(current_text)  # Save for redo
        previous_text = undo_stack.pop()
        textarea.delete("1.0", tk.END)
        textarea.insert(tk.END, previous_text)
    else:
        messagebox.showinfo("Undo", "Nothing to undo!")

# ----------------- Redo Function -----------------
def redo_action(event=None):
    if redo_stack:
        current_text = textarea.get("1.0", tk.END).strip()
        undo_stack.append(current_text)  # Save for undo
        next_text = redo_stack.pop()
        textarea.delete("1.0", tk.END)
        textarea.insert(tk.END, next_text)
    else:
        messagebox.showinfo("Redo", "Nothing to redo!")

# ----------------- Track Changes -----------------
def on_key_press(event):
    text = textarea.get("1.0", tk.END).strip()
    if not undo_stack or (undo_stack and text != undo_stack[-1]):
        undo_stack.append(text)

# ----------------- Layout -----------------
# Button frame at top
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(side="top", fill="x", pady=5)

# Undo and Redo buttons
undo_btn = tk.Button(button_frame, text="Undo", width=12, bg="#d9d9d9", command=undo_action)
undo_btn.pack(side="left", padx=10, pady=5)

redo_btn = tk.Button(button_frame, text="Redo", width=12, bg="#d9d9d9", command=redo_action)
redo_btn.pack(side="left", padx=10, pady=5)

# Text area below buttons
textarea = tk.Text(root, wrap="word", font=("Consolas", 12))
textarea.pack(expand=True, fill="both", padx=10, pady=5)

# Bind key press to record changes
textarea.bind("<KeyRelease>", on_key_press)

# Keyboard shortcuts
root.bind("<Control-z>", undo_action)
root.bind("<Control-y>", redo_action)

# Run the app
root.mainloop()

------------------------------------------------------------------------------------------------------------------------------------------

import ipywidgets as widgets
from IPython.display import display, clear_output

# --- Create Widgets ---
textarea = widgets.Textarea(
    value='',
    placeholder='Write something...',
    description='Editor:',
    layout=widgets.Layout(width='90%', height='150px')
)

undo_button = widgets.Button(description="Undo", button_style='warning')
redo_button = widgets.Button(description="Redo", button_style='success')

# --- Display widgets in a nice row ---
button_box = widgets.HBox([undo_button, redo_button])
display(button_box, textarea)

# --- Undo/Redo logic ---
undo_stack = []
redo_stack = []

def on_text_change(change):
    """Track text changes and push them to the undo stack."""
    new_value = change['new']
    if not undo_stack or undo_stack[-1] != new_value:
        undo_stack.append(new_value)
        # Clear redo stack because a new change resets redo history
        redo_stack.clear()

def undo_action(b):
    """Handle Undo button click."""
    if len(undo_stack) > 1:
        current = undo_stack.pop()          # Remove current state
        redo_stack.append(current)          # Save to redo stack
        previous = undo_stack[-1]           # Go to previous state
        textarea.unobserve(on_text_change, names='value')  # Temporarily stop tracking
        textarea.value = previous
        textarea.observe(on_text_change, names='value')
    else:
        print("Nothing to undo!")

def redo_action(b):
    """Handle Redo button click."""
    if redo_stack:
        next_value = redo_stack.pop()
        undo_stack.append(next_value)
        textarea.unobserve(on_text_change, names='value')
        textarea.value = next_value
        textarea.observe(on_text_change, names='value')
    else:
        print("Nothing to redo!")

# --- Connect buttons and observers ---
textarea.observe(on_text_change, names='value')
undo_button.on_click(undo_action)
redo_button.on_click(redo_action)
