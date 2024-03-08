import tkinter as tk
from tkinter import messagebox
import xml.etree.ElementTree as ET


class Gasto:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor


class ControleGastos:
    def __init__(self):
        self.gastos = []

    def adicionar_gasto(self, descricao, valor):
        gasto = Gasto(descricao, valor)
        self.gastos.append(gasto)

    def excluir_gasto(self, index):
        if index >= 0 and index < len(self.gastos):
            del self.gastos[index]

    def editar_gasto(self, index, descricao, valor):
        if index >= 0 and index < len(self.gastos):
            self.gastos[index].descricao = descricao
            self.gastos[index].valor = valor

    def calcular_total(self):
        total = 0
        for gasto in self.gastos:
            total += gasto.valor
        return total

    def exportar_para_xml(self, nome_arquivo):
        root = ET.Element("gastos")
        for gasto in self.gastos:
            gasto_element = ET.SubElement(root, "gasto")
            descricao_element = ET.SubElement(gasto_element, "descricao")
            descricao_element.text = gasto.descricao
            valor_element = ET.SubElement(gasto_element, "valor")
            valor_element.text = str(gasto.valor)

        tree = ET.ElementTree(root)
        tree.write(nome_arquivo)


class InterfaceGrafica:
    def __init__(self, controle_gastos):
        self.controle_gastos = controle_gastos

        self.janela = tk.Tk()
        self.janela.title("Controle de Gastos")

        self.descricao_label = tk.Label(self.janela, text="Descrição:")
        self.descricao_label.pack()

        self.descricao_entry = tk.Entry(self.janela)
        self.descricao_entry.pack()

        self.valor_label = tk.Label(self.janela, text="Valor:")
        self.valor_label.pack()

        self.valor_entry = tk.Entry(self.janela)
        self.valor_entry.pack()

        self.adicionar_button = tk.Button(
            self.janela, text="Adicionar", command=self.adicionar_gasto
        )
        self.adicionar_button.pack()

        self.excluir_button = tk.Button(
            self.janela, text="Excluir", command=self.excluir_gasto
        )
        self.excluir_button.pack()

        self.editar_button = tk.Button(
            self.janela, text="Editar", command=self.editar_gasto
        )
        self.editar_button.pack()

        self.listbox = tk.Listbox(self.janela)
        self.listbox.pack()

        self.total_label = tk.Label(self.janela, text="Total: R$")
        self.total_label.pack()

        self.exportar_button = tk.Button(
            self.janela, text="Exportar para XML", command=self.exportar_para_xml
        )
        self.exportar_button.pack()

        self.atualizar_listbox()

        self.janela.mainloop()

    def adicionar_gasto(self):
        descricao = self.descricao_entry.get()
        valor = float(self.valor_entry.get())

        self.controle_gastos.adicionar_gasto(descricao, valor)
        self.atualizar_listbox()
        self.atualizar_total()

        self.descricao_entry.delete(0, tk.END)
        self.valor_entry.delete(0, tk.END)

    def excluir_gasto(self):
        index = self.listbox.curselection()
        if index:
            self.controle_gastos.excluir_gasto(index[0])
            self.atualizar_listbox()
            self.atualizar_total()

    def editar_gasto(self):
        index = self.listbox.curselection()
        if index:
            descricao = self.descricao_entry.get()
            valor = float(self.valor_entry.get())

            self.controle_gastos.editar_gasto(index[0], descricao, valor)
            self.atualizar_listbox()
            self.atualizar_total()

    def atualizar_listbox(self):
        self.listbox.delete(0, tk.END)
        for gasto in self.controle_gastos.gastos:
            self.listbox.insert(tk.END, f"{gasto.descricao} - R${gasto.valor}")

    def atualizar_total(self):
        total = self.controle_gastos.calcular_total()
        self.total_label.config(text=f"Total: R${total}")

    def exportar_para_xml(self):
        nome_arquivo = tk.filedialog.asksaveasfilename(defaultextension=".xml")
        if nome_arquivo:
            self.controle_gastos.exportar_para_xml(nome_arquivo)
            messagebox.showinfo("Exportar para XML", "Dados exportados com sucesso!")


controle_gastos = ControleGastos()
interface_grafica = InterfaceGrafica(controle_gastos)
