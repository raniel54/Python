### Agendamento de desligamento

#Crie duas funções em python para agendar o desligamento do computador em uma hora e meia hora.

import os
import sys
done = False
while not done:
    # Opção no programa
    print("O que voce deseja fazer?")
    print("1. Agendar desligamento em 1HR")
    print("2. Agendar desligamento em 30 minutos")
    print("3. cancelar agendamento")
    print("4. Sair")
    
    
    choice = input (">")
    if choice == "1":
        os.system('shutdown -s -t 3600') # Agendar desligamento em 1HR
        print("Seu agendamento foi programado para 1HR")
    elif choice == "2":
        os.system('shutdown -r -t 1800') # Agendar desligamento em 30 minutos
        print("Seu agendamento foi programado para 30 minutos")
    elif choice == "3":
        os.system('shutdown -a') # cancelar agendamento
        print("Seu agendamento foi cancelado")
    elif choice == "4":
        sys.exit()
        
 
