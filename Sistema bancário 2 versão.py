import sys

limite = 500

home_conta = """
[d] depositar
[s] sacar
[e] extrato
[q] sair
"""

nomes = []
senhas = []
saldo = []
ns = []
nd = []

def criar_conta(nomes, senhas, saldo, ns, nd):
    nome = input("Cadastre o seu nome: ")
    nomes.append(nome)
    
    senha = input("Digite a sua senha: ")
    verify_senha = input("Repita a sua senha: ")
    
    while senha != verify_senha:
        verify_senha = input("As senhas não correspondem. Repita a mesma senha ou se desejar parar digite 'p': ")
        if verify_senha == "p":
            nomes.pop()
            return
    
    senhas.append(senha)
    saldo.append(0)
    ns.append(0)
    nd.append(0)

def sacar(u_id):
    valor = float(input("Digite o valor para saque: "))
    
    if valor > saldo[u_id]:
        print("O valor excedeu o saldo.")
    elif valor > limite:
        print("O limite para saque é 500 reais.")
    elif ns[u_id] >= 4:
        print("O limite de números de saques se esgotou.")
    else:
        saldo[u_id] -= valor
        ns[u_id] += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

def depositar(u_id):
    valor = float(input("Digite o valor para depósito: "))
    
    if valor > 0:
        saldo[u_id] += valor
        nd[u_id] += 1
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("O depósito falhou. Tente novamente.")

def extrato(u_id):
    print("\n================ EXTRATO ================")
    print(f"Saldo: R$ {saldo[u_id]:.2f}")
    print(f"Número de saques: {ns[u_id]}")
    print(f"Número de depósitos: {nd[u_id]}")
    print("==========================================")

while True:
    opcao = input("Para acessar sua conta digite 'A', para se cadastrar digite 'C' ou digite 'sair': ")
    
    if opcao == "C":
        criar_conta(nomes, senhas, saldo, ns, nd)
    elif opcao == "A":
        usuario = input("Digite seu nome: ")
        senha_temp = input("Digite sua senha: ")
        
        if usuario in nomes:
            u_id = nomes.index(usuario)
            if senha_temp == senhas[u_id]:
                print(home_conta)
                
                while True:
                    opcao = input("Digite sua operação: ")
                    if opcao == "s":
                        sacar(u_id)
                    elif opcao == "d":
                        depositar(u_id)
                    elif opcao == "e":
                        extrato(u_id)
                    elif opcao == "q":
                        break
                    else:
                        print("Operação não encontrada.")
            else:
                print("Senha incorreta.")
        else:
            print("Usuário não encontrado.")
    elif opcao == "sair":
        sys.exit()
    else:
        print("Operação não encontrada.")
