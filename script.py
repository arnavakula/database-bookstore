from tkinter import *

window = Tk()

#functions
def testing():
    print('Command working')

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
view = Button(window, text = 'View All')
view.grid(row = 2, column = 3)

search = Button(window, text = 'Search Entry')
search.grid(row = 3, column = 3)

add = Button(window, text = 'Add Entry')
add.grid(row = 4, column = 3)

update = Button(window, text = 'Update Selected')
update.grid(row = 5, column = 3)

delete = Button(window, text = 'Delete Selected')
delete.grid(row = 6, column = 3)

close = Button(window, text = 'Close')
close.grid(row = 7, column = 3)

#listbox
lb = Listbox(window, height = 6, width = 36)
lb.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

sb = Scrollbar(window)
sb.grid(row = 2, column = 2, rowspan = 6)

lb.configure(yscrollcommand = sb.set)
sb.configure(command = lb.yview)

window.mainloop()