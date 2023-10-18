#install the two necessary libraries
#pip install googletrans
#pip instal gTTS
from tkinter import *
from googletrans import Translator
from gtts import gTTS

def language_translator():
    change = None      ##it will be overwritten in the if-else block.... so it can be assigned []
    one = text_win.get()
    two = Translator()
    three = lang_dropdown.get()

    if three == "French":
        change = "fr"
    elif three == "English":
        change = "en"
    elif three == "German":
        change = "de"
    elif three == "Greece":
        change = "el"
    elif three == "Japan":
        change= "ja"

    lang_translate = two.translate(one, dest=change) #
    lang_translate = lang_translate.text

    iv = gTTS(text=lang_translate, slow=False, lang=change)
    label_1.config(text=lang_translate)

languages = ["French",
             "English",
             "German",
             "Greece",
             "Japan"]
tk_project = Tk()
tk_project.geometry("600x600") #square shape
tk_project.config(bg="white")



text_win = Entry(tk_project, bg="Orange", fg="white", border=10, borderwidth=10, font=("Baskerville", 16))
text_win.place(x = 10, y = 50)

lang_dropdown = StringVar()
lang_dropdown.set("Choose one Language")

Languages = OptionMenu(tk_project, lang_dropdown, *languages)
Languages.configure(bg="orange", fg="white", border=5, borderwidth=5, font=("Baskerville", 16, "bold"))
Languages.place(x=300, y=50)

label_1 = Label(tk_project, text="\n\n\n\n\n\n", bg="white", fg="white", font=("Baskerville", 14))
label_1.place(x = 1, y= 150)

label_1 = Label(tk_project, text="Here's the Translation", bg="White", fg="black", font=("Baskerville", 20))
label_1.place(x = 100, y=200)

transltn_btn = Button(tk_project, text="Translate!!", bg="white", fg="black", borderwidth= 10, font=("baskerville", 22, "bold"), command=language_translator)
transltn_btn.place(x = 200, y=500)

tk_project.mainloop()