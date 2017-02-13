from Tkinter import *


class GUI:

    def __init__(self, master):

        self.master = master

        master.title("Rock Scissor Paper Tournament")

        frame = Frame(self.master)
        frame.config(height=300, width=400)
        frame.config(relief=RAISED)
        Button(frame, text='I am a button').grid()
        LabelFrame(height=300, width=400,text='I am a LabelFrame').pack()
        frame.pack()


        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

    def display(self):
        self.master.mainloop()

