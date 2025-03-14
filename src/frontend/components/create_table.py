import tkinter as tk
from tkinter import ttk, Toplevel

from src.frontend.constants.colors import FUNDO_AMARELO
from src.frontend.services.userbooks import delete_book


def create_table(search_entry, frame_container, data):
    """
    Cria uma tabela reutilizável para exibição de livros.

    :param search_entry: StringVar que armazena o termo de pesquisa.
    :param frame_container: Frame onde a tabela será carregada.
    :param data: Lista de dicionários no formato [{"id": int, "title": str, "author": str, "pages": int, "year": int}, ...].
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

    # Alterado para refletir os nomes das chaves em inglês
    columns = ("ID", "Title", "Author", "Pages", "Year")
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
                    "title": valores[1],   # Mudança aqui
                    "author": valores[2],  # Mudança aqui
                    "pages": valores[3],   # Mudança aqui
                    "year": valores[4]     # Mudança aqui
                }
                print(f"Linha Selecionada: {button_frame.selected_data}")

    tree.bind("<ButtonRelease-1>", item_selected)

    def load_data(filtered_data=None):
        tree.delete(*tree.get_children())
        display_data = filtered_data if filtered_data is not None else data
        for livro in display_data:
            tree.insert(
                "", "end", iid=livro["id"], 
                values=(livro["id"], livro["title"], livro["author"], livro["pages"], livro["year"])  # Mudança aqui
            )

    def search_books(*args):
        query = search_entry.get().strip().lower()
        if query:
            filtered_data = [livro for livro in data if query in livro["title"].lower() or query in livro["author"].lower()]  # Mudança aqui
            load_data(filtered_data)
        else:
            load_data()

    load_data()
    search_entry.trace_add("write", search_books)

    btn_editar = tk.Button(button_frame, text="Edit", command=lambda: open_edit_window(button_frame.selected_data))  # Mudança aqui
    btn_editar.pack(side="left", padx=10)

    btn_deletar = tk.Button(button_frame, text="Delete", command=lambda: open_delete_window(button_frame.selected_data))  # Mudança aqui
    btn_deletar.pack(side="left", padx=10)

    def open_edit_window(selected_data):
        if selected_data:
            edit_window = tk.Toplevel(frame_container)
            edit_window.title("Edit Book")
            edit_window.geometry(get_center())
            tk.Label(edit_window, text=f"Editing: {selected_data['title']}").pack(pady=10)
            tk.Button(edit_window, text="Close", command=edit_window.destroy).pack(pady=10)

    def open_delete_window(selected_data):
        if selected_data:
            delete_window = tk.Toplevel(frame_container)
            delete_window.title("Confirm Deletion")
            delete_window.geometry(get_center())
            delete_window.configure(bg=FUNDO_AMARELO)

            label = tk.Label(delete_window, text="Do you really want to delete this book?", 
                            bg=FUNDO_AMARELO, fg="black", font=("Arial", 12, "bold"))
            label.pack(pady=15)

            button_frame = tk.Frame(delete_window, bg=FUNDO_AMARELO)
            button_frame.pack(pady=10)

            def confirm_delete():
                nonlocal data
                data = [livro for livro in data if livro["id"] != selected_data["id"]]
                delete_book(selected_data["id"])
                update_table()
                delete_window.destroy()
                print(selected_data)

            btn_confirm = tk.Button(button_frame, text="Yes", bg="white", fg="black", font=("Arial", 10, "bold"), 
                                    width=10, command=confirm_delete)
            btn_confirm.pack(side="left", padx=10)

            btn_cancel = tk.Button(button_frame, text="Cancel", bg="white", fg="black", font=("Arial", 10, "bold"), 
                                width=10, command=delete_window.destroy)
            btn_cancel.pack(side="left", padx=10)

    def update_table():
        tree.delete(*tree.get_children())
        for livro in data:
            tree.insert(
                "", "end", iid=livro["id"], 
                values=(livro["id"], livro["title"], livro["author"], livro["pages"], livro["year"])  # Mudança aqui
            )

    return tree
