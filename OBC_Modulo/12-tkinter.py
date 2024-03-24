import tkinter as tk

# 1 - Criando Janela
window = tk.Tk()
window.geometry("360x150")
window.title("Gerenciamento de frases")

# 2 - Adicionando o frame
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x', expand=True)

# 3 - Adicionando o Label
label = tk.Label(frame, text="Hello, World")
label.pack(fill='x', expand=True)

# 4 - Adicionando o input text
frases_lab = tk.Label(frame, text="frase")
frases_lab.pack(fill='x', expand=True)

frase_inp = tk.Entry(frame)
frase_inp.pack(fill='x', expand=True)

# 5 - Funcao para alterar o texto do label
def click():
    label.config(text=frase_inp.get)

# 5 - Adicionando botao
button = tk.Button(frame, text="Enviar")
button.pack()

window.mainloop()