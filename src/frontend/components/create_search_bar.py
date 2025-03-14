
import tkinter as tk
from PIL import Image, ImageTk


def create_search_bar(root):
    search_frame = tk.Frame(root, bg="white")
    search_frame.pack(pady=15)

    search_entry_frame = tk.Frame(search_frame, bg="white", bd=2, relief="sunken")
    search_entry_frame.pack()

    search_entry = tk.Entry(search_entry_frame, width=40, borderwidth=0, font=("Arial", 12))
    search_entry.pack(side="left", ipady=5, padx=5)

    search_img = Image.open("src/frontend/assets/images/lupa.png").resize((25, 25))
    search_img = ImageTk.PhotoImage(search_img)

    # Variável para armazenar o texto digitado
    search_result = tk.StringVar()

    def get_search_text():
        search_result.set(search_entry.get())  # Atualiza a variável com o texto digitado

    btn_search = tk.Button(search_entry_frame, image=search_img, borderwidth=0, bg="white", command=get_search_text)
    btn_search.image = search_img
    btn_search.pack(side="right")

    return search_result

    

