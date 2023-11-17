def wToFront(w):
    w.geometry("400x300+10+10")
    # ============VERY VERY IMPORTANT===========================
    # The following statements cause the tkinter Window w displayed
    # by GUI CODE TO be PLACED AT THE FRONT OF ALL OTHER WINDOWS
    # (INCLUDING ANY IDE Window).
    w.lift()
    w.attributes("-topmost", True)
    # -----------------------------------------------------------
    # If the following statement is OMITTED, the tkinter window shown
    # by this code would PERMANENTLY remain at the FRONT of
    # ALL OTHER WINDOWS. However, the following statement permits
    # another window to subsequently come to front if the user
    # clicks on that window.
    w.after_idle(w.attributes, '-topmost', False)
    # ======================= END =======================================
