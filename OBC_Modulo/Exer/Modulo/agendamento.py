import os
### Agendamento de desligamento

#Crie duas funções em python para agendar o desligamento do computador em uma hora e meia hora.
def desg_1_hora():
    os.system('shutdown -s -t 3600') # Agendar desligamento em 1HR

def desg_30_min():
    os.system('shutdown -r -t 1800') # Agendar desligamento em 30 minutos

def cancel_desg():
    os.system('shutdown -a') # cancelar agendamento
    
def close():
    os.system('cls') # Limpar tela