
"""
w = ''.join([str(random.randint(0,9)) for i in range(4)])

server = smtplib.SMTP('smtp.gmail.com',587)#connect server
server.starttls()
server.login('saimohitha2002@gmail.com',password)
msg = "Hello,Your otp is" +str(w)
server.sendmail("saimohitha2002@gmail.com","saimohitha627@gmail.com",msg)
server.quit()"""
"""
import random
import smtplib
import getpass

# Generate a random OTP
def generate_otp():
    return random.randint(1000, 9999)

# Send OTP code via email
def send_otp_email(email, otp):
    smtp_server = "smtp.gmail.com"  # Enter your SMTP server address
    smtp_port = 587  # Enter your SMTP server port

    sender_email = "saimohitha627@gmail.com"  # Enter your email address
    sender_password = getpass.getpass("Enter your email password: ")

    message = f"Subject: OTP Verification\n\nYour OTP code is: {otp}"

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, message)
        print("OTP has been sent successfully.")
    except smtplib.SMTPAuthenticationError:
        print("Failed to authenticate with the provided email credentials.")
    except smtplib.SMTPException as e:
        print("An error occurred while sending the email:", str(e))

# Verify the OTP code entered by the user
def verify_otp(otp, user_input):
    return otp == int(user_input)

# Main program
def otp_verification():
    email = input("Enter your email address: ")

    otp = generate_otp()
    send_otp_email(email, otp)

    user_input = input("Enter the OTP code sent to your email: ")

    if verify_otp(otp, user_input):
        print("OTP verification successful.")
    else:
        print("OTP verification failed.")

# Run the OTP verification
otp_verification()"""

""""
import random
import tkinter as tk
from tkinter import messagebox

def generate_otp():
    otp = random.randint(1000, 9999)
    return otp

def verify_otp():
    user_otp = otp_entry.get()
    if user_otp == str(otp):
        messagebox.showinfo("Success", "OTP verification successful!")
    else:
        messagebox.showerror("Error", "Invalid OTP!")

def send_otp():
    global otp
    otp = generate_otp()
    messagebox.showinfo("OTP", f"Your OTP is: {otp}")

# Create the main window
window = tk.Tk()
window.title("OTP Verification")
window.geometry("200x200")

# Create a label
label = tk.Label(window, text="Enter OTP:")
label.pack()

# Create an entry field
otp_entry = tk.Entry(window)
otp_entry.pack()

# Create a verify button
verify_button = tk.Button(window, text="Verify OTP", command=verify_otp)
verify_button.pack()

# Create a send button
send_button = tk.Button(window, text="Send OTP", command=send_otp)
send_button.pack()

# Start the main loop
window.mainloop()"""



import random
import smtplib
from tkinter import *
from tkinter import messagebox


# Generate random OTP
def generate_otp():
    otp = random.randint(1000, 9999)
    return otp

# Send OTP via Gmail
def send_otp(email, otp):
    gmail_user = 'saimohitha2002@gmail.com'
    gmail_password = 'qtwrtwburtkltjit'

    sent_from = gmail_user
    to = 'saimohitha627@gmail.com'
    subject = 'OTP Verification'
    body = f'Your OTP is: {otp}'

    email_text = f"From: {sent_from}\nTo: {', '.join(to)}\nSubject: {subject}\n\n{body}"

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        return True
    except:
        return False

# Verify OTP
def verify_otp():
    user_otp = otp_entry.get()

    if user_otp == str(otp):
        messagebox.showinfo("Success", "OTP verification successful!")
    else:
        messagebox.showerror("Error", "OTP verification failed!")

# Generate and send OTP when button is clicked
def send_otp_clicked():
    email = email_entry.get()

    global otp
    otp = generate_otp()

    if send_otp(email, otp):
        messagebox.showinfo("Success", "OTP sent successfully!")
    else:
        messagebox.showerror("Error", "Failed to send OTP!")

# Create UI
root = Tk()
root.title("OTP Verification")
root.geometry("400x400")

email_label = Label(root, text="Email:")
email_label.pack()
email_entry = Entry(root)
email_entry.pack()

otp_button = Button(root, text="Send OTP", command=send_otp_clicked)
otp_button.pack()

otp_label = Label(root, text="OTP:")
otp_label.pack()
otp_entry = Entry(root)
otp_entry.pack()

verify_button = Button(root, text="Verify OTP", command=verify_otp)
verify_button.pack()

root.mainloop()

