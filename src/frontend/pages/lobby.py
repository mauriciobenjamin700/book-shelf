import tkinter as tk
from tkinter import messagebox
from src.frontend.components.create_header import header
from src.frontend.components.create_search_bar import create_search_bar
from src.frontend.components.create_table import create_table
from src.frontend.services.userbooks import get_books

def main(root):
    '''
    data = [
        ("O Senhor dos Anéis", "J.R.R. Tolkien",1, 1954),
        ("Dom Casmurro", "Machado de Assis",3, 1899),
        ("Cem Anos de Solidão", "Gabriel García Márquez",4,1967),
        ("A Revolução dos Bichos", "George Orwell",5, 1945),
        ("Harry Potter e a Pedra Filosofal", "J.K. Rowling",5, 1997),
        ("O Pequeno Príncipe", "Antoine de Saint-Exupéry",6, 1943),
        ("Crime e Castigo", "Fiódor Dostoiévski",7, 1866),
        ("O Nome do Vento", "Patrick Rothfuss", 8,2007),
        ("O Código Da Vinci", "Dan Brown",9 ,2003),
        ("joao","1",22,2002)
    ]
    '''
    
    '''
    data = [
    {"id": "1", "titulo": "Livro A", "autor": "Autor A", "numero_paginas": 200, "ano": 2020},
    {"id": "2", "titulo": "Livro B", "autor": "Autor B", "numero_paginas": 150, "ano": 2021}
    ]
    '''
    
    print("chegou aqui")
    data = get_books()
    print(data)

    filtered_data = [{k: v for k, v in book.items() if k not in ["created_at", "updated_at"]} for book in data]

    print(filtered_data)

    # Função para fechar a aplicação
    def sair():
        root.quit()

    # Criando a janela principal
    frm = tk.Frame(root)
    frm.pack(fill="both", expand=True)

    
    # Adicionando o header
    header(frm, sair)

    # Adicionando a barra de pesquisa
    search_entry = create_search_bar(frm)

    create_table(search_entry,frm,filtered_data)
