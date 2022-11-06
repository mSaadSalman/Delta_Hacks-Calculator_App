from tkinter import *

expression = ''
result = ''


# Converts the numbers inputted by the user into an expression
def calculation(value):
    global expression
    expression += str(value)
    entry_field.configure(text=expression, anchor='nw')


# Calculates the expression inputted by user
def calculate():
    global expression
    global result
    try:
        result = str(round(eval(expression), 2))
        answer_field.configure(text=result, anchor='se')
        expression = result
    except:
        clear_everything()
        entry_field.configure(text="Error")


# Deletes expression and clears field
def clear_everything():
    global expression
    global result
    expression = ''
    entry_field.configure(text='')
    answer_field.configure(text='')


# Recalls previous answer
def previous_answer():
    global result
    global expression
    expression = result
    entry_field.configure(text='')
    entry_field.configure(text=expression)


# Changes theme of calculator
def theme(mode):
    if mode == "light":
        root.config(bg="white")
        output_frame.config(bg="white")
        entry_field.config(bg="white")
        answer_field.config(bg="white")
        for i in buttons:
            i.configure(bg="white", fg="black")

    else:
        root.config(bg="black")
        output_frame.config(bg="gray")
        entry_field.config(bg="gray")
        answer_field.config(bg="gray")

        for i in buttons:
            i.configure(bg="#5c6169", fg="#2ad11b")


# =======================================================

# initializes GUI and ets title and icon image
root = Tk()
root.title("Calculator")
root.geometry('275x350')
root.iconbitmap("C:/Python_Projects/Calculator/App_Files/icon_calculator.ico")

# layout of calculator buttons
calc_buttons = ["1", "2", "3", "+",
                "4", "5", "6", "-",
                "7", "8", "9", "*",
                "(", "0", ")", "/",
                ".", "CE", "ANS", "=",
                "light", "dark"]

# Initializes variables used through the GUI
buttons = []
rel_height = 0.1
rel_width = 0.25
rely = 0.4
relx = 0
rounded_rely = 0
button_font = "Arial, 14"
entry_font = "Arial, 20"
bg = "white"
fg = "black"

# Creates entry field frame where user sees their inputted values and answer
output_frame = Frame(root, bd=10, bg=bg, relief=SUNKEN)
output_frame.place(relheight=0.4, relwidth=1)

entry_field = Label(output_frame, bg=bg, font=entry_font)
entry_field.place(relheight=0.5, relwidth=1)

answer_field = Label(output_frame, bg=bg, font=entry_font)
answer_field.place(relheight=0.5, relwidth=1, rely=0.5)


for i in calc_buttons:
    # Define Buttons
    if i == "CE":
        button = Button(root, text=i, command=clear_everything, font=button_font, bg=bg, fg=fg)
    elif i == "ANS":
        button = Button(root, text=i, command=previous_answer, font=button_font, bg=bg, fg=fg)
    elif i == "=":
        button = Button(root, text=i, command=calculate, font=button_font, bg=bg, fg=fg)
    elif i == "light":
        button = Button(root, text="Light", command=lambda i=i: theme(i), font=button_font, fg=fg,
                        bg=bg)
    elif i == "dark":
        button = Button(root, text="Dark", command=lambda i=i: theme(i), font=button_font, fg=fg,
                        bg=bg)
    else:
        button = Button(root, text=i, command=lambda i=i: calculation(i), font=button_font, bg=bg, fg=fg)

    buttons.append(button)

    # place buttons on screen
    button.place(relheight=rel_height, relwidth=rel_width, relx=relx, rely=rely)
    if relx == 0.75:
        relx = 0
        rely += 0.1
        rounded_rely = round(rely, 2)  # rounded to prevent decimal points error
    elif rounded_rely == 0.9 and relx == 0:
        button.place(relheight=rel_height, relwidth=rel_width + 0.25, relx=relx, rely=rely)
        relx += 0.5
    elif rounded_rely == 0.9 and relx == 0.5:
        button.place(relheight=rel_height, relwidth=rel_width + 0.25, relx=relx, rely=rely)
    else:
        relx += 0.25

root.mainloop()
