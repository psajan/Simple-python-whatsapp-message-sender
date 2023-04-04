import tkinter as tk
from tkinter import messagebox
import pywhatkit as whatsapp
import datetime

def send_message():
    phone_number = phone_number_field.get()
    message = message_field.get("1.0", "end-1c")
    
    try:
        whatsapp.sendwhatmsg_instantly(f"+{phone_number}", message)
        messagebox.showinfo("Message Sent", f"Message sent to {phone_number}: {message}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Send WhatsApp Message")

# Phone Number Field
phone_number_label = tk.Label(root, text="Phone Number (with country code, without '+')")
phone_number_label.pack()
phone_number_field = tk.Entry(root)
phone_number_field.pack()

# Message Field
message_label = tk.Label(root, text="Message")
message_label.pack()
message_field = tk.Text(root, height=5)
message_field.pack()

# Send Button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()
