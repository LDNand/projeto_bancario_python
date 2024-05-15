'''
 ============================================================================
 Name        : Projeto bancario V1
 Author      : Andrew Alex Pereira
 Description : projeto em python simulando aplicativo bancario
 ============================================================================
'''

saldo = 1000
cheque_especial = 10000
limite_saque = 500
limite_saque_diario = 3
historico_saque = []
historico_desposito = []

operacao_invalida = "Numero da operacao invalido !!!"
texto_saldo = f"Saldo disponivel R${saldo}"
texto_cheque_especial = f"Valor disponivel do cheque especial R${cheque_especial}"
saudacao_final = "Obrigado por estar conosco !!"

menu_extrato_deposito = f"Deposito: R${historico_desposito}"
menu_extrato_saque = f"Saque: R${historico_saque}"

menu_retorno = """ 
=============== MENU ===============

    [1] Voltar ao menu inicial
    [2] Sair

====================================
"""

while True: 
    menu_principal = f"""
    =============== MENU ===============

        saldo R${saldo}
        Cheque especial R${cheque_especial}

        [1] Sacar
        [2] Depositar
        [3] Extrato
        [4] Sair

    ====================================

    """
    print (menu_principal)
    opcao = int(input("Digite o numero da operacao: ")) 

    # saque
    if opcao == 1:
        limite_saque_diario = limite_saque_diario - 1

        if limite_saque_diario > 0:
            saque = float(input("valor do saque: "))
            historico_saque.append (saque)

            if saque <= limite_saque:
                novo_saldo = saldo - saque

                texto_saque = f"Valor sacado R${saque}"
                texto_novosaldo = f"Saldo disponivel R${novo_saldo}"
                
                if saldo >= saque:
                    
                    saldo = saldo - saque
                    texto_saldo = f"Saldo disponivel R${saldo}"

                    print ("sacando o valor... ")
                    print (texto_saque) 
                    print (texto_saldo)

                    print (menu_retorno)
                    retorno = int(input("Digite o numero da operacao: "))
                    
                    if retorno == 1:
                        print("Processando...")

                    elif retorno == 2:
                        print ("Saindo... ")
                        break

                    else:
                        print (operacao_invalida)
                        break
                    

                elif saque <= (novo_saldo + cheque_especial):

                    if novo_saldo < 0:
                        saldo = 0
                        novo_saldo = novo_saldo * -1
                        cheque_especial = cheque_especial - novo_saldo

                        texto_saldo = f"Saldo disponivel R${saldo}"
                        texto_cheque_especial = f"Valor do cheque especial disponivel R${cheque_especial}"

                        print ("sacando o valor... ")
                        print (texto_saque)
                        print (texto_saldo)

                        print (menu_retorno)
                        retorno = int(input("Digite o numero da operacao: "))
                        
                        if retorno == 1:
                            print("Processando...")

                        elif retorno == 2:
                            print ("Saindo... ")
                            break

                        else:
                            print (operacao_invalida)
                            break
                    
                else:
                    print ("saldo insuficiente...")

                    print (menu_retorno)
                    retorno = int(input("Digite o numero da operacao: "))
                    
                    if retorno == 1:
                        print("Processando...")

                    elif retorno == 2:
                        print ("Saindo... ")
                        break

                    else:
                        print (operacao_invalida)
                        break

            else:
                print ("Valor de saque acima do permitido! ")

                print (menu_retorno)
                retorno = int(input("Digite o numero da operacao: "))
                
                if retorno == 1:
                    print("Processando...")

                elif retorno == 2:
                    print ("Saindo... ")
                    break

                else:
                    print (operacao_invalida)
                    break

        else:
            print ("limite de saque alcancado !")
            
            print (menu_retorno)
            retorno = int(input("Digite o numero da operacao: "))
            
            if retorno == 1:
                print("Processando...")

            elif retorno == 2:
                print ("Saindo... ")
                break

            else:
                print (operacao_invalida)
                break
        
    #desposito
    elif opcao == 2:
        deposito = float(input("Valor desejado para deposito: "))
        historico_desposito.append (deposito)
        texto_deposito = f"Valor depositado com sucesso R${deposito}"


        if deposito >= 0:
            print (texto_deposito)
            saldo = deposito + saldo

            texto_saldo = f"Saldo disponivel R${saldo}"
            print (texto_saldo)
            
            print (menu_retorno)
            retorno = int(input("Digite o numero da operacao: "))
            
            if retorno == 1:
                print("Processando...")

            elif retorno == 2:
                print ("Saindo... ")
                break

            else:
                print (operacao_invalida)
                break

        else:
            print ("Valor de deposito invalido!")
            
            print (menu_retorno)
            retorno = int(input("Digite o numero da operacao: "))
            
            if retorno == 1:
                print("Processando...")

            elif retorno == 2:
                print ("Saindo... ")
                break

            else:
                print (operacao_invalida)
                break
            
    #extrato
    elif opcao == 3:

        print ("exibindo extrato... ")
        print (texto_saldo)
        print (texto_cheque_especial)

        for valor_deposito in historico_desposito:
            print (f"Deposito: R${valor_deposito:.2f}")

        for valor_saque in historico_saque:
            print (f"Saque: R${valor_saque: .2f}")

        print (menu_retorno)
        retorno = int(input("Digite o numero da operacao: "))
        
        if retorno == 1:
            print("Processando...")

        elif retorno == 2:
            print ("Saindo... ")
            break

        else:
            print (operacao_invalida)
            break

    #sair
    elif opcao == 4:
        break

    else:
        print (operacao_invalida)

exit (saudacao_final)
