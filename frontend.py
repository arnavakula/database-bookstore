from tkinter import *
from backend import Database

database = Database()

window = Tk()
window.wm_title('Bookstore')

#functions
def refresh():
    lb.delete(0, END)
    view_command()

def get_selected_row(event): 
    try:    
        index = lb.curselection()[0]
        global selected
        selected = lb.get(index)
        te.delete(0, END)
        te.insert(END, selected[1])
        ae.delete(0, END)
        ae.insert(END, selected[2])
        ye.delete(0, END)
        ye.insert(END, selected[3])
        ie.delete(0, END)
        ie.insert(END, selected[4])
    except:
        print('Sorry, you cannot select a book from an empty list. Please select a valid book.\n')

def view_command():
    lb.delete(0, END)
    for row in database.view():
        lb.insert(END, row)
        
def search_command():
    lb.delete(0, END)
    for row in database.search(tval.get(), aval.get(), yval.get(), ival.get()):
        lb.insert(END, row)

def add_command():
    database.add(tval.get(), aval.get(), yval.get(), ival.get()) 
    lb.insert(END, (tval.get(), aval.get(), yval.get(), ival.get()))
    refresh()

def update_command():
    database.update(selected[0], tval.get(), aval.get(), yval.get(), ival.get())
    refresh()
    
def delete_command():
    database.delete(selected[0])
    lb.delete(0, END)
    te.delete(0, END)
    ye.delete(0, END)
    ae.delete(0, END)
    ie.delete(0, END)
    view_command()

#labels
tl = Label(window, text = 'Title')
tl.grid(row = 0, column = 0)

yl = Label(window, text = 'Year')
yl.grid(row = 1, column = 0)

al = Label(window, text = 'Author')
al.grid(row = 0, column = 2)

il = Label(window, text = 'ISBN')
il.grid(row = 1, column = 2)

#entries
tval = StringVar()
te = Entry(window, textvariable = tval)
te.grid(row = 0, column = 1)

yval = StringVar()
ye = Entry(window, textvariable = yval)
ye.grid(row = 1, column = 1)

aval = StringVar()
ae = Entry(window, textvariable = aval)
ae.grid(row = 0, column = 3)

ival = StringVar()
ie = Entry(window, textvariable = ival)
ie.grid(row = 1, column = 3)

#buttons
view = Button(window, text = 'View All', width = 12, command = view_command)
view.grid(row = 2, column = 3)

search = Button(window, text = 'Search Entry', width = 12, command = search_command)
search.grid(row = 3, column = 3)

add = Button(window, text = 'Add Entry', width = 12, command = add_command)
add.grid(row = 4, column = 3)

update = Button(window, text = 'Update Selected', width = 12, command = update_command)
update.grid(row = 5, column = 3)

delete = Button(window, text = 'Delete Selected', width = 12, command = delete_command)
delete.grid(row = 6, column = 3)

close = Button(window, text = 'Close', width = 12, command = window.destroy)
close.grid(row = 7, column = 3)

#listbox, scrollbar
lb = Listbox(window, height = 6, width = 36)
lb.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

sb = Scrollbar(window)
sb.grid(row = 2, column = 2, rowspan = 6)

lb.configure(yscrollcommand = sb.set)
sb.configure(command = lb.yview)

lb.bind('<<ListboxSelect>>', get_selected_row)

#app runner
window.mainloop()