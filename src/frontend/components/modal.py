from enum import Enum
import tkinter as tk

from src.frontend.constants.colors import MODALS_BACKGROUND
from src.frontend.utils.positions import get_center

class ModalTypes(Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"

def main(master: tk.Tk, title: str, message: str, type: ModalTypes):
    popup = tk.Toplevel(master)
    popup.geometry(get_center(master))
    popup.configure(bg="#FFB800")  # Define o fundo amarelo
    popup.overrideredirect(True)  # Remove a barra de título

    # Criando um frame para a caixa de diálogo
    frame = tk.Frame(popup, bg="#FFB800", bd=0)  # Removendo a borda
    frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=200)  # Aumentando o tamanho do popup

    # Rótulo de texto
    label = tk.Label(
        frame,
        text=message,
        font=("Arial", 14, "bold"),  # Aumentando o tamanho da fonte
        bg="#FFB800",
        fg="white"
    )
    label.pack(pady=20)
    
    if type == ModalTypes.ERROR:

        btn_sair = tk.Button(
            frame,
            text="Sair",
            font=("Arial", 12),  # Aumentando o tamanho da fonte
            bg="white",
            fg="black",
            width=20,
            command=master.quit
        )
        btn_sair.pack(pady=10)

        btn_cancelar = tk.Button(
            frame,
            text="Cancelar",
            font=("Arial", 12),  # Aumentando o tamanho da fonte
            bg="lightgray",
            fg="black",
            width=20,
            command=popup.destroy  # Corrigido para fechar o popup
        )
        btn_cancelar.pack(pady=10)
        
    else:
        btn_ok = tk.Button(
            frame,
            text="OK",
            font=("Arial", 12),  # Aumentando o tamanho da fonte
            bg="white",
            fg="black",
            width=20,
            command=popup.destroy
        )
        btn_ok.pack(pady=10)