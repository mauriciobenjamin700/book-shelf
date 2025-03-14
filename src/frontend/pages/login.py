import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from src.frontend.pages import lobby
from src.frontend.services.user import user_login  


def main(root):

    def handle_login():
        
        try:
            email = email_entry.get()
            password = senha_entry.get()
            response = user_login(email,password)
            if response:
                lobby.main(root)

        except:
            pass

    frm = ttk.Frame(root, padding=10)
    frm.place(relx=0.5, rely=0.5, anchor="center")

    # Carregar imagem do logo
    img_logo = Image.open("src/frontend/assets/images/soon.png").resize((400, 180), Image.Resampling.LANCZOS)
    img_logo = ImageTk.PhotoImage(img_logo)
    title_label = ttk.Label(frm, image=img_logo)
    title_label.image = img_logo  
    title_label.pack()

    welcome_label = ttk.Label(frm, text="Bem-vindo", font=("Arial", 18))
    welcome_label.pack(pady=(10, 20))

    email_label = ttk.Label(frm, text="E-mail:", font=("Arial", 12))
    email_label.pack(anchor="w")
    email_entry = ttk.Entry(frm, width=60)
    email_entry.pack(pady=(0, 10))

    senha_label = ttk.Label(frm, text="Senha:", font=("Arial", 12))
    senha_label.pack(anchor="w")
    senha_entry = ttk.Entry(frm, width=60, show="*")
    senha_entry.pack(pady=(0, 20))

  

    img_continue = Image.open("src/frontend/assets/images/Continue.png").resize((200, 60), Image.Resampling.LANCZOS)
    img_continue = ImageTk.PhotoImage(img_continue)
    continue_button = tk.Button(frm, image=img_continue, borderwidth=0, command=lambda: handle_login())
    continue_button.image = img_continue  
    continue_button.pack(pady=10)





