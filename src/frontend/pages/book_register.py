import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from src.frontend.components import modal
from src.frontend.pages import lobby
from src.frontend.services.user import user_register
from src.frontend.services.userbooks import register_book



def main(root):
    
    def handle_register():
        try:
            title = entries[0].get()
            author = entries[1].get()
            pages = entries[2].get()
            year = entries[3].get()

            response = register_book(title, author, pages, year)

            if response:        

                modal.main(root, "Sucesso", "Cadastro realizado com sucesso!", modal.ModalTypes.INFO.value)
                frm.destroy()
                lobby.main(root)
        
        except Exception as e:
            print(e)
            modal.main(root, "Erro", "Erro ao realizar cadastro!", modal.ModalTypes.ERROR.value)
    
    # Criando um frame centralizado
    frm = ttk.Frame(root, padding=10)
    frm.place(relx=0.5, rely=0.5, anchor="center")

    # Carregar imagem do topo
    img_logo = Image.open("src/frontend/assets/images/soon.png").resize((400, 180), Image.Resampling.LANCZOS)
    img_logo = ImageTk.PhotoImage(img_logo)
    title_label = ttk.Label(frm, image=img_logo)
    title_label.image = img_logo  
    title_label.pack()

    # Label de instrução
    info_label = ttk.Label(frm, text="Informe os dados cadastrais do livro", font=("Arial", 14))
    info_label.pack(pady=(10, 20))

    # Campos de entrada
    labels = ["Título:", "Autor", "Paginas:", "Ano"]
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
    botao_cadastrar = tk.Button(frm, image=img_botao, borderwidth=0, command=handle_register)
    botao_cadastrar.image = img_botao  
    botao_cadastrar.pack(anchor="e", pady=(20, 0))

   
