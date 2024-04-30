
# # Exercício 1
# ## Lendo n linhas de um arquivo
# Escreva um programa Python para ler as primeiras n linhas de um arquivo.
# 1. O nome do arquivo e a quantidade de linhas devem ser passadas via parâmetro na função.

"""
-Arquivos:

'r': modo de leitura, o arquivo deve existir previamente
'w': modo de escrita, se o arquivo não existir, ele será criado
'a': modo de anexar, adiciona informações ao final do arquivo
'x': modo exclusivo, cria um novo arquivo somente se ele não existir
'b': modo binário, usado para arquivos binários, como imagens ou vídeos
't': modo de texto, usado para arquivos de texto

"""
arq = open("exer1.txt", "rt", encoding="utf-8")
file = arq.read(31).strip()
linhas = len(arq.readlines())
print(f"O nome do arquivo é: {__file__} \n a quantidade de linhas: {linhas}")


# Codigo do professor
# #def file_read_from_line(fname, nlines):
#         from itertools import islice
#         with open(fname, encoding="utf-8") as f:
#                 for line in islice(f, nlines):
#                         print(line)
# file_read_from_line('texto.txt',1)
        
