from tkinter import *
from tkinter.ttk import *

class MyFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master = master
        self.master.title = "My Frame"
        self.pack(fill=BOTH, expand=True)

def main():
    root = Tk()
    root.geometry("600x550+100+100")
    app = MyFrame(root)
    root.mainloop()

if __name__ == "__main__":
    main()