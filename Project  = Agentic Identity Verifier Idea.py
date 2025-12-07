# Hackathone Project 1 :

# Agentic Identity Verifier Idea Book :

import tkinter as tk

chapters = [
["Chapter 1",
"An Agentic Identity Verifier is an advanced automated system.",
"It verifies human identity using artificial intelligence.",
"Its main purpose is to prevent fraud and identity theft.",
"It analyzes data and biometric information.",
"It serves as a digital guardian."],

["Chapter 2",
"The system monitors user activities.",
"Each action is checked by algorithms.",
"Alerts are generated for suspicious identity.",
"It is used in banking and security.",
"It increases digital trust."],

["Chapter 3",
"The system will become more autonomous.",
"Human work will be reduced.",
"Digital crimes will decrease.",
"Legal systems will improve.",
"It will become the pillar of digital identity."]
]

i = 0
root = tk.Tk()
root.title("Agentic Identity Verifier Idea Book")
root.geometry("600x350")

title = tk.Label(root, font=("Arial",14,"bold"))
title.pack(pady=5)

box = tk.Text(root, font=("Arial",11))
box.pack(expand=True, fill="both", padx=10)

def show():
    box.delete("1.0","end")
    title.config(text=chapters[i][0])
    for line in chapters[i][1:]:
        box.insert("end", line + "\n\n")

def nxt():
    global i
    if i < 2:
        i += 1
        show()

def prv():
    global i
    if i > 0:
        i -= 1
        show()

tk.Button(root, text="Prev", command=prv).pack(side="left", padx=20)
tk.Button(root, text="Next", command=nxt).pack(side="right", padx=20)

show()
root.mainloop()

# << practiced by Bint e Zain >>