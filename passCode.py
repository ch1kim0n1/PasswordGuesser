import PyPDF2
import string
import itertools
import os
import tkinter as tk
from tkinter import messagebox

pdf_file = r"YOUR/FILE/HERE"

# Verify PDF file exists
if not os.path.isfile(pdf_file):
    print(f"File not found: {pdf_file}")
else:
    print(f"File found: {pdf_file}")

characters = string.ascii_letters + string.digits + string.punctuation  

attempts = 0

def unlock_pdf(file, password):
    try:
        with open(pdf_file, 'rb') as file:
            pdf = PyPDF2.PdfReader(file)
            if pdf.decrypt(password):
                show_popup(f"HORAY! The password is - {password}")
                return True
            else:
                return False
    except Exception as e:
        print(f"Error: {e}")
        return False
    
def show_popup(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Password Found", message)
    root.destroy()

for length in range(6, 25):
    for guess in itertools.product(characters, repeat=length):
        guess = ''.join(guess) 
        print(f"Password guess - {guess}", end=" ")
            
        if unlock_pdf(pdf_file, guess):
            print("success")
            break
        else:
            print("fail")
