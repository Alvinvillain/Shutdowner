import tkinter as tk
from tkinter import ttk
import os
import webbrowser

def greet_shutdowner(event=None):
    user_name = name_entry.get()
    result_label_tab1.config(text=f"Hello {user_name}, I am SHUTDOWNER.")
    continue_button_tab1.pack(pady=10)  # Show the continue button
    continue_button_tab1.config(state=tk.NORMAL)  # Activate the continue button

def switch_to_tab2():
    notebook.select(tab2_frame)  # Switch to tab2_frame (Instructions)

def execute_shutdown():
    choice = choice_var.get()

    if choice in ["Shutdown", "Restart"]:
        os.system(f'shutdown /{choice.lower()[0]} /t {choice1_var.get()}')
        info_label.config(text=f"A {choice} has been scheduled")
    elif choice == "Logout":
        os.system(f'shutdown /l')
        info_label.config(text=f"A {choice} has been scheduled")
    elif choice == "Abort":
        os.system(f'shutdown /a')
        info_label.config(text=f"An {choice} has been executed")
    
    # Update info label and display continue button in Tab 2
    continue_button_tab2.pack(pady=10)  # Show the continue button in tab2
    continue_button_tab2.config(state=tk.NORMAL)  # Activate the continue button

def close_app():
    # Switch to tab3_frame (Thank You)
    notebook.select(tab3_frame)
    
    # Display thank you message and details
    thank_you_label.config(text=f"Thank you for using OAR services, {name_entry.get()}!\n"
                                "Have a great day!")

    contact_label.pack(pady=20)  # Display contact information
    email_link.pack(pady=5)  # Display email link
    whatsapp_link.pack(pady=5)  # Display WhatsApp link
    close_button.pack(pady=10)  # Show the close button in tab3

# Function to open email link
def open_email_link(event):
    # Replace with your email address
    webbrowser.open_new_tab("mailto:alvinoar49@gmail.com")

# Function to open WhatsApp link
def open_whatsapp_link(event):
    # Replace with your WhatsApp links
    webbrowser.open_new_tab("https://wa.me/256772543045")
    webbrowser.open_new_tab("https://wa.me/256755853319")

root = tk.Tk()
root.title("Shutdown Automation")

notebook = ttk.Notebook(root)
notebook.pack(pady=10, padx=10, fill='both', expand=True)

# Tab 1: Enter Name
tab1_frame = ttk.Frame(notebook)
notebook.add(tab1_frame, text='Enter Name')

title_label_tab1 = tk.Label(tab1_frame, text="Shutdown Automation", font=("Helvetica", 16))
title_label_tab1.pack(pady=10)

name_label = tk.Label(tab1_frame, text="Enter your name:")
name_label.pack(pady=5, anchor=tk.W)
name_entry = tk.Entry(tab1_frame)
name_entry.pack(pady=5)
name_entry.bind("<Return>", greet_shutdowner)  # Bind Enter key to greet_shutdowner function

result_label_tab1 = tk.Label(tab1_frame, text="", font=("Helvetica", 12), fg="blue")
result_label_tab1.pack(pady=5)

continue_button_tab1 = tk.Button(tab1_frame, text="Continue", command=switch_to_tab2, state=tk.DISABLED)
continue_button_tab1.pack_forget()  # Continue button initially hidden

# Tab 2: Instructions or Options
tab2_frame = ttk.Frame(notebook)
notebook.add(tab2_frame, text='Instructions')

choice_var = tk.StringVar()
choice_label = tk.Label(tab2_frame, text="Choose an option:")
choice_label.pack(pady=10)

choices = ["Shutdown", "Logout", "Restart", "Abort"]
choice_dropdown = tk.OptionMenu(tab2_frame, choice_var, *choices)
choice_dropdown.pack(pady=5)

choice1_label = tk.Label(tab2_frame, text="Seconds (for Shutdown/Restart):")
choice1_label.pack(pady=5)

choice1_var = tk.StringVar()
choice1_entry = tk.Entry(tab2_frame, textvariable=choice1_var)
choice1_entry.pack(pady=5)

info_label = tk.Label(tab2_frame, text="Choose an option and enter seconds (if applicable).", font=("Helvetica", 12))
info_label.pack(pady=10)

execute_button = tk.Button(tab2_frame, text="Execute", command=execute_shutdown)
execute_button.pack(pady=10)

continue_button_tab2 = tk.Button(tab2_frame, text="Continue", command=close_app, state=tk.DISABLED)
continue_button_tab2.pack_forget()  # Continue button initially hidden

# Tab 3: Thank You Message and Contact Information
tab3_frame = ttk.Frame(notebook)
notebook.add(tab3_frame, text='Thank You')

thank_you_label = tk.Label(tab3_frame, text="", font=("Helvetica", 16))
thank_you_label.pack(pady=50)

contact_label = tk.Label(tab3_frame, text="For more services, contact us via:")
contact_label.pack(pady=20)

email_link = tk.Label(tab3_frame, text="Email: alvinoar49@gmail.com", fg="blue", cursor="hand2")
email_link.pack(pady=5)
email_link.bind("<Button-1>", open_email_link)

whatsapp_link = tk.Label(tab3_frame, text="WhatsApp: Click to Chat", fg="blue", cursor="hand2")
whatsapp_link.pack(pady=5)
whatsapp_link.bind("<Button-1>", open_whatsapp_link)

close_button = tk.Button(tab3_frame, text="Close", command=root.quit)
close_button.pack(pady=10)
close_button.pack_forget()  # Hide the close button initially

# Start with Tab 1 selected
notebook.select(tab1_frame)

root.mainloop()
