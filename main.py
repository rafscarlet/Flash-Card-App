from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE = "Spanish"
FONT_LANGUAGE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")

word_pool = {}
try:
    data = pandas.read_csv('./to_learn/spanish_tolearn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('./data/spanish_words.csv')
    word_pool = original_data.to_dict("records")
else:
    word_pool = data.to_dict("records")

# ------------------- Flip Card Sides --------------------#


def flip():
    # Find word Translation
    global chosen_word
    translation = chosen_word["English"]

    # Flip UI
    flashcard.itemconfig(card_bg, image=back_img)
    flashcard.itemconfig(language_txt, text="English", fill='white')
    flashcard.itemconfig(word_txt, text=translation, fill='white')


# -------------------- Show new Word -------------------- #

def gen_word():
    # Pick random Foreign Word
    global chosen_word
    global clock
    window.after_cancel(clock)
    chosen_word = random.choice(word_pool)
    es_word = chosen_word["Spanish"]

    # Set it as the text on the canvas
    flashcard.itemconfig(word_txt, text=es_word, fill='black')
    flashcard.itemconfig(language_txt, text=LANGUAGE, fill='black')
    clock = window.after(3000, flip)

# ---------------------- Words to Learn ---------------------- #


def update_to_learn():
    word_pool.remove(chosen_word)
    print(len(word_pool))
    data = pandas.DataFrame(word_pool)
    data.to_csv('./to_learn/spanish_tolearn.csv', index=False)
    gen_word()


# --------------------- Building the UI --------------------- #

window = Tk()
window.title(f"{LANGUAGE} FlashCards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Images
front_img = PhotoImage(file='./images/card_front.png')
back_img = PhotoImage(file='./images/card_back.png')
right_img = PhotoImage(file='./images/right.png')
wrong_img = PhotoImage(file='./images/wrong.png')

# Canvas
flashcard = Canvas(width=800, height=526,
                   bg=BACKGROUND_COLOR, highlightthickness=0)

# Canvas Contents
card_bg = flashcard.create_image(400, 263, image=front_img)
language_txt = flashcard.create_text(
    400, 150, text=LANGUAGE, font=FONT_LANGUAGE)
word_txt = flashcard.create_text(400, 263, text="Word", font=FONT_WORD)
flashcard.grid(row=0, column=0, columnspan=2)

# Buttons
x_btn = Button(image=wrong_img, highlightthickness=0,
               border=0, command=gen_word)
x_btn.grid(row=1, column=0)

v_btn = Button(image=right_img, highlightthickness=0,
               border=0, command=update_to_learn)
v_btn.grid(row=1, column=1)

# --------------- main -----------------#

clock = window.after(3000, flip)
gen_word()

window.mainloop()
