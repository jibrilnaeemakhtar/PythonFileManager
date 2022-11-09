# IMPORT REQUIRED MODULES
from tkinter import *                                         # provides wide APIs for GUI functionalities
import shutil                                                 # offers a number of high-level operations on files and file collections
import os                                                     # utility model for OS interaction in programs
import easygui                                                # allows selection of any file from the system
from tkinter import filedialog                                # used for folder selection
from tkinter import messagebox as mb                          # used to read the file chosen by file box, using a path


# PRESENTS A FILE BOX WINDOW TO SELECT A FILE
def open_window():
    read = easygui.fileopenbox()                              # opens pop-up box to allow file selection
    return read

# OPEN FILES FUNCTION
def open_file():
    string = open_window()                                    # stores returned path of chosen file
    try:
        os.startfile(string)                                  # if file is chosen, function opens the file
    except:
        mb.showinfo('confirmation', "File not found.")        # pop-up message box if no file is chosen or found

# COPY FILES FUNCTION
def copy_file():
    source1 = open_window()                                   
    destination1 = filedialog.askdirectory()                  # stores destination folder address returned by askdirectory()
    shutil.copy(source1, destination1)                        # copies file present at source1 to destination1 address
    mb.showinfo('confirmation', "File has been copied.")      
    
# DELETE FILES FUNCTION
def delete_file():
    del_file = open_window()                                  
    if os.path.exists(del_file):
        os.remove(del_file)                                   # deletes file if path to chosen file exists
    else:
        mb.showinfo('confirmation', "File not found.")        
        
# RENAME FILES FUNCTION
def rename_file():
    chosen_file = open_window()                               
    path1 = os.path.dirname(chosen_file)                      # stores path of directory of chosen file
    extension = os.path.splitext(chosen_file)[1]              # splits path into root and extensions
    print("Enter a new name for the chosen file.")
    new_name = input()                                        # new file name is stored
    path = os.path.join(path1, new_name + extension)          # new file name is joined to the root and extension
    print(path)
    os.rename(chosen_file,path)                               # file is re-named
    mb.showinfo('confirmation', "File's name has been changed.")
    
# MOVE FILES FUNCTION
def move_file():
    source = open_window()
    destination = filedialog.askdirectory()                   # stores destination folder address 
    if(source == destination):                                # doesn't allow moving if source and destination are identical
        mb.showinfo('confirmation', "Source and destination are the same.")
    else:
        shutil.move(source, destination)                      # moves file if source and destination aren't identical
        mb.showinfo('confirmation', "File has been moved.")
    
# MAKE NEW FOLDERS FUNCTION
def make_folder():
    new_folder_path = filedialog.askdirectory()
    print("Enter name of new folder")
    new_folder = input()
    path = os.path.join(new_folder_path, new_folder)          # new folder path is created
    os.mkdir(path)                                            # new folder is created
    mb.showinfo('confirmation', "Folder created.")
    
# DELETE FOLDERS FUNCTION
def remove_folder():
    del_folder = filedialog.askdirectory()
    os.rmdir(del_folder)                                      # folder is deleted
    mb.showinfo('confirmation', "Folder deleted.")


# LIST ALL FILES IN FOLDER FUNCTION
def list_files():
    folder_list = filedialog.askdirectory()
    sort_list = sorted(os.listdir(folder_list))               # lists all files present in selected folder
    i = 0
    print("Files in ", folder_list, "folder are: ")
    while(i < len(sort_list)):                                # list is sorted using while loop
        print(sort_list[i] + '\n')
        i += 1

        
# BUILD FILE MANAGER UI USING TKINTER
root = Tk()                                                                 # creates window

canv = Canvas(root, width = 500, height = 420, bg = 'white')                
canv.grid(row = 0, column = 2)
img = ImageTk.PhotoImage(Image.open("/Users/jibril/Documents/Portfolio/Website/gold-background.jpg"))  
canv.create_image(20, 20, anchor = NW, image = img)                         # create canvas for window

# creating label and buttons to perform operations
Label(root, text = "Python File Manager", font = ("Helvetica", 16), fg = "blue").grid(row = 5, column = 2) 
Button(root, text = "Open a File", command = open_file).grid(row=15, column =2)
Button(root, text = "Copy a File", command = copy_file).grid(row = 25, column = 2)
Button(root, text = "Delete a File", command = delete_file).grid(row = 35, column = 2)
Button(root, text = "Rename a File", command = rename_file).grid(row = 45, column = 2)
Button(root, text = "Move a File", command = move_file).grid(row = 55, column =2)
Button(root, text = "Make a Folder", command = make_folder).grid(row = 75, column = 2)
Button(root, text = "Remove a Folder", command = remove_folder).grid(row = 65, column =2)
Button(root, text = "List all Files in Folder", command = list_files).grid(row = 85,column = 2)
root.mainloop()






