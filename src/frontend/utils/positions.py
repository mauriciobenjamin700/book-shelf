import tkinter as tk

def get_center(frame_container: tk.Frame) -> str:
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