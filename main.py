from tkinter import *
import pandas
from random import choice
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
word = ""
CAN_CLICK = False


def change():
    global word, CAN_CLICK
    canvas.itemconfig(main_image, image=back_image)
    canvas.itemconfig(text_lang, text="ENGLISH")
    word_in_eng = data_dict[word]
    canvas.itemconfig(text_prt, text=word_in_eng)
    CAN_CLICK = True


def wrong_command():
    global CAN_CLICK
    if CAN_CLICK:
        canvas.itemconfig(main_image, image=front_image)
        timer_to_back()
        CAN_CLICK = False


def right_command():
    global CAN_CLICK, word
    if CAN_CLICK:
        canvas.itemconfig(main_image, image=front_image)
        timer_to_back()
        CAN_CLICK = False
        french_list.pop(french_list.index(word))
        print(len(french_list))


def timer_to_back():
    global word, CAN_CLICK

    try:
        word = choice(french_list)
    except IndexError:
        messagebox.showinfo(title="Congrats", message="You Have Learnt All Words in this List")
        CAN_CLICK = False
    else:
        canvas.itemconfig(text_lang, text="FRENCH")
        canvas.itemconfig(text_prt, text = word)
        window.after(3000, change)



# ------------Pandas Data------------------#

data = pandas.read_csv("data/french_words.csv")
data_dict = {row.French: row.English for (index, row) in data.iterrows()}
french_list = [name for name in data_dict]

# ------------------ IMAGES -----------------------------#

front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
img_right = PhotoImage(file="images/right.png")
img_wrong = PhotoImage(file="images/wrong.png")

# -------------- User Interface ----------------------#

canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
main_image = canvas.create_image(400, 263, image=front_image)
canvas.grid(row=0, column=0, columnspan=3)
text_prt = canvas.create_text(400, 275, text=f"", font=("ariel", 24, "normal"))
text_lang = canvas.create_text(400, 245, text="FRENCH", font=("Courier", 30, "bold"))

tick_button = Button(width=100, height=100, image=img_right, highlightthickness=0)
tick_button.grid(row=1, column=0)
tick_button.config(command=right_command)

cross_button = Button(width=100, height=100, image=img_wrong, highlightthickness=0)
cross_button.grid(row=1, column=2)
cross_button.config(command=wrong_command)


timer_to_back()

window.mainloop()