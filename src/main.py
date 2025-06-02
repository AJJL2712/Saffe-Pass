#Archivo principal donde estará el código principal
from tkinter import Tk
from gui import PasswordManagerGUI

if __name__ == "__main__":
    root = Tk()
    app = PasswordManagerGUI(root)
    root.mainloop()
