import tkinter as tk
from tkinter import ttk, Toplevel

from src.frontend.constants.colors import FUNDO_AMARELO

'''
def create_table(search_entry, frame_container, data):
    """
    Cria uma tabela reutilizável para exibição de livros.

    :param search_entry: StringVar que armazena o termo de pesquisa.
    :param frame_container: Frame onde a tabela será carregada.
    :param data: Lista de dicionários no formato [{"titulo": str, "autor": str, "numero_paginas": int, "ano": int}, ...].
    :return: Retorna o objeto da tabela.
    """

    def get_center():
        # Obtém as dimensões da tela
        largura_tela = frame_container.winfo_screenwidth()
        altura_tela = frame_container.winfo_screenheight()

        # Define o tamanho da janela
        largura_janela = 350
        altura_janela = 150

        # Calcula a posição central
        pos_x = (largura_tela - largura_janela) // 2
        pos_y = (altura_tela - altura_janela) // 2

        # Aplica a posição calculada
        return(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
    
    # Criando o frame da tabela dentro do frame_container
    table_frame = tk.Frame(frame_container, bg="white")
    table_frame.pack(pady=10, fill="both", expand=True)

    # Criando a tabela
    columns = ("Título", "Autor", "Número de Páginas", "Ano de Publicação")
    tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)

    # Configuração das colunas
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=250)

    tree.pack(fill="both", expand=True)

    # Criando os botões Editar e Deletar
    button_frame = tk.Frame(frame_container, bg="white")
    button_frame.pack(pady=10)

    # Variável para armazenar os dados da linha selecionada
    button_frame.selected_data = {}

    # Função para capturar a seleção da linha
    def item_selected(event):
        selected_item = tree.selection()
        if selected_item:
            item = tree.item(selected_item[0])  # Pega os valores da linha selecionada
            valores = item["values"]
            if valores:
                button_frame.selected_data = {
                    "titulo": valores[0],
                    "autor": valores[1],
                    "numero_paginas": valores[2],
                    "ano": valores[3]
                }
                print(f"Linha Selecionada: {button_frame.selected_data}")

    tree.bind("<ButtonRelease-1>", item_selected)

    # Função para carregar os dados na tabela (útil para pesquisa)
    def load_data(filtered_data=None):
        tree.delete(*tree.get_children())  # Limpa a tabela
        display_data = filtered_data if filtered_data is not None else data
        for index, livro in enumerate(display_data):
            tree.insert("", "end", iid=index, values=(livro["titulo"], livro["autor"], livro["numero_paginas"], livro["ano"]))

    # Função de pesquisa
    def search_books(*args):
        query = search_entry.get().strip().lower()  # Obtém a string e formata
        if query:
            filtered_data = [livro for livro in data if query in livro["titulo"].lower() or query in livro["autor"].lower()]
            load_data(filtered_data)  # Atualiza a tabela
        else:
            load_data()  # Se vazio, exibe todos os dados

    # Aplica a pesquisa inicial e configura a atualização automática
    load_data()  
    search_entry.trace_add("write", search_books)  # Atualiza sempre que a entrada mudar

    # Botão Editar
    btn_editar = tk.Button(button_frame, text="Editar", command=lambda: open_edit_window(button_frame.selected_data))
    btn_editar.pack(side="left", padx=10)

    # Botão Deletar
    btn_deletar = tk.Button(button_frame, text="Deletar", command=lambda: open_delete_window(button_frame.selected_data))
    btn_deletar.pack(side="left", padx=10)

    # Função para abrir a tela de edição
    def open_edit_window(selected_data):
        if selected_data:
            edit_window = tk.Toplevel(frame_container)
            edit_window.title("Editar Livro")
            edit_window.geometry(get_center())

            tk.Label(edit_window, text=f"Editando: {selected_data['titulo']}").pack(pady=10)
            tk.Button(edit_window, text="Fechar", command=edit_window.destroy).pack(pady=10)

    # Função para abrir a tela de deleção
    def open_delete_window(selected_data):
        if selected_data:
            delete_window = tk.Toplevel(frame_container)
            delete_window.title("Confirmar Deleção")
            delete_window.geometry(get_center())
            delete_window.configure(bg=FUNDO_AMARELO)  # Fundo amarelo

            # Pergunta
            label = tk.Label(delete_window, text="Você realmente deseja apagar esse dado?", 
                            bg=FUNDO_AMARELO, fg="black", font=("Arial", 12, "bold"))
            label.pack(pady=15)

            # Frame para os botões
            button_frame = tk.Frame(delete_window, bg=FUNDO_AMARELO)
            button_frame.pack(pady=10)

            def confirm_delete():
                nonlocal data
                data = [livro for livro in data if livro != selected_data]  # Remove o item da lista
                update_table()  # Atualiza a tabela
                delete_window.destroy()
                print(selected_data)

            # Botão Sim
            btn_confirm = tk.Button(button_frame, text="Sim", bg="white", fg="black", font=("Arial", 10, "bold"), 
                                    width=10, command=confirm_delete)
            btn_confirm.pack(side="left", padx=10)

            # Botão Cancelar
            btn_cancel = tk.Button(button_frame, text="Cancelar", bg="white", fg="black", font=("Arial", 10, "bold"), 
                                width=10, command=delete_window.destroy)
            btn_cancel.pack(side="left", padx=10)

    def update_table():
        """Recarrega os dados na tabela para garantir atualização visual."""
        tree.delete(*tree.get_children())  # Limpa a tabela
        for index, livro in enumerate(data):  # Recarrega os dados da lista atualizada
            tree.insert("", "end", iid=index, values=(livro["titulo"], livro["autor"], livro["numero_paginas"], livro["ano"]))

    return tree  # Retorna a tabela para possíveis manipulações externas
'''

def create_table(search_entry, frame_container, data):
    """
    Cria uma tabela reutilizável para exibição de livros.

    :param search_entry: StringVar que armazena o termo de pesquisa.
    :param frame_container: Frame onde a tabela será carregada.
    :param data: Lista de dicionários no formato [{"id": int, "titulo": str, "autor": str, "numero_paginas": int, "ano": int}, ...].
    :return: Retorna o objeto da tabela.
    """

    def get_center():
        largura_tela = frame_container.winfo_screenwidth()
        altura_tela = frame_container.winfo_screenheight()
        largura_janela = 350
        altura_janela = 150
        pos_x = (largura_tela - largura_janela) // 2
        pos_y = (altura_tela - altura_janela) // 2
        return(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
    
    table_frame = tk.Frame(frame_container, bg="white")
    table_frame.pack(pady=10, fill="both", expand=True)

    columns = ("ID", "Título", "Autor", "Número de Páginas", "Ano de Publicação")
    tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=150 if col == "ID" else 250)

    tree.pack(fill="both", expand=True)

    button_frame = tk.Frame(frame_container, bg="white")
    button_frame.pack(pady=10)

    button_frame.selected_data = {}

    def item_selected(event):
        selected_item = tree.selection()
        if selected_item:
            item = tree.item(selected_item[0])
            valores = item["values"]
            if valores:
                button_frame.selected_data = {
                    "id": valores[0],
                    "titulo": valores[1],
                    "autor": valores[2],
                    "numero_paginas": valores[3],
                    "ano": valores[4]
                }
                print(f"Linha Selecionada: {button_frame.selected_data}")

    tree.bind("<ButtonRelease-1>", item_selected)

    def load_data(filtered_data=None):
        tree.delete(*tree.get_children())
        display_data = filtered_data if filtered_data is not None else data
        for livro in display_data:
            tree.insert("", "end", iid=livro["id"], values=(livro["id"], livro["titulo"], livro["autor"], livro["numero_paginas"], livro["ano"]))

    def search_books(*args):
        query = search_entry.get().strip().lower()
        if query:
            filtered_data = [livro for livro in data if query in livro["titulo"].lower() or query in livro["autor"].lower()]
            load_data(filtered_data)
        else:
            load_data()

    load_data()
    search_entry.trace_add("write", search_books)

    btn_editar = tk.Button(button_frame, text="Editar", command=lambda: open_edit_window(button_frame.selected_data))
    btn_editar.pack(side="left", padx=10)

    btn_deletar = tk.Button(button_frame, text="Deletar", command=lambda: open_delete_window(button_frame.selected_data))
    btn_deletar.pack(side="left", padx=10)

    def open_edit_window(selected_data):
        if selected_data:
            edit_window = tk.Toplevel(frame_container)
            edit_window.title("Editar Livro")
            edit_window.geometry(get_center())
            tk.Label(edit_window, text=f"Editando: {selected_data['titulo']}").pack(pady=10)
            tk.Button(edit_window, text="Fechar", command=edit_window.destroy).pack(pady=10)

    def open_delete_window(selected_data):
        if selected_data:
            delete_window = tk.Toplevel(frame_container)
            delete_window.title("Confirmar Deleção")
            delete_window.geometry(get_center())
            delete_window.configure(bg=FUNDO_AMARELO)

            label = tk.Label(delete_window, text="Você realmente deseja apagar esse dado?", 
                            bg=FUNDO_AMARELO, fg="black", font=("Arial", 12, "bold"))
            label.pack(pady=15)

            button_frame = tk.Frame(delete_window, bg=FUNDO_AMARELO)
            button_frame.pack(pady=10)

            def confirm_delete():
                nonlocal data
                data = [livro for livro in data if livro["id"] != selected_data["id"]]
                update_table()
                delete_window.destroy()
                print(selected_data)

            btn_confirm = tk.Button(button_frame, text="Sim", bg="white", fg="black", font=("Arial", 10, "bold"), 
                                    width=10, command=confirm_delete)
            btn_confirm.pack(side="left", padx=10)

            btn_cancel = tk.Button(button_frame, text="Cancelar", bg="white", fg="black", font=("Arial", 10, "bold"), 
                                width=10, command=delete_window.destroy)
            btn_cancel.pack(side="left", padx=10)

    def update_table():
        tree.delete(*tree.get_children())
        for livro in data:
            tree.insert("", "end", iid=livro["id"], values=(livro["id"], livro["titulo"], livro["autor"], livro["numero_paginas"], livro["ano"]))

    return tree
