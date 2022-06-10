# ==============================================
# * * Question : Simple Calculator (Gui - File)
# * * Author   : Alhasan Gamal Mahmoud
# * * Date     : 24 - 12 - 2021
# ===============================================
# * Import Every thing from tkinter
from tkinter import *
# * globally declare the expression variable

exp = ""

# * Function to Update the exp in Text Entry Box


def pres(num):
    global exp

    # * String Concatenation

    exp += str(num)

    # * Update the expresion

    equation.set(exp)

# * Evaluate the final expression


def equalpress():
    try:
        global exp

        # * Write Expression in file

        file.write(exp)

        # * using eval function to calculate expression

        total = str(eval(exp))
        equation.set(total)

        # * Write = total and make new line in file

        file.write(" = ")
        file.write(total)
        file.write("\n")

        # * add to total to expression and continuo equation

        exp = total
    except:
        equation.set(" Error ")
        file.write(" = ")
        file.write("Error!")
        file.write("\n")
        exp = ""

# * Clearing the Contents of the Calculator


def clear():
    global exp
    exp = ""
    equation.set(exp)

# * BackSpace Element of Equation


def backspace():
    global exp
    exp = exp[:-1]
    equation.set(exp)


# * Creat a GUI
if __name__ == '__main__':
    window = Tk()

    # * Crate File and Append in it

    file = open("Calculator.txt", "a")

    # * Set Background Color

    window.config(background="gray")

    # * Set Title

    window.title("Simple Calculator")

    # * Set the size of window

    window.geometry("390x340")

    equation = StringVar()

    # * Function for Creating the EntryBox for Typing the Text for Operation

    exp_field = Entry(window, textvariable=equation, font="lucida 12 bold")

    # * Using the Grid Method for Assigning the Widgets at their respective positions.

    exp_field.grid(columnspan=4, ipadx=102, ipady=32)

    # * create the Buttons and position them inside the window.

    bton1 = Button(window, text=' 1 ', font="lucida 15 bold", fg="gray",
                   bg="white", command=lambda: pres(1), height=1, width=7)
    bton1.grid(row=2, column=0)

    bton2 = Button(window, text=' 2 ', font="lucida 15 bold", fg="gray",
                   bg="white", command=lambda: pres(2), height=1, width=7)
    bton2.grid(row=2, column=1)

    bton3 = Button(window, text=' 3 ', font="lucida 15 bold", fg="gray",
                   bg="white", command=lambda: pres(3), height=1, width=7)
    bton3.grid(row=2, column=2)

    bton4 = Button(window, text=' 4 ', font="lucida 15 bold", fg="gray",
                   bg="white", command=lambda: pres(4), height=1, width=7)
    bton4.grid(row=3, column=0)

    bton5 = Button(window, text=' 5 ', font="lucida 15 bold", fg="gray",
                   bg="white", command=lambda: pres(5), height=1, width=7)
    bton5.grid(row=3, column=1)

    bton6 = Button(window, text=' 6 ', font="lucida 15 bold", fg="gray",
                   bg="white", command=lambda: pres(6), height=1, width=7)
    bton6.grid(row=3, column=2)

    bton7 = Button(window, text=' 7 ', font="lucida 15 bold", fg="gray",
                   bg="white", command=lambda: pres(7), height=1, width=7)
    bton7.grid(row=4, column=0)

    bton8 = Button(window, text=' 8 ', font="lucida 15 bold", fg="gray",
                   bg="white", command=lambda: pres(8), height=1, width=7)
    bton8.grid(row=4, column=1)

    bton9 = Button(window, text=' 9 ', font="lucida 15 bold", fg="gray",
                   bg="white", command=lambda: pres(9), height=1, width=7)
    bton9.grid(row=4, column=2)

    bton0 = Button(window, text=' 0 ', font="lucida 15 bold", fg="gray",
                   bg="white", command=lambda: pres(0), height=1, width=7)
    bton0.grid(row=5, column=0)

    bton_plus = Button(window, text=' + ', font="lucida 15 bold", fg="gray",
                       bg="white", command=lambda: pres("+"), height=1, width=7)
    bton_plus.grid(row=2, column=3)

    bton_minus = Button(window, text=' - ', font="lucida 15 bold", fg="gray",
                        bg="white", command=lambda: pres("-"), height=1, width=7)
    bton_minus.grid(row=3, column=3)

    bton_multiply = Button(window, text=' * ', font="lucida 15 bold",
                           fg="gray", bg="white", command=lambda: pres("*"), height=1, width=7)
    bton_multiply.grid(row=4, column=3)

    bton_divide = Button(window, text=' / ', font="lucida 15 bold", fg="gray",
                         bg="white", command=lambda: pres("/"), height=1, width=7)
    bton_divide.grid(row=5, column=3)

    bton_equal = Button(window, text=' = ', font="lucida 15 bold",
                        fg="gray", bg="white", command=equalpress, height=1, width=7)
    bton_equal.grid(row=6, column=1)

    bton_power = Button(window, text=' ^ ', font="lucida 15 bold", fg="gray",
                        bg="white", command=lambda: pres("**"), height=1, width=7)
    bton_power.grid(row=5, column=2)

    bton_sqr = Button(window, text=' sqr ', font="lucida 15 bold", fg="gray",
                      bg="white", command=lambda: pres("**0.5"), height=1, width=7)
    bton_sqr.grid(row=6, column=0)

    bton_moduls = Button(window, text=' % ', font="lucida 15 bold", fg="gray",
                         bg="white", command=lambda: pres("%"), height=1, width=7)
    bton_moduls.grid(row=6, column=2)

    bton_int_divid = Button(window, text=' // ', font="lucida 15 bold",
                            fg="gray", bg="white", command=lambda: pres("//"), height=1, width=7)
    bton_int_divid.grid(row=6, column=3)

    bton_decimal = Button(window, text=' . ', font="lucida 15 bold",
                          fg="gray", bg="white", command=lambda: pres("."), height=1, width=7)
    bton_decimal.grid(row=5, column=1)

    bton_clear = Button(window, text=' Clear ', font="lucida 15 bold",
                        fg="gray", bg="white", command=clear, height=1, width=7)
    bton_clear.grid(row=7, column=0)

    backspace = Button(window, text=' Del ', font="lucida 15 bold",
                       fg="gray", bg="white", command=backspace, height=1, width=7)
    backspace.grid(row=7, column=1)

    # * Start GUI

    window.mainloop()

    # * Close File

    file.close()
