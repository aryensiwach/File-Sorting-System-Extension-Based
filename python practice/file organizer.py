import os
from os import startfile
import shutil
import tkinter as tk
from tkinter import *
from tkinter import filedialog,messagebox
from PIL import ImageTk, Image
import customtkinter
from time import strftime
import random

root = customtkinter.CTk()
root.title("File Organizer")
root.geometry("550x550")
root.minsize(width=720,height=680)
root.configure()
selected_directory = None
root.resizable(False,True)
root.iconbitmap("G:\python\mini project\python practice\LOGO2.ico")
# root.resizable(False,False)


def sort():
    root = customtkinter.CTk()
    root.title("File Sorter")
    root.geometry("600x110")
    root.configure()
    root.minsize(width=600,height=110)
    root.iconbitmap("G:\python\mini project\python practice\LOGO2.ico")
    
        
    
    
    #select directory
    def select_directory():
        global selected_directory
    
        selected_dir = filedialog.askdirectory()
        if selected_dir:
            selected_directory = selected_dir
            directory_label=customtkinter.CTkLabel(master=root,text=f"Selected Directory: {selected_directory}", text_color="green").place(x=150,y=12)
        #sort files
    def sort_files_by_extension():
        if selected_directory:
            try:
                for file in os.listdir(selected_directory):
                    file_path = os.path.join(selected_directory, file)
                    if os.path.isfile(file_path):
                        file_extension = file.split('.')[-1]
                        folder_path = os.path.join(selected_directory, file_extension)
                        os.makedirs(folder_path, exist_ok=True)
                        shutil.move(file_path, os.path.join(folder_path, file))
                file_sorter_label = customtkinter.CTkLabel(master=root, text="Files sorted successfully based on file extensions." ,text_color="green").place(x=150,y=57)
                
            except Exception as e:
                file_sorter_label = customtkinter.CTkLabel(master=root, text="Error sorting files: ",text_color="red" ).place(x=150,y=57)
        else:
            file_sorter_label = customtkinter.CTkLabel(master=root, text="Please select a directory to sort files.",text_color="red" ).place(x=150,y=57)

    # sortframe=customtkinter.CTkFrame(master=root,width=400,height=200,fg_color="#4D4D4D").pack(side="bottom",fill=Y)
    
    select_directory_button = customtkinter.CTkButton(master=root, text="Select Directory", command=select_directory,hover_color="#00aa00").pack(side=TOP ,anchor=NW ,padx=5,pady=10)
    directory_label = customtkinter.CTkLabel(master=root, text="Selected Directory:").place(x=150,y=12)
    sort_files_button = customtkinter.CTkButton(master=root, text="Sort Files", command=sort_files_by_extension,hover_color="#00aa00").pack(side=TOP ,anchor=NW ,padx=5,pady=10)
    file_sorter_label = customtkinter.CTkLabel(master=root, text="" ).place(x=150,y=57)
     
   
    root.mainloop()

def folder():
    root = customtkinter.CTk()
    root.title("Create Folder")
    root.geometry("600x400")
    root.minsize(width=600,height=400)
    root.iconbitmap("G:\python\mini project\python practice\LOGO2.ico")
    def select_directory():
        global selected_directory
    
        selected_dir = filedialog.askdirectory()
        if selected_dir:
            selected_directory = selected_dir
            directory_label=customtkinter.CTkLabel(master=root,text=f"Selected Directory: {selected_directory}", text_color="green").place(x=150,y=12)
    def slider(value):
        global slider
        global num_folders
        
        num_folders_entry_label.configure(text=int(value))
        # print(int(value))
        
        num_folders = int(value)
    def create_folders(): 
        global num_folders
        folder_name = folder_name_entry.get()
        num_folders = int(num_folders)
        if selected_directory and folder_name and num_folders:
            # num_folders = int(num_folders)
            for i in range(num_folders):
                new_folder = os.path.join(selected_directory, f"{folder_name}_{i+1}")
                os.mkdir(new_folder)
            folder_created_label.configure(text=f"{num_folders} folders created successfully in '{selected_directory}'." ,text_color="green")
        else:
            folder_created_label.configure(text="Please select a directory and provide folder name and quantity.",text_color="red")

    select_directory_button = customtkinter.CTkButton(master=root, text="Select Directory", command=select_directory,hover_color="#00aa00").pack(side=TOP ,anchor=NW ,padx=5,pady=10)
    directory_label = customtkinter.CTkLabel(master=root, text="Selected Directory:").place(x=150,y=12)

    folder_name_label = customtkinter.CTkLabel(master=root, text="ENTER FOLDER NAME: ")
    folder_name_label.pack(pady=2,side=TOP,padx=2)

    folder_name_entry = customtkinter.CTkEntry(master=root, width=200)
    folder_name_entry.pack(pady=2,side=TOP,padx=2)
    num_folder_amount=customtkinter.CTkLabel(master=root,text="SELECT AMOUNT OF FOLDERS: ").pack(pady=5)
    num_folders_entry = customtkinter.CTkSlider(master=root, width=200, from_=0,to=100 ,command=slider,progress_color="#00aa00",border_width=5)
    num_folders_entry.set(0)
    num_folders_entry.pack(pady=5)
    num_folders_entry_label=customtkinter.CTkLabel(master=root ,text="" ,text_color="#D800FF",font=("monospace" , 20))
    num_folders_entry_label.pack(pady=5)
    create_folders_button = customtkinter.CTkButton(master=root, text="CREATE FOLDERS", command=create_folders,hover_color="#00aa00")
    create_folders_button.pack(pady=5)
    folder_created_label = customtkinter.CTkLabel(master=root, text="")
    folder_created_label.pack(pady=5)

    root.mainloop()

def rename():
    root = customtkinter.CTk()
    root.title("Rename folder")
    root.geometry("600x400")
    root.minsize(width=600,height=400)
    root.iconbitmap("G:\python\mini project\python practice\LOGO2.ico")

    def select_directory():
        global selected_directory
        selected_dir = filedialog.askdirectory()
        if selected_dir:
            selected_directory = selected_dir
            directory_label=customtkinter.CTkLabel(master=root,text=f"Selected Directory: {selected_directory}", text_color="green").place(x=150,y=12)
    def rename_folders():
        old_name = old_name_entry.get()
        new_name = new_name_entry.get()
        if selected_directory and old_name and new_name:
            try:
                os.rename(os.path.join(selected_directory, old_name), os.path.join(selected_directory, new_name))
                folder_renamed_label.configure(text=f"Folder '{old_name}' renamed to '{new_name}'.",text_color="green")
            except FileNotFoundError:
                folder_renamed_label.configure(text=f"Folder '{old_name}' not found." ,text_color="red")
    
        else:
            folder_renamed_label.configure(text="Please select a directory and provide both old and new folder names.",text_color="red")


    select_directory_button = customtkinter.CTkButton(master=root, text="Select Directory", command=select_directory,hover_color="#00aa00").pack(side=TOP ,anchor=NW ,padx=5,pady=10)
    directory_label = customtkinter.CTkLabel(master=root, text="Selected Directory:").place(x=150,y=12)
    old_name_label = customtkinter.CTkLabel(master=root, text="Old Name  ---->")
    old_name_label.place(x=13,y=55)

    old_name_entry = customtkinter.CTkEntry(master=root, width=160)
    old_name_entry.pack(pady=5)
    

    new_name_label = customtkinter.CTkLabel(master=root, text="New Name  --->")
    new_name_label.place(x=13,y=90)

    new_name_entry = customtkinter.CTkEntry(master=root, width=160)
    new_name_entry.pack(pady=5)
    

    rename_folders_button = customtkinter.CTkButton(master=root, text="Rename Folder", command=rename_folders,hover_color="#00aa00")
    rename_folders_button.pack(pady=5)

    folder_renamed_label = customtkinter.CTkLabel(master=root, text="")
    folder_renamed_label.pack(pady=5)

    root.mainloop()

def delete():
    root = customtkinter.CTk()
    root.title("Permanent Delete Files")
    root.geometry("600x400")
    root.minsize(width=600,height=400)
    root.iconbitmap("G:\python\mini project\python practice\LOGO2.ico")

    def select_directory():
        global selected_directory
        selected_dir = filedialog.askdirectory()
        if selected_dir:
            selected_directory = selected_dir
            directory_label=customtkinter.CTkLabel(master=root,text=f"Selected Directory: {selected_directory}", text_color="green").place(x=150,y=12)
    def select_files():
        files = filedialog.askopenfilenames(title="Select Files to Delete", filetypes=[("All Files", "*.*")])
        if files:
            for file_path in files:
                listbox.insert(tk.END, file_path)
    def delete_files():
        selected_files = listbox.curselection()
        if not selected_files:
            messagebox.showwarning("No Selection", "Please select files to delete.")
            return

        files_to_delete = [listbox.get(index) for index in selected_files]

        for file_path in files_to_delete:
            try:
                os.remove(file_path)
                listbox.delete(selected_files)  # Remove the item from the listbox
            except Exception as e:
                messagebox.showerror("Error", f"Error deleting file {file_path}: {e}")
    
                


    select_button = customtkinter.CTkButton(master=root, text="Select Files" ,command=select_files,hover_color="#00aa00")
    select_button.pack(pady=20)
    
    listbox = tk.Listbox(root, selectmode=tk.MULTIPLE,width=50)
    listbox.pack(pady=5)
    deletefiles=customtkinter.CTkLabel(master=root,text="Select files to delete-----> ").place(x=15,y=21)
    deleteitems=customtkinter.CTkLabel(master=root,text="Items-----> ").place(x=15,y=130)
    
    delete_button = customtkinter.CTkButton(master=root, text="Delete", command=delete_files ,hover_color="#00aa00")
    delete_button.pack(pady=5)

    root.mainloop()

# clock
def update_time():
    current_time = strftime('%H:%M:%S %p')
    time_label.config(text=current_time)
    time_label.config(fg="gray", bg="#212121")
    root.after(1000, update_time)  # Schedule the update every 1000 milliseconds (1 second)

def random_color():
    global color
    color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color

def help():
    startfile("G:\\python\\mini project\\python practice\\help.txt")
# main window
mainwindowframe3=customtkinter.CTkFrame(master=root,width=400,height=100,fg_color="#212121",corner_radius=0)
mainwindowframe3.pack(side="top",fill=X)
mainwindowframe3label=customtkinter.CTkLabel(master=mainwindowframe3,text="F",font=('Verdana',60 ,"bold"),text_color="red").place(x=80,y=9.4)
mainwindowframe3label2=customtkinter.CTkLabel(master=mainwindowframe3,text="ILE ORGANIZER",font=('Verdana',40 ,"bold"),text_color="white").place(x=119,y=30)
mainwindowframe=customtkinter.CTkFrame(master=root,width=120,height=400,fg_color="#4D4D4D",corner_radius=0)
mainwindowframe.pack(side="right",fill=Y)
mainwindowframe2=customtkinter.CTkFrame(master=root,width=50,height=400,fg_color="#4D4D4D",corner_radius=0)
mainwindowframe2.pack(side="left",fill=Y)

# img=PhotoImage(file="G:\\python\\python practice\\Cute-Ball-Help-icon.png",width=40,height=80)
label1=customtkinter.CTkLabel(master=mainwindowframe2,text="1. ",text_color="white",font=('Verdana',30 ,"bold") ).pack(side=TOP,anchor=NW,padx=20,pady=38,expand=True)
label2=customtkinter.CTkLabel(master=mainwindowframe2,text="2. ",text_color="white",font=('Verdana',30 ,"bold")).pack(side=TOP,anchor=NW,padx=20,pady=38,expand=True)
label3=customtkinter.CTkLabel(master=mainwindowframe2,text="3. ",text_color="white",font=('Verdana',30 ,"bold")).pack(side=TOP,anchor=NW,padx=20,pady=38,expand=True)
label4=customtkinter.CTkLabel(master=mainwindowframe2,text="4. ",text_color="white",font=('Verdana',30 ,"bold")).pack(side=TOP,anchor=NW,padx=20,pady=38,expand=True)
exit=customtkinter.CTkButton(master=mainwindowframe,text="EXIT",compound=LEFT,width=70,height=30,border_width=1,fg_color= "gray",hover_color="red",command=root.destroy, corner_radius=0).pack(side="bottom",anchor=NW,pady=30,padx=20)
help=customtkinter.CTkButton(master=mainwindowframe,text="HELP",compound=LEFT,width=70,height=30,border_width=1,fg_color="gray",hover_color="#00cc00",corner_radius=0,command=help).pack(side="bottom",anchor=NW,pady=0,padx=20)
sortbutton=customtkinter.CTkButton(master=root,text="Sort Files",corner_radius=0,width=10,height=50,hover_color="#00cc00",text_color="white",border_width=1 ,command=sort,font=('Verdana',19 ,"bold")).pack(expand=True,fill=BOTH)
createfolderbutton=customtkinter.CTkButton(master=root,text="Create Folder",corner_radius=0,width=10,height=50,hover_color="#00cc00",border_width=1,command=folder,font=('Verdana',20 ,"bold")).pack(expand=True,fill=BOTH)
renamefolderbutton=customtkinter.CTkButton(master=root,text="Rename Folder",corner_radius=0,width=10,height=50,hover_color="#00cc00",border_width=1,command=rename,font=('Verdana',20 ,"bold")).pack(expand=True,fill=BOTH)
deletefilebutton=customtkinter.CTkButton(master=root,text="Permanent Delete File",corner_radius=0,width=10,height=50,hover_color="#00cc00",border_width=1,command=delete,font=('Verdana',20 ,"bold")).pack(expand=True,fill=BOTH)
# clock
time_label = tk.Label(mainwindowframe3,font=('calibri', 12, 'bold'))
time_label.place(x=310,y=4)
update_time()
root.mainloop()