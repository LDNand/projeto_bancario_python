'''
 ============================================================================
 Name        : Projeto bancario V2
 Author      : Andrew Alex Pereira
 Description : projeto em python simulando aplicativo bancario
 ============================================================================
'''
cpf_list = [1]
def invalid_enter ():
    print ("comando invalido\n")
    print ("saindo... ")
def register_menu ():
    layout_menu = f'''
    ================ MENU ================
    
    Deseja realizar o cadastro?\n 
    [y/n]:
    ======================================
    '''
    return layout_menu
def out_menu ():

    layout_menu = input (f'''
    ================ MENU ================
    
    Deseja sair? \n
    [y/n]:
    ======================================
    ''')
    if layout_menu == 'y':
        print("saindo...")
        return True
    elif layout_menu == 'n':
        print("voltando ao menu...")
        return False
def new_account ():
    while True:
        cpf = int(input("Digite seu CPF: "))
        if cpf in cpf_list:
            print (f"Seu CPF: {cpf}")
        else:
            print(register_menu())
            register = (input())
            register.lower()
            if register == 'y':
                cpf_list.append (cpf)
                is_out = out_menu()
                if is_out == True:
                    break
                else:
                    print ("menu")
            elif register == 'n': 
                print ("voltando...")
            else:
                invalid_enter()
new_account()