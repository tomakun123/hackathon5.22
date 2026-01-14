from pynput import keyboard
import pandas as pd
import subprocess

#Start of code

count = 0
keys = [""]
secret = [""]

badWords = pd.read_csv("bad-words.csv")
bwcol = badWords.columns
mainbw = badWords[bwcol[0]]
badWordsList = mainbw.tolist()
with open("additionalWords.txt", "r") as g:
    additionalWords = g.read().split(", ")
print(additionalWords)
for x in additionalWords:
    badWordsList.append(x)

# writes characters excluding space, backspace, and other special keystrokes
def write_txt(keys):
    typed = ' '.join(str(item.char) for item in keys)
    with open("keylogger.txt", "a") as f:
        f.write(typed)

# writes special keystrokes
def write_other(secret):
    special = ' '.join(str(item) for item in secret)
    with open("keylogger.txt", "a") as f:
        f.write(special)
        

def on_press(key):
    global secret
    global keys
    try:
        keys[0] = (key) #for letters/numbers (doesn't work for space and backspace)
        write_txt(keys)
        print("{0} was pressed".format(key.char))
        

    except AttributeError:
        if key == keyboard.Key.space:
            secret[0] = " " #creates a space
            write_other(secret)
            secret[0] = "" #resets var secret

            #Filter
            with open("keylogger.txt", "r") as f:
                file_content = f.read().strip()
            file_content = file_content.split()
            
            if file_content[len(file_content)-1] in badWordsList:
                print("Flagged Word Found, Shutting Down Program")
                # Execute the system command to force quit Safari on macOS
                subprocess.run(["osascript", "-e", 'quit app "Safari"'])

        elif key == keyboard.Key.backspace:
            with open("keylogger.txt", "r") as f:
                text = f.read()
                text = text[0: (len(text) - 1)] #substring may have issues
            with open("keylogger.txt", "w") as f:
                f.write("")
            with open("keylogger.txt", "a") as f:
                f.write(text)
            

def on_release(key):
    if key == keyboard.Key.esc:
        with open("keylogger.txt", "a") as f:
            f.truncate(0)
        return False
    
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release,
        write_txt=write_txt) as listener:
    listener.join()