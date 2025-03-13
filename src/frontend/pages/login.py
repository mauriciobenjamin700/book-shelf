import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  

def centralizar_janela(janela, largura, altura):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    pos_x = (largura_tela - largura) // 2
    pos_y = (altura_tela - altura) // 2
    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

def main():
    login_window = tk.Toplevel()  # Criar uma nova janela em vez de Tk()
    login_window.title("Book Shelf - Login")
    largura, altura = 1280, 720
    centralizar_janela(login_window, largura, altura)
    login_window.resizable(False, False)

    frm = ttk.Frame(login_window, padding=10)
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
    continue_button = tk.Button(frm, image=img_continue, borderwidth=0, command=lambda: print("Login realizado!"))
    continue_button.image = img_continue  
    continue_button.pack(pady=10)

    login_window.img_logo = img_logo
    login_window.img_continue = img_continue

    login_window.mainloop()




