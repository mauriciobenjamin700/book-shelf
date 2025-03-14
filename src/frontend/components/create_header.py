import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from src.frontend.constants.colors import FUNDO_AMARELO

def header(root,sair):
    # Cor do cabeçalho
    cor_cabecalho = FUNDO_AMARELO

    # Criando o cabeçalho
    header = tk.Frame(root, bg=cor_cabecalho, height=60)
    header.pack(fill="x", side="top")

    header_content = tk.Frame(header, bg=cor_cabecalho, height=60)
    header_content.pack(expand=True, fill="both")
    header_content.pack_propagate(False)

    # Botão de menu (canto esquerdo)
    menu_img = Image.open("src/frontend/assets/images/Sidebar Button.png").resize((40, 40))
    menu_img = ImageTk.PhotoImage(menu_img)
    btn_menu = tk.Button(header_content, image=menu_img, borderwidth=0, bg=cor_cabecalho, command=lambda: print("Menu aberto"))
    btn_menu.image = menu_img
    btn_menu.pack(side="left", padx=20, pady=10)

    # Logo central no cabeçalho
    logo_img = Image.open("src/frontend/assets/images/soon.png").resize((100, 50))
    logo_img = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(header_content, image=logo_img, bg=cor_cabecalho)
    logo_label.image = logo_img
    logo_label.pack(side="left", expand=True)

    # Botão de saída (canto direito)
    exit_img = Image.open("src/frontend/assets/images/sair.png").resize((40, 40))
    exit_img = ImageTk.PhotoImage(exit_img)
    btn_exit = tk.Button(header_content, image=exit_img, borderwidth=0, bg=cor_cabecalho, command=sair)
    btn_exit.image = exit_img
    btn_exit.pack(side="right", padx=20, pady=10)