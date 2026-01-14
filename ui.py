import tkinter as tk
from tkinter import font

additionalWords = ""
window = tk.Tk()
window.geometry("500x400")
window.resizable(False,False)

# Set the window title
window.title("Censor for School")

# Create a label widget
sizedif = font.Font(size=40)
sizedif2 = font.Font(size=16) 
main = tk.Label(text="Test", fg="black", bg="white")
label = tk.Label(window, text="Censoring for School!", font=sizedif)
label.pack(anchor=tk.CENTER)

# Question to add words
label = tk.Label(window, text="What words would you like to ban? \nInput Additional Words in the following format: \nWord1, Word2, Word3", font=sizedif2)
label.pack(anchor=tk.CENTER)

# Create an entry widget
entry = tk.Entry(window, width=20)
entry.place(x=150,y=150)
    

# Function to handle button click
def handle_button_click():
    additionalWords = entry.get()  # Get the text from the entry widget
    print(type(additionalWords))
    print("Words:", additionalWords)
    with open('additionalWords.txt', "w") as f:
        f.write(additionalWords)


# Create a button widget
button = tk.Button(window, text="Submit", command=handle_button_click)
button.place(x=205,y=200)

# Start the Tkinter event loop
window.mainloop()

print(additionalWords)