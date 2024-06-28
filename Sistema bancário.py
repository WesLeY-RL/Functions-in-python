
limite = 500
home_conta = """
[d] depositar
[s] sacar
[e] extrato
[q] sair
"""
contas = {
    "Nomes": nomes,
    "Senhas": senhas,
    "Saldo": saldo,
    "Número de saques": ns,
    "Número de depósitos": nd
}
nomes = []
senhas = []
saldo = []
ns = []
nd = []

while True:
    opcao = str(input("Para acessar sua conta digite A, para se cadastrar digite C ou digite sair"))
    if opcao =="C" :
        def criar_conta(nomes,senhas, saldo, ns, nd):
            
            #criação dos nomes
            
            nome = str(input("Cadastre o seu nome: "))
            nomes.append(nome)
            
            #criaçãos das senhas
            v = True
            senha = str(input("Digite a sua senha: "))
            verify_senha = str(input("repita a sua senha: "))
            while senha != verify_senha and v == True:
                verify_senha = (str(input("Repita a mesma senha ou se desejar parar digite p :")))
                if verify_senha == "p":
                    v = False
            senhas.append(senha)
            
            #criação dos saldos, numeros de saques e de depósitos

            saldo.append(0)
            ns.append(0)
            nd.append(0)
            
    elif opcao == "A":
        
        acesso = True
        
        while acesso == True:
            
            usuario = str(input("Digite seu nome: "))
            senha_temp = str(input("digite sua senha: "))
            u_id = 0
            s_id = 0
            for i in range(0,len(nomes)):
                if usuario == nomes[i]:
                    u_id = i
            for j in range(0, len(senhas)):
                if senha_temp == senhas[j]:
                    s_id = j
            if u_id == s_id:
                
                print(home_conta)
                
                while True:
                    opcao = input("digite sua operação: ")
                    if opcao == "s" :
                        sacar(saldo[u_id],limite, ns[u_id])
                        
                    elif opcao == "d":
                        depositar(saldo[u_id])
                    
                    elif opcao == "e":
                        extrato(u_id)
                    elif opcao == "q":
                        break
                    else:
                        print("operação não encontrado")
            else:
                print("conta não encontrada")
                desire = str(input("deseja parar: "))
                if desire == "sim":
                    acesso = False
    
    elif opcao == "sair":
        break
    else:
        print("operação não encontrada")

def sacar(saldo,limite,ns):

    valor = float(input("Digite o valor para saque: "))
    if valor > saldo:
        print(" O valor excedeu o saldo")
            
    elif valor > limite: 
        print("O limite para saque é 500 reais.")
    elif ns == 4 :
        print("o limite de números de saques se esgotou.")
    else:
        saldo = saldo - valor
        ns = ns + 1
        
def depositar(saldo):
    
    if valor > 0:
        saldo = saldo + valor
        np = np + 1
    else:
        print("O depósito falhou tente novamente.")

def extratro(id):
    
    print("\n================ EXTRATO ================")
    print(f"\nNúmero de depósitos: {nd[id]:.2f}")
    print(f"\nNúmero de saques: {ns[id]:.2f}")
    print(f"\nSaldo: R$ {saldo[id]:.2f}")
    print("==========================================")