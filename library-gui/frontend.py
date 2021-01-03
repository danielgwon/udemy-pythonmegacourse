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
import backend


window = Tk()

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

# Buttons
viewButton = Button(window, text="View all", width=12)
viewButton.grid(row=2, column=3)
searchButton = Button(window, text="Search Entry", width=12)
searchButton.grid(row=3, column=3)
addButton = Button(window, text="Add entry", width=12)
addButton.grid(row=4, column=3)
updateButton = Button(window, text="Update", width=12)
updateButton.grid(row=5, column=3)
deleteButton = Button(window, text="Delete", width=12)
deleteButton.grid(row=6, column=3)
closeButton = Button(window, text="Close", width=12)
closeButton.grid(row=7, column=3)


window.mainloop()