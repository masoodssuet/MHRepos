
# THIS PYTHON APP PROVIDES AN INTERFACE FOR BUILDING A
# WEB PAGE THAT WOULD CONTAIN HTML AND INLINE CSS STYLES.
# THE PAGE IS CONSTRUCTED WITH FOUR ELEMENTS EACH OF WHICH
# IS STORED IN A FILE.
# FIRST, THE USER MUST ENTER THE FOR OR SELECT A BASE DIRECTORY
# THAT WOULD BE THE ROOT FOR ALL FILES FROM WHICH INFORMATION IS
# TO BE READ. FOR EXAMPLE, THE DIRECTORY MAY BE C:\HTMLBuilder.
# THEN THE USER MUST ENTER THE PATH FOR OR SELECT A FOLDER
# WITHIN THE BASE DIRECTORY IN WHICH THE FILES HAVING FIXED
# NAMES WOULD BE DIRECTLY LOCATED. FOR EXAMPLE, THE DIRECTORY
# MAY BE C:\HTMLBuilder\builda. THE FIXED NAMES OF THE FILES
# MUST BE "top.html", "head.html", and "body.html". EACH FILE
# WOULD CONTAIN THE TEXT OF THE RESPECTIVE PART OF THE PAGE
# TO BE CONSTRUCTED.
# THE USER MUST ALSO ENTER THE PATH FOR OR SELECT A FILE WHICH
# WOULD CONTAIN THE CSS STYLES TO BE APPLIED TO THE PAGE. THAT
# FILE MUST BE SOMEWHERE IN THE BASE DIRECTORY OR INSIDE ITS
# SUBDIRECTORIES STRUCTURE.
# THIS APP WOULD COMBINE THE ELEMENTS AND CONSTRUCT AN OUTPUT
# TEXT FILE CONTAINING THE WHOLE HTML CODE ALONG WITH THE CSS
# STYLES. THE NAME (ONLY THE NAME) OF THE OUTPUT FILE MUST BE
# PROVIDED BY THE USER.
# ---------------VERY IMPORTANT---------------
# THE <head> AND </head> TAGS MUST BE OMITTED FROM THE CONTENT
# OF THE FIXED NAME FILE head.html.
# ALSO, THE <body> AND </body> TAGS AND THE TERMINATING </html>
# TAG MUST BE OMITTED FROM THE CONTENT OF THE FIXED NAME FILE
# body.html.
# THESE TAGS ARE ADDED TO BY THIS APP WHEN BUILDING THE PAGE.
# ---------------------------------------------------------------
import pkgMHGUI.GUIWindowCommon as pyw
import pkgMHGUI.GUICommon as myg
import pkgPageBuild.pageBuildUtils as mdbuild
import tkinter as tk
from tkinter import Frame
import subprocess
import os
# --------------------------------------------------
# myShow CLASS DEFINITION. CLASS INHERITS Frame
class myShow(myg.myFrame):
    def __init__(self, win):
        super().__init__(win, 650, 450)
        self.topFrame = myg.myFrame(win, 600, 400)
        myg.putItem(self.topFrame, 0, 0)
        self.topFrame.setGridWeights(
            (15, 18, 11, 20, 11, 11, 11, 11), (1,))
        vwd = 400
        vht1 = 40
        vht2 = 25
        self.framea = self.topFrame.addNewSubFrame(
            0, 0, vwd, 35)
        self.framea.setGridWeights((1,), (1, 1))
        vwd = 140
        vcap = "Select..."
        self.btnbase = myg.btn(self.framea,
                0, 0, vwd,
                vcap, self.selectBaseDir)
        vwd = 140
        vcap = "Build Page"
        self.btnapply = myg.btn(self.framea,
                               0, 1, vwd,
                               vcap, self.applyPageBuild)
        vwd = 450
        vcap = "Enter Base Path for root where items are stored"
        self.inpbasepath = myg.inpBoxMulti(
                self.topFrame, 1,
                        0, vwd, vht2, vcap)
        vwd = 250
        vcap = "Enter name of output html file in content Dir"
        self.inpoutfile = myg.inpBoxMulti(
            self.topFrame, 2,
            0, vwd, vht2, vcap)
        # --------------------------------------------------------
        vwd = 500
        vcap = "PRESET: TOP Code in top.html HEAD Code in head.html"
        self.lblinfo = myg.myLabel(
            self.topFrame, 3, 0, vwd, vcap)

        vwd = 250
        vcap = "Select..."
        self.btncssfile = myg.btn(self.topFrame,
            4,0, vwd, vcap, self.selectCSSFile)
        vwd = 450
        vcap = "Enter path of CSS File within Base Dir"
        self.inpcssfile = myg.inpBoxMulti(
            self.topFrame, 5,
            0, vwd, vht2, vcap)
        vwd = 250
        vcap = "Select..."
        self.btncontentdir = myg.btn(self.topFrame,
                    6, 0, vwd, vcap,
                            self.selectContentDir)
        vwd = 450
        vcap = "Select Content Dir within Base Dir"
        self.inpcontentdir = myg.inpBoxMulti(
            self.topFrame, 7,
            0, vwd, vht2, vcap)

    # ---------------------------------------------
    def doPass(self):
        pass
    def selectBaseDir(self):
        initdir = "C:/"
        cap = "Select Base Directory"
        bp = ""
        vbasedir = mdbuild.selectDir(bp, cap)
        if vbasedir != None:
            self.inpbasepath.setText(vbasedir)

    def selectCSSFile(self):
        initdir = "C:/"
        cap = "Select CSS File"
        bp = self.inpbasepath.getText()
        vfile = mdbuild.selectFile(bp, cap)
        if vfile != None:
            self.inpcssfile.setText(vfile)

    def selectContentDir(self):
        initdir = "C:/"
        cap = "Select Content Directory"
        bp = self.inpbasepath.getText()
        vdir = mdbuild.selectDir(bp, cap)
        if vdir != None:
            self.inpcontentdir.setText(vdir)

    def applyPageBuild(self):

        spath = os.getcwd()
        print(spath)
        print("Web Page Builder Interface...")

        try:
            bp = os.path.abspath(self.inpbasepath.getText())
            contentpath = mdbuild.completePath(
                bp, self.inpcontentdir.getText())
            topfile = os.path.join(contentpath, "top.html")
            headfile = os.path.join(contentpath, "head.html")
            bodyfile = os.path.join(contentpath, "body.html")
            cssfile = mdbuild.completePath(
                bp, self.inpcssfile.getText())
            outfile = os.path.join(
                contentpath, self.inpoutfile.getText())
            print("Base Path: ", bp)
            print("Content Path: ", contentpath)
            print("CSS File: ", cssfile)
            with (open(outfile, mode="w") as outf):
                with open(topfile, mode="r") as topf:
                    topstr = str(topf.read())
                with open(headfile, mode="r") as headf:
                    headstr = str(headf.read())
                with open(bodyfile, mode="r") as bodyf:
                    bodystr = str(bodyf.read())
                with open(cssfile, mode="r") as cssf:
                    cssstr = str(cssf.read())
                    cssstr = mdbuild.removeCSSComments(cssstr)
                fullstr = topstr + "\n"
                fullstr += "<head>\n" + headstr + "\n"
                fullstr += "<style>\n" + cssstr + "\n"
                fullstr += "</style>\n" + "</head>\n"
                fullstr += "<body>\n" + bodystr + "\n</body>\n</html>\n"
                outf.write (fullstr)
        except Exception as e:
            print("ERROR: ", str(e))

        


# END OF CLASS
# ----------------------------------------------
def doApp():
    # CREATE THE GUI WINDOW
    w = tk.Tk()
    w.title("<Web Page Builder Interface>")
    w.geometry("800x550+10+10")
    pyw.wToFront(w)
    w.grid_propagate(False)
    shw = myShow(w)
    w.mainloop()
