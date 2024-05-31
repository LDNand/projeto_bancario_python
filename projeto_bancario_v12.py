'''
 ============================================================================
 Name        : Projeto bancario V1.1
 Author      : Andrew Alex Pereira
 Description : projeto em python simulando aplicativo bancario
 ============================================================================
'''
cashout_times = 3
balance = 1000.00
limit = 500
extract = []
accounts = []

def account_menu ():
    while True:
        account_menu_confirmation = int(input(f'''
    =============== MENU ===============
                                              
        Already a user?
        [1] Login
        [2] Register
                                                                                                        
    ====================================                                
            '''))
        if account_menu_confirmation == 1:
            cpf = int(input ("Enter your CPF: "))
            if cpf in accounts:
                print (f"Your CPF is: {cpf}")
                return True
            else:
                print ("Your CPF was not registered")
        if account_menu_confirmation == 2:
            creat_account ()
            return True

def creat_account ():
    cpf = int(input ("Tipe your CPF: "))
    accounts.append (cpf)
    
def out_menu ():
    while True:
        out_menu_layout = int(input(f"""
=============== MENU ===============

    Return to main menu
    [1] Yes
    [2] No

====================================
        """))
        if out_menu_layout == 1:
            return True
        elif out_menu_layout == 2:
            return False
        else:
            print ("Insert a valid option")
    
def cashout_limit ():
    global cashout_times
    cashout_times -= 1
    return cashout_times

def balance_deposit (cashin):
    global balance
    balance += cashin
    print (f"New balance: ${balance}")
    extract.append (cashin)

def balance_withdrawal (cashout):
    global balance

    if balance < cashout:
        print("insufficient funds")
        return
    else:
        balance -= cashout
        cashout *= -1
        extract.append (cashout)
        return balance
    

def main_menu ():
    global balance
    global limit

    if account_menu ():

        while True:
            main_menu_layout = f"""
    =============== MENU ===============

        [1] Cashout
        [2] Cashin
        [3] bank statement
        [4] Exit

    ====================================
            """
        
            print (main_menu_layout)
            choice = int(input("Tipe the number of the operation: "))

            if choice == 1:
                remaining_cashout = cashout_limit()

                if remaining_cashout < 0:
                    print("Maximum number of operations reached")
                    
                    if out_menu ():
                        print ("Return to the main menu")
                    else:
                        print ("Exit")
                        break
                else:
                    cashout = float(input("Enter the withdrawal amount: "))
                    
                    if cashout > limit:
                        print ("withdrawal amount exceeds limit")

                        if out_menu ():
                            print ("return to main menu... ")
                        else:
                            print ("exit")
                    else: 
                        balance_withdrawal (cashout)
                        print (f"New balance: ${balance}")

                        if out_menu():
                            print ("Return to the main menu")
                        else:
                            print ("Exit")
                            break
            elif choice == 2:
                cashin = float(input("Desired deposit amount: "))
                balance_deposit (cashin)

                if out_menu ():
                    print ("return to main menu... ")
                else:
                    print ("exit")
            elif choice == 3:
                print ("Bank statemant")
                for operation in extract:
                    print (f"Operation ${operation:.2f}")
                if out_menu():
                        print ("Return to the main menu... ")
                else:
                    print ("Exit")
                    break
            elif choice == 4:
                print ("exit")
                break   
            else:
                print ("Invalid option")
    else:
        print ("Error")
main_menu ()