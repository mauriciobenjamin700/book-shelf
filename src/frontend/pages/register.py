import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Para manipulação de imagens

def centralizar_janela(root, largura, altura):
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    pos_x = (largura_tela - largura) // 2
    pos_y = (altura_tela - altura) // 2
    root.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

def abrir_cadastro():  # Renomeado para ser chamado externamente
    cadastro = tk.Toplevel()  # Criar nova janela
    cadastro.title("Book Shelf - Cadastro")
    largura, altura = 1280, 720
    centralizar_janela(cadastro, largura, altura)
    cadastro.resizable(False, False)

    # Criando um frame centralizado
    frm = ttk.Frame(cadastro, padding=10)
    frm.place(relx=0.5, rely=0.5, anchor="center")

    # Carregar imagem do topo
    img_logo = Image.open("src/frontend/assets/images/soon.png").resize((400, 180), Image.Resampling.LANCZOS)
    img_logo = ImageTk.PhotoImage(img_logo)
    title_label = ttk.Label(frm, image=img_logo)
    title_label.image = img_logo  
    title_label.pack()

    # Label de instrução
    info_label = ttk.Label(frm, text="Informe os dados cadastrais", font=("Arial", 14))
    info_label.pack(pady=(10, 20))

    # Campos de entrada
    labels = ["Nome:", "E-mail:", "Senha:", "Confirmar Senha:"]
    entries = []

    for label in labels:
        lbl = ttk.Label(frm, text=label, font=("Arial", 12))
        lbl.pack(anchor="w")
        entry = ttk.Entry(frm, width=60, show="*" if "Senha" in label else "")
        entry.pack(pady=(0, 10))
        entries.append(entry)

    # Botão de cadastro (imagem)
    img_botao = Image.open("src/frontend/assets/images/cadastrar.png").resize((200, 60), Image.Resampling.LANCZOS)
    img_botao = ImageTk.PhotoImage(img_botao)
    botao_cadastrar = tk.Button(frm, image=img_botao, borderwidth=0, command=lambda: print("Cadastro realizado!"))
    botao_cadastrar.image = img_botao  
    botao_cadastrar.pack(anchor="e", pady=(20, 0))

    # Mantendo referências para evitar descarte
    cadastro.img_logo = img_logo
    cadastro.img_botao = img_botao
