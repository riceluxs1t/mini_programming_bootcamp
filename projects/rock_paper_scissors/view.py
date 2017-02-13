from Tkinter import *


class GUI:

    def __init__(self, master):

        self.master = master

        frame = Frame(self.master)
        frame.pack()

        self.exitButton = Button(frame, text="Exit", command=frame.quit)
        self.exitButton.pack(side=LEFT)

    def display(self):
        print "fuck"
        self.master.mainloop()

