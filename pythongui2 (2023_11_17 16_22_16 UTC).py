import tkinter as tk
import os
from PyPDF2 import PdfWriter,PdfReader
import shutil
from tkinter import filedialog
from tkinter import ttk
from sys import platform
root = tk.Tk()
root.title('PDF Editor')
root.geometry('400x200')
print("Click open file to choose pdf to encrypt.")
def openPDF():
    root.filename = filedialog.askopenfilename(title = "Select a File",filetypes=(("PDF Files","*.pdf"),))
    original_path = root.filename
    current_dir = os.getcwd()
    print("Current directory" + current_dir)
    shutil.copy(original_path,current_dir)
    print("File Copied")
    pdfwrite = PdfWriter()
    #Get Original Name of PDf and Location Name
    print(os.path.split(root.filename))
    pdf_name = os.path.split(root.filename)[1]
    
    if platform == "win32":
        destination_dir = current_dir + "\\" + pdf_name
        pdf_encrypt_name = current_dir + "\\" + pdf_name.replace(".pdf","_encrypt.pdf")
    elif platform == "darwin":
        destination_dir = current_dir + "/" + pdf_name
        pdf_encrypt_name = current_dir + "/" + pdf_name.replace(".pdf","_encrypt.pdf")
    pdf = PdfReader(destination_dir)
    for page_num in pdf.pages:
        pdfwrite.add_page(page_num)

    password = input("Enter Password: ")
    pdfwrite.encrypt(password)
    print("Choose a location to download encrypted pdf")

    with open(pdf_encrypt_name,"wb") as f:
        pdfwrite.write(f)
    destination2 = filedialog.askdirectory()
    shutil.copy(pdf_encrypt_name,destination2)
    print("encrypted pdf is now downloaded")



button = tk.Button(root,text = "Open File", command = openPDF).pack()

#Adds unprotected pdf to working dir, gives it password, saves to downloads













# A
root.mainloop()

