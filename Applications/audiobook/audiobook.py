import pyttsx3
with open(r"book.txt") as book:
    book_text=book.readlines()
engine = pyttsx3.init()
for i in book_text:
    engine.say(i)
    engine.runAndWait()
