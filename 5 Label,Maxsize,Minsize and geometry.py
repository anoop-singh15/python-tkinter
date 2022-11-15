from  tkinter import *

# intialisation
instance_root = Tk()

# width X height for gui's size
instance_root.geometry("444x474")

#width,height to lock minimum size, size cannot become lesser than minsize
instance_root.minsize(444,474)

#width,height to lock maximum size, size cannot become larger than maxsize
# instance_root.maxsize(444,474)

# Label to  print things at tk window
label = Label(text="\nHello World \n\nThis Is My First GUI")
label.pack()


# GUI  Logic here
instance_root.mainloop()