import tkinter as tk

# globally declare the calculation variable
text_field = ""
# function to update calculation in the text entry box
def add_to_textfeild(symbol):
    # point out the global calculation variable
    global text_field
    # concatenation of string
    text_field += str(symbol)
    Field.delete(1.0, "end")
    Field.insert(1.0, text_field)
    # Function to evaluate the final expression


# noinspection PyBroadException
def evaluate_calculation():
    # Try and except statement is used for handling the errors like zero division error .Put that code inside the try block which may generate the error
    global text_field
    try:
        # eval function evaluate the calculation
        # and str function convert the result
        # into string
        result = str(eval(text_field))
        # initialize the calculation variable
        # by empty string
        text_field = ""
        Field.delete(1.0, "end")
        Field.insert(1.0, result)
        # When the error is generated then handle by the except block
    except:
        clear_field()
        Field.insert(1.0, "Syntax Error")
        # Function to clear the contents of text entry box
def clear_field():
    global text_field
    text_field = ""
    Field.delete(1.0, "end")
# Create GUI window
window = tk.Tk()


# Set configuration for the GUI window
window.geometry("720x720")
# Set title for the GUI window
window.title("Nansera_Ena_simpleCalculator")
# Set background color
window.configure(background="white")

Field = tk.Text(window, height=2, width=50, font=("Times New Roman", 25))
Field.grid(columnspan=90)

# create Buttons and place them at a particular location inside the window. when user press the button, the function affiliated to that button is executed .
button1 = tk.Button(window, text="1", command=lambda: add_to_textfeild(1),
                 width=20, font=("Times New Roman", 14), fg='white', bg='orange')
button1.grid(row=2, column=1)
button2 = tk.Button(window, text="2", command=lambda: add_to_textfeild(2),
                 width=20, font=("Times New Roman", 14), fg='white', bg='orange')
button2.grid(row=2, column=2)
button3 = tk.Button(window, text="3", command=lambda: add_to_textfeild(3),
                 width=20, font=("Times New Roman", 14), fg='white', bg='orange')
button3.grid(row=2, column=3)
button4 = tk.Button(window, text="4", command=lambda: add_to_textfeild(4),
                 width=20, font=("Times New Roman", 14), fg='white', bg='orange')
button4.grid(row=3, column=1)
button5 = tk.Button(window, text="5", command=lambda: add_to_textfeild(5),
                 width=20, font=("Times New Roman", 14), fg='white', bg='orange')
button5.grid(row=3, column=2)
button6 = tk.Button(window, text="6", command=lambda: add_to_textfeild(6),
                 width=20, font=("Times New Roman", 14), fg='white', bg='orange')
button6.grid(row=3, column=3)
button7 = tk.Button(window, text="7", command=lambda: add_to_textfeild(7),
                 width=20, font=("Times New Roman", 14), fg='white', bg='orange')
button7.grid(row=4, column=1)
button8 = tk.Button(window, text="8", command=lambda: add_to_textfeild(8),
                 width=20, font=("Times New Roman", 14), fg='white', bg='orange')
button8.grid(row=4, column=2)
button9 = tk.Button(window, text="9", command=lambda: add_to_textfeild(9),
                 width=20, font=("Times New Roman", 14), fg='white',
                 bg='orange')
button9.grid(row=4, column=3)
button0 = tk.Button(window, text="0", command=lambda: add_to_textfeild(0),
                 width=20, font=("Times New Roman", 14), fg='white', bg='orange')
button0.grid(row=5, column=2)
btn_ob = tk.Button(window, text="(", command=lambda: add_to_textfeild("("),
                   width=20, font=("Times New Roman", 14), fg='white', bg='orange')
btn_ob.grid(row=5, column=1)
btn_oc = tk.Button(window, text=")", command=lambda: add_to_textfeild(")"),
                   width=20, font=("Times New Roman", 14), fg='white', bg='orange')
btn_oc.grid(row=5, column=3)
button_times = tk.Button(window, text="*", command=lambda: add_to_textfeild("*"),
                      width=20, font=("Times New Roman", 14), fg='white', bg='blue')
button_times.grid(row=3, column=4)
button_plus = tk.Button(window, text="+", command=lambda: add_to_textfeild("+"),
                     width=20, font=("Times New Roman", 14), fg='white', bg='blue')
button_plus.grid(row=4, column=4)
button_minus = tk.Button(window, text="-", command=lambda: add_to_textfeild("-"),
                      width=20, font=("Times New Roman", 14), fg='white', bg='blue')
button_minus.grid(row=5, column=4)
button_divide = tk.Button(window, text="/", command=lambda: add_to_textfeild("/"),
                       width=20, font=("Times New Roman", 14), fg='white', bg='blue')
button_divide.grid(row=6, column=4)
button_clear = tk.Button(window, text="AC", command=clear_field,
                   width=20, font=("Times New Roman", 14), fg='white', bg='green')
button_clear.grid(row=2, column=4)
button_equals = tk.Button(window, text="=", command=evaluate_calculation,
                       width=20, font=("Times New Roman", 14), fg='white', bg='orange')
button_equals.grid(row=6, column=3)
btn_dec = tk.Button(window, text=".", command=lambda: add_to_textfeild("."),
                    width=20, font=("Times New Roman", 14), fg='white', bg='orange')
btn_dec.grid(row=6, column=1)
button_zero = tk.Button(window, text="00", command=lambda: add_to_textfeild("00"),
                     width=20, font=("Times New Roman", 14), fg='white', bg='orange')
button_zero.grid(row=6, column=2)
# Start the GUI
window.mainloop()


