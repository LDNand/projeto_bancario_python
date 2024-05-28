cashout_times = 3
balance = 1000.00

balance_text = f"Balance: ${balance}\n"

def cashout_limit ():
    global cashout_times
    cashout_times -= 1
    return cashout_times

def balance_withdrawn (cashout):
    global balance
    balance -= cashout
    return balance

def main_menu ():
    while True:
        main_layout = f"""
        =============== MENU ===============

        Balance: ${balance}

        [1] Sacar
        [2] Depositar
        [3] Extrato
        [4] Sair

        ====================================
        """
    
        print (main_layout)
        choice = int(input("Digite o numero da operacao: "))

        if choice == 1:
            remaining_cashout = cashout_limit()

            if remaining_cashout < 0:
                print("fim...")
                break
            else:
                cashout = float(input("Digite o valor do saque: "))
                balance_withdrawn (cashout)
                print (f"Novo saldo: ${balance}") 
main_menu ()