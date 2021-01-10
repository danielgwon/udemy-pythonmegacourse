"""
A program that stores the following book information:
Title, Author
Year, ISBN

User can:
View all records
Search for an entry
Add an entry
Update an entry
Delete
Close
"""

from tkinter import *
from backend import Database


database = Database("books.db")


def getSelectedRow(event):
    global selectedTuple

    try:
        index = output.curselection()[0]
        selectedTuple = output.get(index)

        # output in input fields
        titleInput.delete(0, END)
        titleInput.insert(END, selectedTuple[1])
        authorInput.delete(0, END)
        authorInput.insert(END, selectedTuple[2])
        yearInput.delete(0, END)
        yearInput.insert(END, selectedTuple[3])
        ISBNInput.delete(0, END)
        ISBNInput.insert(END, selectedTuple[4])
    except IndexError:
        print("Nothing selected!")
        pass




def viewCommand():

    # clear prior displayed data
    output.delete(0, END)

    # fetch and output new data
    rows = database.view()
    for row in rows:
        output.insert(END, row)


def searchCommand():
    output.delete(0, END)
    rows = database.search(titleText.get(), authorText.get(), yearText.get(), ISBNText.get())
    for row in rows:
        output.insert(END, row)


def addCommand():
    database.insert(titleText.get(), authorText.get(), yearText.get(), ISBNText.get())
    output.delete(0, END)
    output.insert(END, (titleText.get(), authorText.get(), yearText.get(), ISBNText.get()))


def updateCommand():
    database.update(selectedTuple[0], titleText.get(), authorText.get(), yearText.get(), ISBNText.get())


def deleteCommand():
    database.delete(selectedTuple[0])


window = Tk()

window.wm_title("Bookstore")

# Labels
titleLabel = Label(window, text="Title")
titleLabel.grid(row=0, column=0)
authorLabel = Label(window, text="Author")
authorLabel.grid(row=0, column=2)
yearLabel = Label(window, text="Year")
yearLabel.grid(row=1, column=0)
ISBNLabel = Label(window, text="ISBN")
ISBNLabel.grid(row=1, column=2)

# Inputs
titleText = StringVar()
titleInput = Entry(window, textvariable=titleText)
titleInput.grid(row=0, column=1)
authorText = StringVar()
authorInput = Entry(window, textvariable=authorText)
authorInput.grid(row=0, column=3)
yearText = StringVar()
yearInput = Entry(window, textvariable=yearText)
yearInput.grid(row=1, column=1)
ISBNText = StringVar()
ISBNInput = Entry(window, textvariable=ISBNText)
ISBNInput.grid(row=1, column=3)

# Output
output = Listbox(window, height=6, width=35)
output.grid(row=2, column=0, rowspan=6, columnspan=2)
scrollBar = Scrollbar(window)
scrollBar.grid(row=3, column=2, rowspan=6)
output.configure(yscrollcommand=scrollBar.set)
scrollBar.configure(command=output.yview)
output.bind('<<ListboxSelect>>', getSelectedRow)

# Buttons
viewButton = Button(window, text="View all", width=12, command=viewCommand)
viewButton.grid(row=2, column=3)
searchButton = Button(window, text="Search Entry", width=12, command=searchCommand)
searchButton.grid(row=3, column=3)
addButton = Button(window, text="Add entry", width=12, command=addCommand)
addButton.grid(row=4, column=3)
updateButton = Button(window, text="Update", width=12, command=updateCommand)
updateButton.grid(row=5, column=3)
deleteButton = Button(window, text="Delete", width=12, command=deleteCommand)
deleteButton.grid(row=6, column=3)
closeButton = Button(window, text="Close", width=12, command=window.destroy)
closeButton.grid(row=7, column=3)


window.mainloop()