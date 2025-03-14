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
    popup.configure(bg=MODALS_BACKGROUND.get("yellow"))  # Define o fundo amarelo
    popup.overrideredirect(True)  # Remove a barra de título

    # Criando um frame para a caixa de diálogo
    frame = tk.Frame(
        popup, 
        bg=MODALS_BACKGROUND.get("yellow"), 
        bd=2, 
        border=0, 
        relief="ridge"
    )
    frame.place(relx=0.5, rely=0.5, anchor="center", width=250, height=150)

    # Rótulo de texto
    label = tk.Label(
        frame,
        text="Você tem certeza\nque deseja sair?",
        font=("Arial", 12, "bold"),
        bg=MODALS_BACKGROUND.get("yellow"),
        fg="white"
    )
    label.pack(pady=15)

    btn_sair = tk.Button(
        frame,
        text="Sair",
        font=("Arial", 10),
        bg="white",
        fg="black",
        width=20,
        command=master.quit
    )
    btn_sair.pack(pady=5)

    btn_cancelar = tk.Button(
        frame,
        text="Cancelar",
        font=("Arial", 10),
        bg="lightgray",
        fg="black",
        width=20,
        command=popup.destroy  # Corrigido para fechar o popup
    )
    btn_cancelar.pack(pady=5)