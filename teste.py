import tkinter as tk


class TelaControleGastos:
    def __init__(self, master):
        self.master = master
        master.title("Controle de Gastos")

        # Criação dos widgets
        self.label_titulo = tk.Label(
            master, text="Controle de Gastos", font=("Arial", 16)
        )
        self.label_titulo.pack(pady=10)

        self.label_descricao = tk.Label(master, text="Descrição:")
        self.label_descricao.pack()

        self.entry_descricao = tk.Entry(master)
        self.entry_descricao.pack()

        self.label_valor = tk.Label(master, text="Valor:")
        self.label_valor.pack()

        self.entry_valor = tk.Entry(master)
        self.entry_valor.pack()

        self.button_adicionar = tk.Button(
            master, text="Adicionar", command=self.adicionar_despesa
        )
        self.button_adicionar.pack(pady=10)

        self.listbox_despesas = tk.Listbox(master)
        self.listbox_despesas.pack()

        self.button_editar = tk.Button(
            master, text="Editar", command=self.editar_despesa
        )
        self.button_editar.pack(pady=10)

        self.button_excluir = tk.Button(
            master, text="Excluir", command=self.excluir_despesa
        )
        self.button_excluir.pack()

        self.label_total = tk.Label(master, text="Total de Gastos: R$ 0,00")
        self.label_total.pack(pady=10)

    def adicionar_despesa(self):
        descricao = self.entry_descricao.get()
        valor = float(self.entry_valor.get())

        self.listbox_despesas.insert(tk.END, f"{descricao} - R$ {valor:.2f}")

        self.entry_descricao.delete(0, tk.END)
        self.entry_valor.delete(0, tk.END)

        self.atualizar_total()

    def editar_despesa(self):
        selecionado = self.listbox_despesas.curselection()

        if selecionado:
            descricao_antiga, valor_antigo = self.listbox_despesas.get(
                selecionado[0]
            ).split(" - ")
            valor_antigo = float(valor_antigo[3:])

            self.entry_descricao.insert(0, descricao_antiga)
            self.entry_valor.insert(0, valor_antigo)

            self.listbox_despesas.delete(selecionado[0])

            self.atualizar_total()

    def excluir_despesa(self):
        selecionado = self.listbox_despesas.curselection()

        if selecionado:
            self.listbox_despesas.delete(selecionado[0])

            self.atualizar_total()

    def atualizar_total(self):
        total = sum(
            float(self.listbox_despesas.get(i).split(" - ")[1][3:])
            for i in range(self.listbox_despesas.size())
        )

        self.label_total.config(text=f"Total de Gastos: R$ {total:.2f}")


root = tk.Tk()
tela = TelaControleGastos(root)
root.mainloop()
