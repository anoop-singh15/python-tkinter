from tkinter import  *
from PIL import Image,ImageTk   # pyhton imaging library = pillow



# initialisation
root=Tk()

# size
root.geometry("252x448")

# image of .png type needs label
# image_1=PhotoImage(file="E:\pycharm\pycharm project\Images for GUI/'ENTER name here'")

# FOR JPG IMAGES USE pillow //syntax below
image=Image.open("E:\pycharm\pycharm project\Images for GUI/SL.jpg")
image_1=ImageTk.PhotoImage(image)

#now pack image in a label
image_label_1=Label(image=image_1)
image_label_1.pack()






# End and main
root.mainloop()