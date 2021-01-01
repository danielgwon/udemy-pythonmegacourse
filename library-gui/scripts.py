from tkinter import *


window=Tk()


# ---------------------------------------- FUNCTIONS --------------------------------------
def convertKg():

    # get the value and make the conversion
    kg = float(kgValue.get())
    g = kgToGrams(kg)
    lb = kgToLb(kg)
    oz = kgToOz(kg)

    # update text fields
    gramsText.insert('0.0', g)
    lbText.insert('0.0', lb)
    ozText.insert('0.0', oz)

def kgToGrams(kg):
    print("converting kg to g")
    return kg * 1000

def kgToLb(kg):
    print("converting kg to lbs")
    return kg * 2.20462

def kgToOz(kg):
    print("converting kg to ounces")
    return kg * 35.274


# ---------------------------------------- ROW ONE --------------------------------------
kgHeader = Label(window, text="kg")
kgHeader.grid(row=0, column=0)

kgValue = StringVar()
kgInput = Entry(window, textvariable=kgValue)
kgInput.grid(row=0, column=1)

convert = Button(window, text="Convert", command=convertKg)
convert.grid(row=0, column=2)

# ---------------------------------------- ROW TWO --------------------------------------
gramsText = Text(window, height=1, width=20)
gramsText.grid(row=1, column=0)

lbText = Text(window, height=1, width=20)
lbText.grid(row=1, column=1)

ozText = Text(window, height=1, width=20)
ozText.grid(row=1, column=2)


# b1 = Button(window, text="Execute", command=kmToMiles)
# b1.grid(row=0, column=0)

# e1Value = StringVar()
# e1 = Entry(window, textvariable=e1Value)
# e1.grid(row=0, column=1)

# t1 = Text(window, height=1, width=20)
# t1.grid(row=0, column=2)

# t1.insert(END, miles)


window.mainloop()