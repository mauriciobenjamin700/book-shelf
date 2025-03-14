import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Pillow para redimensionamento de imagens
from src.frontend.pages.login import main as abrir_login
from src.frontend.pages.register import abrir_cadastro

# Função para centralizar a janela no meio da tela
def centralizar_janela(root, largura, altura):
    largura_tela = root.winfo_screenwidth()  
    altura_tela = root.winfo_screenheight()  
    pos_x = (largura_tela - largura) // 2  
    pos_y = (altura_tela - altura) // 2  
    root.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")  

# Função principal para criar a interface gráfica
def main():

    def handle_login():
        frm.destroy()
        abrir_login(root)
    
    
    def handle_register():
        abrir_cadastro(root)
        frm.destroy()
    
    root = tk.Tk()  
    root.title("Book Shelf")  
    root.update_idletasks()  
    largura, altura = 1280, 720  
    centralizar_janela(root, largura, altura)  
    root.resizable(False, False)  

    # Criar um frame centralizado
    frm = ttk.Frame(root, padding=10)
    frm.place(relx=0.5, rely=0.5, anchor="center")  

    # Carregar e redimensionar imagens dos botões
    img_entrar = Image.open("src/frontend/assets/images/entrar.png")
    img_entrar = img_entrar.resize((200, 60), Image.Resampling.LANCZOS)  
    img_entrar = ImageTk.PhotoImage(img_entrar)

    img_cadastrar = Image.open("src/frontend/assets/images/cadastrar.png")
    img_cadastrar = img_cadastrar.resize((200, 60), Image.Resampling.LANCZOS)  
    img_cadastrar = ImageTk.PhotoImage(img_cadastrar)

    # Criar rótulo para imagem principal
    img_logo = Image.open("src/frontend/assets/images/soon.png")
    img_logo = img_logo.resize((500, 200), Image.Resampling.LANCZOS)  
    img_logo = ImageTk.PhotoImage(img_logo)

    title_label = ttk.Label(frm, image=img_logo)
    title_label.pack()

    # Label de boas-vindas
    welcome_label = ttk.Label(frm, text="Bem-vindo ao Book Shelf, entre com sua conta para continuar", font=("Arial", 18))
    welcome_label.pack(pady=(10, 20))  

    # Botão "Entrar" que chama a tela de login
    entrar_button = tk.Button(frm, image=img_entrar, borderwidth=0, command=handle_login)
    entrar_button.pack(pady=10)

    # Botão "Cadastrar"
    cadastrar_button = tk.Button(frm, image=img_cadastrar, borderwidth=0, command=handle_register)
    cadastrar_button.pack(pady=10)

    # Manter referências das imagens para evitar descarte pelo Garbage Collector
    root.img_logo = img_logo
    root.img_entrar = img_entrar
    root.img_cadastrar = img_cadastrar

    root.mainloop()  








