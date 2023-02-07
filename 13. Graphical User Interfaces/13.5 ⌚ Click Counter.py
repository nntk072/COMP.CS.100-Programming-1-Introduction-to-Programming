"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 0123456
Name:       Xxxx Yyyyyy
Email:      xxxx.yyyyyy@tuni.fi

Code template for counter program.
"""

from tkinter import *


class Counter:
    def __init__(self):
        # TODO: You have to creater one label and four buttons and store
        #       them in the following attributes:
        self.__main_window = Tk()
        self.__a = 0
        self.__current_value_label = Label(self.__main_window, text=f"{self.__a}", padx=0, pady=0)
        self.__current_value_label.pack(expand=True, fill=BOTH)
        self.__current_value_label.grid(row=0, column=0, columnspan=4)
        # Label displaying the current value of the counter.

        self.__reset_button = Button(self.__main_window, text="Reset", command=self.reset)
        self.__reset_button.grid(row=1, column=0)
        # Button which resets counter to zero.
        self.__increase_button = Button(self.__main_window, text="Increase", command=self.increase)
        self.__increase_button.grid(row=1, column=1)
        # Button which increases the value of the counter by one.
        self.__decrease_button = Button(self.__main_window, text="Decrease", command=self.decrease)
        self.__decrease_button.grid(row=1, column=2)
        # Button which decreases the value of the counter by one.
        self.__quit_button = Button(self.__main_window, text="Quit", command=self.quit)
        self.__quit_button.grid(row=1, column=3)
        # Button which quits the program.

        self.__main_window.mainloop()

        #     Make sure you name the components exactly as shown above,
        #    otherwise the automated tests will fail.

        # TODO: Implement the rest of the needed methods here.

    def reset(self):
        self.__a = 0
        self.__current_value_label.config(text=f"{self.__a}")

    def increase(self):
        self.__a += 1
        self.__current_value_label.config(text=f"{self.__a}")

    def decrease(self):
        self.__a -= 1
        self.__current_value_label.config(text=f"{self.__a}")

    def quit(self):
        self.__main_window.destroy()


def main():
    Counter()


if __name__ == "__main__":
    main()
