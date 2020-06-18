from tkinter import *
from backend import Database

database = Database()

class Window:
    
    def __init__(self, window):
        self.window = window

        self.window.wm_title('Bookstore')

        #labels
        self.tl = Label(self.window, text = 'Title')
        self.tl.grid(row = 0, column = 0)

        self.yl = Label(self.window, text = 'Year')
        self.yl.grid(row = 1, column = 0)

        self.al= Label(self.window, text = 'Author')
        self.al.grid(row = 0, column = 2)

        self.il = Label(self.window, text = 'ISBN')
        self.il.grid(row = 1, column = 2)

        #entries
        self.tval = StringVar()
        self.te= Entry(self.window, textvariable = self.tval)
        self.te.grid(row = 0, column = 1)

        self.yval = StringVar()
        self.ye = Entry(self.window, textvariable = self.yval)
        self.ye.grid(row = 1, column = 1)

        self.aval = StringVar()
        self.ae = Entry(self.window, textvariable = self.aval)
        self.ae.grid(row = 0, column = 3)

        self.ival = StringVar()
        self.ie = Entry(self.window, textvariable = self.ival)
        self.ie.grid(row = 1, column = 3)

        #buttons
        view = Button(self.window, text = 'View All', width = 12, command = self.view_command)
        view.grid(row = 2, column = 3)

        search = Button(self.window, text = 'Search Entry', width = 12, command = self.search_command)
        search.grid(row = 3, column = 3)

        add = Button(self.window, text = 'Add Entry', width = 12, command = self.add_command)
        add.grid(row = 4, column = 3)

        update = Button(self.window, text = 'Update Selected', width = 12, command = self.update_command)
        update.grid(row = 5, column = 3)

        delete = Button(self.window, text = 'Delete Selected', width = 12, command = self.delete_command)
        delete.grid(row = 6, column = 3)

        close = Button(self.window, text = 'Close', width = 12, command = self.window.destroy)
        close.grid(row = 7, column = 3)

        #listbox, scrollbar
        self.lb = Listbox(self.window, height = 6, width = 36)
        self.lb.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

        self.sb = Scrollbar(self.window)
        self.sb.grid(row = 2, column = 2, rowspan = 6)

        self.lb.configure(yscrollcommand = self.sb.set)
        self.sb.configure(command = self.lb.yview)

        self.lb.bind('<<ListboxSelect>>', self.get_selected_row)

    #functions
    def refresh(self):
        self.lb.delete(0, END)
        self.view_command()

    def get_selected_row(self, event): 
        try:    
            index = self.lb.curselection()[0]
            self.selected = self.lb.get(index)
            self.te.delete(0, END)
            self.te.insert(END,  self.selected[1])
            self.ae.delete(0, END)
            self.ae.insert(END,  self.selected[2])
            self.ye.delete(0, END)
            self.ye.insert(END,  self.selected[3])
            self.ie.delete(0, END)
            self.ie.insert(END,  self.selected[4])
        except:
            self.te.delete(0, END)
            self.te.delete(0, END)
            self.te.delete(0, END)
            self.te.delete(0, END)

    def view_command(self):
        self.lb.delete(0, END)
        for row in database.view():
            self.lb.insert(END, row)
            
    def search_command(self):
        self.lb.delete(0, END)
        for row in database.search(self.tval.get(), self.aval.get(), self.yval.get(), self.ival.get()):
            self.lb.insert(END, row)

    def add_command(self):
        database.add(self.tval.get(), self.aval.get(), self.yval.get(), self.ival.get()) 
        self.lb.insert(END, (self.tval.get(), self.aval.get(), self.yval.get(), self.ival.get()))
        self.refresh()

    def update_command(self):
        database.update( self.selected[0], self.tval.get(), self.aval.get(), self.yval.get(), self.ival.get())
        self.refresh()
        
    def delete_command(self):
        database.delete( self.selected[0])
        self.lb.delete(0, END)
        self.te.delete(0, END)
        self.ye.delete(0, END)
        self.ae.delete(0, END)
        self.ie.delete(0, END)
        self.view_command()

#instantiate and initialize window
window = Tk()
Window(window)

#run window
window.mainloop()