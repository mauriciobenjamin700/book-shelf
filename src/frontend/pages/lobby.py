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
    
    
    data = [
    {"ID":"33r2dw","titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "numero_paginas": 1, "ano": 1954},
    {"ID": "121DDW","titulo": "Dom Casmurro", "autor": "Machado de Assis", "numero_paginas": 3, "ano": 1899}
    ]
    
    
    #data = get_books()
    #print(data)


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

    create_table(search_entry,frm,data)
