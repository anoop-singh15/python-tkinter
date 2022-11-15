from tkinter import *
# initialisation
root = Tk()

# size of tk window
root.geometry("733x434")
root.minsize(733,434)

# background colour and tk window title
root.title("PyCharm")
root.configure(bg='#d0ae9b')

# create a label
label = Label(text="\n\nWELCOME TO PYCHARM",bg="#d0ae9b",fg="black",font="Helvetica 28 bold italic",bd=1)
label.pack(pady=20)


root.mainloop()
