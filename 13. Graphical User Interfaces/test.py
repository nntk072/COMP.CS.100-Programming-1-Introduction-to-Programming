from tkinter import *


class GUI:
    def __init__(self):
        self.__main_window = Tk()

        self.__labelA = Label(self.__main_window, text="A", borderwidth=2, relief=GROOVE)
        self.__labelA.grid(row=1, column=1)

        self.__labelB = Label(self.__main_window, text="B", borderwidth=2, relief=GROOVE)
        self.__labelB.grid(row=1, column=2, sticky=E)

        self.__high_label = Label(self.__main_window, text="high", borderwidth=2, relief=GROOVE)
        self.__high_label.grid(row=0, column=0, rowspan=3, sticky=N + S)

        self.__wide_label = Label(self.__main_window, text="wide", borderwidth=2, relief=GROOVE)
        self.__wide_label.grid(row=0, column=1, columnspan=2, sticky=E + W)

        self.__quit_button = Button(self.__main_window, text="Quit", command=self.quit)
        self.__quit_button.grid(row=2, column=2)

        self.__main_window.mainloop()

    def quit(self):
        self.__main_window.destroy()


def main():
    gui = GUI()


if __name__ == "__main__":
    main()
