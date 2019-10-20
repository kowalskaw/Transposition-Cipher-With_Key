from tkinter import *
from encrypt_transpos_cipher import EncryptTranspositionCipher as etc


def create_encryptor(word, text):
    encryptor = etc(word=word, input=text)
    encryptor.check_blocks_and_encrypt()
    return encryptor.get_encrypted()


def enter_given_input():
    # this will collect the text from the entry box
    entered_word = word.get()
    entered_text = explicit_text.get()
    # clearing boxes
    # word.delete(0.0, END)
    # explicit_text.delete(0.0, END)
    output.delete(0.0, END)
    encrypted_text = create_encryptor(entered_word, entered_text)
    output.insert(END, encrypted_text)


# main
window = Tk()
window.title("Encryptor")
window.configure(background="grey")


# WORD
# label
Label(window, text="Enter word:", bg="grey", fg="white",
      font="none 12 bold").grid(row=1, column=0, sticky=W)
# entry text box
word = Entry(window, width=40, bg="lightgrey")
word.grid(row=2, column=0, sticky=W)

# TEXT
# label
Label(window, text="Enter text to encrypt:", bg="grey",
      fg="white", font="none 12 bold") \
    .grid(row=3, column=0, sticky=W)
# entry text box
explicit_text = Entry(window, width=40, bg="lightgrey")
explicit_text.grid(row=4, column=0, sticky=W)

# SUBMIT USER INPUT
# submit button for submitting word/key
Button(window, text="Submit", width=6, command=enter_given_input) \
    .grid(row=6, column=0, sticky=N)


# label for displaying result
Label(window, text="\n"
                   "Encrypted text:", bg="grey", fg="white",
      font="none 12 bold").grid(row=10, column=0, sticky=W)
# text box
output = Text(window, width=30, height=12, wrap=WORD, background="lightgrey")
output.grid(row=11, column=0, columnspan=2, sticky=W)

# app = Window(window)
window.mainloop()
