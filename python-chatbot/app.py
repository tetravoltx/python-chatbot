import tkinter as tk
from tkinter import scrolledtext
import tkinter.font as tkfont
from ai_logic import ask_gemini

root = tk.Tk()

BG = "#0a0a0a"
BG_LIGHT = "#141414"
FG = "#e8e8e8"
FG_DIM = "#6b6b6b"
ACCENT = "#ffffff"
BORDER = "#2a2a2a"

def pick_font(preferred, size=11, weight="normal"):
    available = tkfont.families()
    for font in preferred:
        if font in available:
            return (font, size, weight)
    return ("Arial", size, weight)

FONT_MAIN = pick_font(["JetBrains Mono", "Consolas", "Monaco", "Courier New"], size=10)
FONT_TITLE = pick_font(["JetBrains Mono", "Consolas"], size=12, weight="bold")

current_chat = []
chats = []

def send_prompt():
    global current_chat
    
    prompt = input_box.get("1.0", tk.END).strip()
    if not prompt:
        return
    
    input_box.delete("1.0", tk.END)
    input_box.config(state="disabled")
    
    output_box.config(state="normal")
    
    output_box.insert(tk.END, "user@gemini:~$ ", "prompt")
    output_box.insert(tk.END, prompt + "\n", "user")
    output_box.see(tk.END)
    output_box.update()
    
    try:
        response = ask_gemini(prompt)
    except Exception as e:
        response = f"Error: {str(e)}"
    
    output_box.insert(tk.END, response + "\n\n", "bot")
    
    current_chat.append(("USER", prompt))
    current_chat.append(("BOT", response))
    
    output_box.config(state="disabled")
    output_box.see(tk.END)
    
    input_box.config(state="normal")
    input_box.focus()

def handle_enter(event):
    if event.state & 0x0001:
        return
    send_prompt()
    return "break"

def new_chat():
    global current_chat
    if current_chat:
        chats.append(list(current_chat))
    current_chat = []
    output_box.config(state="normal")
    output_box.delete("1.0", tk.END)
    output_box.config(state="disabled")

root.title("CHATBOT")
root.geometry("900x600")
root.configure(bg=BG)
root.minsize(600, 400)

header = tk.Frame(root, bg=BG, height=50)
header.pack(fill="x", padx=20, pady=(16, 0))
header.pack_propagate(False)

title = tk.Label(
    header,
    text="CHATBOT",
    font=FONT_TITLE,
    bg=BG,
    fg=ACCENT,
    anchor="w"
)
title.pack(side="left", fill="y")

new_btn = tk.Button(
    header,
    text="⟳",
    command=new_chat,
    bg=BG,
    fg=FG_DIM,
    font=("Arial", 18),
    relief="flat",
    borderwidth=0,
    width=2,
    cursor="hand2",
    activebackground=BG,
    activeforeground=ACCENT
)
new_btn.pack(side="right")

def btn_enter(e):
    new_btn.config(fg=ACCENT)

def btn_leave(e):
    new_btn.config(fg=FG_DIM)

new_btn.bind("<Enter>", btn_enter)
new_btn.bind("<Leave>", btn_leave)

output_frame = tk.Frame(root, bg=BG)
output_frame.pack(fill="both", expand=True, padx=20, pady=16)

output_box = scrolledtext.ScrolledText(
    output_frame,
    bg=BG,
    fg=FG,
    insertbackground=ACCENT,
    font=FONT_MAIN,
    wrap=tk.WORD,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    padx=12,
    pady=12
)
output_box.pack(fill="both", expand=True)
output_box.config(state="disabled")

output_box.tag_config("prompt", foreground=FG_DIM)
output_box.tag_config("user", foreground=ACCENT)
output_box.tag_config("bot", foreground=FG, spacing3=8)

input_container = tk.Frame(root, bg=BG)
input_container.pack(fill="x", padx=20, pady=(0, 20))

input_wrapper = tk.Frame(
    input_container, 
    bg=BG_LIGHT,
    highlightbackground=BORDER,
    highlightthickness=1
)
input_wrapper.pack(fill="x")

prompt_label = tk.Label(
    input_wrapper,
    text="user@gemini:~$",
    font=FONT_MAIN,
    bg=BG_LIGHT,
    fg=FG_DIM,
    padx=12
)
prompt_label.pack(side="left")

input_box = tk.Text(
    input_wrapper,
    height=1,
    bg=BG_LIGHT,
    fg=FG,
    insertbackground=ACCENT,
    insertwidth=2,
    font=FONT_MAIN,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    padx=4,
    pady=0
)
input_box.pack(side="left", fill="both", expand=True, pady=12)

def input_focus_in(e):
    input_wrapper.config(highlightbackground=ACCENT)
    prompt_label.config(fg=ACCENT)

def input_focus_out(e):
    input_wrapper.config(highlightbackground=BORDER)
    prompt_label.config(fg=FG_DIM)

input_box.bind("<FocusIn>", input_focus_in)
input_box.bind("<FocusOut>", input_focus_out)
input_box.bind("<Return>", handle_enter)

root.mainloop()