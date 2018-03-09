from Tkinter import * 

def hello():
    print "Hello!"

root = Tk()
frame = Frame(root)
frame.pack()

topframe = Frame(root)
topframe.pack( side = TOP )

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

middleframe = Frame(root)
middleframe.pack()

# top
redbutton = Button(topframe, text="Red", fg="red", command=hello)
redbutton.pack( side = LEFT)

greenbutton = Button(topframe, text="Brown", fg="brown", command=hello)
greenbutton.pack( side = RIGHT )

bluebutton = Button(topframe, text="Blue", fg="blue", command=hello)
bluebutton.pack( side = TOP )

blackbutton = Button(topframe, text="Black", fg="black", command=hello)
blackbutton.pack( side = BOTTOM)

#middle
c = Canvas(middleframe, bg="grey", height=200, width=200)
coord = 10,50,240,210
arc = c.create_line(coord, fill="red")
c.pack()

c.pack()
#bottom
redbutton = Button(bottomframe, text="Red", fg="red", command=hello)
redbutton.pack( side = LEFT)

greenbutton = Button(bottomframe, text="Brown", fg="brown", command=hello)
greenbutton.pack( side = RIGHT )

bluebutton = Button(bottomframe, text="Blue", fg="blue", command=hello)
bluebutton.pack( side = TOP )

blackbutton = Button(bottomframe, text="Black", fg="black", command=hello)
blackbutton.pack( side = BOTTOM)

#menubar
menubar = Menu(root)

  # create a pulldown menu, and add it to the menu bar
filemenu = Menu(root, tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

  # create more pulldown menus
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=hello)
menubar.add_cascade(label="Help", menu=helpmenu)

  # display the menu
root.config(menu=menubar)
root.mainloop()
