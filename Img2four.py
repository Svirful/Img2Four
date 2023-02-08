import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

def add_transparency(img):
    width, height = img.size
    if width % 4 != 0 or height % 4 != 0:
        new_width = width + (4 - (width % 4)) if width % 4 != 0 else width
        new_height = height + (4 - (height % 4)) if height % 4 != 0 else height
        transparent = Image.new("RGBA", (new_width, new_height), (255, 255, 255, 0))
        ratio = min(new_width / width, new_height / height)
        new_img = img.resize((int(width * ratio), int(height * ratio)))
        transparent.paste(new_img, (int((new_width - new_img.width) / 2), int((new_height - new_img.height) / 2)))
        return transparent
    return img

def change_resolution(path):
    for filename in os.listdir(path):
        img = Image.open(os.path.join(path, filename))
        img = add_transparency(img)
        img.save(os.path.join(path, filename))

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        change_resolution(folder_path)
        messagebox.showinfo("Success", "The resolution of the images in the selected folder has been changed successfully!")
    else:
        messagebox.showerror("Error", "No folder was selected.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Change Image Resolution")
    tk.Button(root, text="Select Folder", command=select_folder).pack()
    root.mainloop()