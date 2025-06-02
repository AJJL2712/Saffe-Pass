from src.gui import PasswordManagerGUI
import ttkbootstrap as tb

if __name__ == "__main__":
    app = PasswordManagerGUI(tb.Window(themename="flatly"))
    app.root.mainloop()
