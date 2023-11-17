import tkinter as tk
from tkinter import filedialog
import os

def isComment(s, p):
    if s == None:
        return False
    elif p > len(s) - 3:
        return False
    elif s[p:p+2] == "/*":
        return True
    else:
        return False


def CSSSkipCodeSec(csstext, p):
    if csstext == None:
        return None
    tl = len(csstext)
    if p > tl-1 or p < 0:
        return None
    p1 = p
    endcode = False
    for k in range(p,tl-1):
        p1 = k
        if csstext[k:k+2] == "/*":
            endcode = True
            break
        elif csstext[k:k+2] == "*/":
            return None
    if not endcode:
        return tl
    else:
        return p1


def CSSSkipComment(csstext, p):
    if csstext == None:
        return None
    tl = len(csstext)
    if p > tl-1 or p < 0:
        return None
    if p > tl-5:
        return None
    if csstext[p:p+2] != "/*":
        return None
    p1 = p
    endcooment = False
    for k in range(p+2, tl - 1):
        p1 = k
        if csstext[k:k + 2] == "*/":
            endcooment = True
            break
        elif csstext[k:k + 2] == "\*":
            return None
    if not endcooment:
        return None
    else:
        return p1 + 2


def removeCSSComments(csstext):
    if csstext == None:
        return csstext
    fullstr = ""
    donev = False
    tl = len(csstext)
    p = 0
    p1 = 0
    while not donev:
        p1 = CSSSkipCodeSec(csstext, p)
        if p1 == None:
            donev = True
            break
        elif p1 == p:
            pass
        else:
            fullstr += csstext[p:p1]
        if p1 >= tl-1:
            break

        p = p1
        p2 = p1
        while isComment(csstext, p):
            p2 = CSSSkipComment(csstext, p)
            if p2 == None:
                donev = True
                break
            elif p2 == p:
                donv = True
                break
            if p2 >= tl-1:
                donv = True
                break
            p = p2


    return fullstr

def completePath(basedir, path):
    # IF POSSIBLE, MAP A CANDIDATE PARAMETER CONTAINING
    # A POSSIBLE PATH ONTO A MORE COMPLETE PATH
    # BASED On THE VALUE OF BASE DIRECTORY PATH PASSED
    # AS THE FIRST PARAMETER.
    if os.path.isabs(path):
        return path
    elif basedir.isspace():
        return path
    else:
        return os.path.join(basedir, path)

def effectivePath(basedir, pathloc):
    # CONSTRUCT THE EFFECTIVE PATH FROM A RAW
    # PATH (NORMALLY GIVEN AS RAW PARAMETER).
    # THE CONSTRUCTION WOULD BE BASED ON THE
    # BASE DIRECTORY.

    ploc = os.path.abspath(pathloc)
    bdirreal = os.path.abspath(basedir)
    ploc = os.path.normpath(ploc)
    bdirreal = os.path.normpath(bdirreal)
    if ploc.startswith(bdirreal):
        return ploc[len(bdirreal) + 1:]
    else:
        return None


def constructParamStr(prmlist):
    s = ""
    for pr in prmlist:
        s += setPr(pr)
    return s

def selectBaseDir(basedir, cap):
    # SELECT THE BASE DIR THROUGH A DIALOG

    initdir = "C:/"
    bdir = None
    if basedir.isspace():
        bdir = tk.filedialog.askdirectory()
    elif not os.path.isdir(basedir):
        bdir = tk.filedialog.askdirectory()
    else:
        bdir = tk.filedialog.askdirectory()
    if bdir == None:
        pass
    elif bdir.isspace():
        bdir = None
    return bdir


def selectDir(basedir, cap):
    # SELECT A DIRECTORY THROUGH A DIALOG

    selectdir = None
    if basedir.isspace():
        selectdir = tk.filedialog.askdirectory()
    elif not os.path.isdir(basedir):
        selectdir = tk.filedialog.askdirectory()
    else:
        selectdir = tk.filedialog.askdirectory()
        if selectdir != None:
            selectdir = effectivePath(basedir, selectdir)
    if selectdir == None:
        pass
    elif selectdir.isspace():
        selectdir = None
    return selectdir


def selectFile(basedir, cap):
    # SELECT A FILE THROUGH A DIALOG
    selectfile = None
    print("BASE DIR: ", basedir)
    if basedir.isspace():
        selectfile = tk.filedialog.askopenfilename()
    elif not os.path.isdir(basedir):
        selectfile = tk.filedialog.askopenfilename()
    else:
        selectfile = tk.filedialog.askopenfilename()
        if selectfile != None:
            selectfile = effectivePath(basedir, selectfile)
    if selectfile == None:
        pass
    elif selectfile.isspace():
        selectfile = None
    else:
        print("SELECTED FILE: ", selectfile)
    return selectfile

