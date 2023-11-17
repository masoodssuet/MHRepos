# THIS IS A USER-BUILT MODULE CODED IN PYTHON. THE
# MODULE PROVIDES CERTAIN USER-DEFINED CONVENIENCE
# CLASSES THAT REPRESENT CUSTOM USER-DEFINED GUI
# COMPONENTS SUCH AS USER INPUT BOX, USER BUTTON,
# TAILORED LIST BOX. EACH USER-BUILT COMPONENT
# ITSELF IS BASED UPON CLASSES OF THE PYTHON
# tkinter MODULE.
import tkinter as tk
from tkinter import ttk
from tkinter import Frame
import tkinter.messagebox as mymsg
import tkinter.font as tkfont
def createLabel(parentf, wd, cap):
    # ------------VERY VERY IMPORTANT-----(SETTING TEXT ANCHOR)-----
    # THE VALUE OF THE anchor attribute MUST BE SPECIFICALLY SET
    # TO (PREFERABLY) tk.W FOR a tkinter Label OBJECT. FOR SOME
    # REASON THE TEXT WITHIN THE LABEL MIGHT BE (BY DEFAULT)
    # PRESET TO tk.E OR tk.CENTER. THIS MAY CAUSE THE TEXT WITHIN
    # THE LABEL TO INVISIBLE WITHIN THE VIEWABLE AREA OF THE LABEL.

    lbl =  tk.Label(parentf, width=wd,
            padx=0, pady=0, anchor=tk.W,
            text=cap, background="Light Gray")
    lbl.grid(row=0, column=0, sticky="W")
    return lbl
    # -------------------------------------------------------------
def putItem(vitem, vrow, vcolumn):
    vitem.grid(pad=None,
               row=vrow, column=vcolumn)
def fixWidget(wgt):
    putItem(wgt, 0, 0)
def addToFrame(f, vitem, vrow, vcol):
    if isinstance(f, myFrame):
        f.addItem(vitem, vrow, vcol)

class myFrame(Frame):
    def __init__(self, parentwindow, wd, hgt):
        super().__init__(
            parentwindow, width=wd, height=hgt)
        self.WGTS = []
        self.grid_propagate(False)
        self.grid(row=0, column=0, sticky=tk.W)
    def setRowWeights(self, rowsw):
        if rowsw == None:
            return False
        try:
            nrows = len(rowsw)
            for c in range(nrows):
                self.rowconfigure(c, rowsw[c])
                return True
        except:
            return False

    def setColumnWeights(self, colsw):
        if colsw == None:
            return False
        try:
            ncols = len(colsw)
            for c in range(ncols):
                self.columnconfigure(c, colsw[c])
            return True
        except:
            return False
    def setGridWeights(self, rowsw, colsw):
        if rowsw == None or colsw == None:
            return False
        if not self.setRowWeights(rowsw):
            return False
        if not self.setColumnWeights(colsw):
            return False
        return True


    def addItem(self, vitem, vrow, vcol):
        try:
            if vitem not in self.WGTS:
                self.WGTS.append(vitem)
                putItem(vitem, vrow, vcol)
            else:
                mymsg.showinfo("Duplicate Item",
                    "Item already exists...")
        except:
            mymsg.showinfo("Grid Positioning", "Error...")

    def addNewSubFrame(self, vrow, vcol, wd, hgt):
        f = myFrame(self, wd, hgt)
        self.addItem(f, vrow, vcol)
        return f

    def resetItems(self):
        self.WGTS = []

class myLabel(myFrame):
    def __init__(self, parentf, vrow, vcol, wd, cap):
        super().__init__(parentf, wd+5, 28)
        addToFrame(parentf, self, vrow, vcol)
        self.lblv = createLabel(self, wd, cap)
        self.addItem(self.lblv,0, 0)
    def getText(self):
            return self.lblv['text']

    def setText(self, s):
        self.lblv['text'] = s


class inpBox(myFrame):
    def __init__(self, parentf, vrow, vcol, wd, cap=""):
        # THIS FUNCTION CREATES AN INPUT BOX.
        # THE INPUT BOX IS COMPOSED OF A LABEL AND
        # AN ENTRY WIDGET FOR ENTERING DATA. Various
        # values are passed as parameters to the
        # class constructor for setting attributes for
        # for INPUT BOX. THE PARENT FRAME w IS ALSO
        # PASSED AS PARAMETER TO THIS FUNCTION.
        super().__init__(parentf, wd+5, 50)
        addToFrame(parentf, self, vrow, vcol)
        self.lblv = createLabel(self, wd, 25, cap)
        self.txtv = tk.Entry(self, width=wd)
        self.addItem(self.lblv, 0, 0)
        self.addItem(self.txtv, 1, 0)

    def getEntry(self):
        return self.txtv

    def getText(self):
        return self.txtv.get()

    def setText(self, s):
        self.txtv.delete(0, 'end')
        self.txtv.insert(tk.END, s)
    def appendText(self, s):
        self.txtv.insert(tk.END, s)
    def clearText(self):
        self.txtv.delete(0, 'end')
# END OF inpBox class

class inpBoxMulti(myFrame):
    def __init__(self, parentf, vrow, vcol, wd, ht, cap):
        # THIS FUNCTION CREATES AN INPUT BOX.
        # THE INPUT BOX IS COMPOSED OF A LABEL AND
        # AN ENTRY WIDGET FOR ENTERING DATA. Various
        # values are passed as parameters to the
        # class constructor for setting attributes for
        # for INPUT BOX. THE PARENT FRAME w IS ALSO
        # PASSED AS PARAMETER TO THIS FUNCTION.
        super().__init__(parentf, wd+5, ht+25)
        addToFrame(parentf, self, vrow, vcol)
        self.setGridWeights((
            25, (ht+25)), (1,))
        self.lblv = createLabel(self, wd, cap)
        # -------------------------------------------------------------
        self.txtv = tk.Text(self, width=wd, height=ht)
        self.addItem(self.lblv, 0, 0)
        self.addItem(self.txtv, 1, 0)



    def getEntry(self):
        return self.txtv

    def getText(self):
        # The value "1.0" for the first parameter
        # to get() indicates that the text has to be
        # obtained starting from the very first character
        # in the Multiline text box.
        return self.txtv.get("1.0", "end-1c")

    def setText(self, s):
        self.txtv.delete("1.0", tk.END)
        self.txtv.insert("1.0", s)
    def appendText(self, s):
        self.txtv.insert(tk.END, s)
    def appendLine(self, s):
        self.txtv.insert(tk.END, s + "\n")

    def clearText(self):
        self.txtv.delete("1.0", tk.END)


# END OF inpBox class

class btn(myFrame):
    def __init__(self, parentf, vrow, vcol, wd, cap, cmd):
        # THIS FUNCTION CREATES A BUTTON WHICH CAN BE
        # CLICKED TO EXECUTE SOME GIVEN FUNCTION.
        # Various values are passed as parameters to the
        # class constructor for setting attributes for
        # for BUTTON. THE PARENT FRAME w IS ALSO
        # PASSED AS PARAMETER TO THIS FUNCTION.

        super().__init__(parentf, wd, 28)
        addToFrame(parentf, self, vrow, vcol)
        self.btn = tk.Button(self,
                             text=cap, command=cmd)
        self.addItem(self.btn, 0, 0)


    def getBtn(self):
        return self.btn

class myCheckBox(myFrame):
    def __init__(self, parentf, vrow,
                 vcol, wd, cap, cmd):
        # THIS FUNCTION CREATES A CHECK BOX WHICH CAN BE
        # USED TO TURN ON OR TURN OFF THE OPTION ASSOCIATED
        # WITH THE CHECK BOX.
        # Various values are passed as parameters to the
        # class constructor for setting attributes for
        # for CHECK BOX. THE PARENT FRAME w IS ALSO
        # PASSED AS PARAMETER TO THIS FUNCTION.
        super().__init__(parentf, wd+5, 28)
        addToFrame(parentf, self, vrow, vcol)
        self.statev = tk.IntVar()
        self.chk = tk.Checkbutton(self,
            variable=self.statev, offvalue=0,
            onvalue=1, text=cap, command=cmd)
        self.addItem(self.chk, 0, 0)
        print("bbbb")


    def getCheckBox(self):
        return self.chk
    def isOn(self):
        if self.statev == 1:
            return True
        else:
            return False
    # END OF myCheckBox class

    def turnOn(self):
        self.chk.select()


    def turnOff(self):
        self.chk.deselect()

class myListBox(myFrame):
    def __init__(self, parentf, vrow, vcol,
                 wd, hgt, fcap, itemsv):
        # THIS FUNCTION CREATES A LIST BOX.
        # THE LIST BOX IS COMPOSED OF A LABEL AND
        # AN ACTUAL tkinter LIST BOX. Various values
        # are passed as parameters to the class constructor
        # for setting attributes for LIST BOX. THE PARENT
        # FRAME w IS ALSO PASSED AS PARAMETER TO THIS
        # FUNCTION.
        super().__init__(parentf, wd+5, hgt + 20)
        addToFrame(parentf, self, vrow, vcol)
        self.lbl = createLabel(self, wd, 25, fcap)
        self.var = tk.Variable(value=itemsv)
        self.lbox = tk.Listbox(self, width=wd, height=hgt,
                               listvariable=self.var,
                               selectmode=tk.MULTIPLE, state="normal")
        self.addItem(self.lbl, 0, 0)
        self.addItem(self.lbox, 1, 0)


    def getFrame(self):
        return self.f

    def getListBox(self):
        return self.lbox


# END OF myListBox class
class myCombo(myFrame):
    def __init__(self, parentf, vrow, vcol,
                 wd, fcap, itemsv):
        # THIS FUNCTION CREATES A COMBO BOX.
        # THE COMBO BOX IS COMPOSED OF A LABEL AND
        # AN ACTUAL tkinter COMBO BOX. Various values
        # are passed as parameters to the class constructor
        # for setting attributes for COMBO BOX. THE PARENT
        # FRAME w IS ALSO PASSED AS PARAMETER TO THIS
        # FUNCTION.
        super().__init__(parentf, vrow, vcol, wd+5, 50)
        addToFrame(parentf, self, vrow, vcol)
        self.lblv = createLabel(self, wd, 25, fcap)
        self.cmb = tk.ttk.Combobox(self, values=itemsv, width=wd, state="normal")

        self.addItem(self.lbl, 0, 0)
        self.addItem(self.cmb, 1, 0)

    def getCombo(self):
        return self.cmb
# END OF myCombo class