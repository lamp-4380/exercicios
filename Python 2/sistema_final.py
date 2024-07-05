import time
nomes = ["Marcos", "Filipe"]
senhas = [1234, 4321]
produtos = ["Celular","Mouse","Monitor"]
nprodutos = [50,60,30]
cod = [0,1,2]
desc = ["Dispositivo móvel mais utilizado ultimamente","Dispositivo mais dinâmico para controlar o cursor do computador",\
        "Dispositivo que mostra a tela do computador"]
admmsg = []
while True:
    nomeu = input("Escreva seu nome: ")
    senhau = int(input("Escreva sua senha: "))
    if nomeu == "Marcos" and senhau == 1234:
        print("Entrando...")
        while True:
            
            time.sleep(1)
            d = int(input("Digite um número para o que você quer fazer:\n1)Diminuir quantidade de produtos;\
                          \n2)Aumentar quantidade de produtos;\n3)Adicionar novo produto;\n4)Pedir envio de produtos;\n0)Sair.\nDigite Aqui: "))
            if d == 1:
                print("Processando...")
                time.sleep(1)
                print("Escreva o número do produto a ser modificado: ")
                for i,j in enumerate(produtos):
                    print(i,j)
                d1 = int(input("Digite Aqui: "))
                print("Processando...")
                time.sleep(1)
                print(produtos[d1], "\nDescrição: ",desc[d1],"\nQuantia Atual: ", nprodutos[d1],"\nCódigo: ", cod[d1])
                qr = int(input("Digite quantas unidades serão retiradas: "))
                print("Processando...")
                time.sleep(1)
                if nprodutos[d1] >= qr:
                    qt = nprodutos[d1] - qr 
                    nprodutos.insert(d1,qt)
                    print("Quantia retirada! Voltando à tela inicial...")
                    time.sleep(0.5)
                else:
                    print("Não há produtos suficientes... Retornando à tela inicial.")
                time.sleep(0.5)
            elif d == 2:
                print("Processando...")
                time.sleep(1)
                print("Escreva o número do produto a ser modificado: ")
                for i,j in enumerate(produtos):
                    print(i,j)
                d1 = int(input("Digite Aqui: "))
                print("Processando...")
                time.sleep(1)
                print(produtos[d1], "\nDescrição: ",desc[d1],"\nQuantia Atual: ", nprodutos[d1],"\nCódigo: ", cod[d1])
                qa = int(input("Digite quantas unidades serão adicionadas: "))
                print("Processando...")
                time.sleep(1)
                qt = qa + nprodutos[d1]
                nprodutos.insert(d1,qt)
                print("Quantia Adicionada! Voltando à tela inicial...")
                time.sleep(0.5)
            elif d == 3:
                np = input("Escreva o nome do novo produto: ")
                produtos.append(np)
                print("Processando...")
                time.sleep(1)
                dp = input("Agora, escreva a descrição do produto: ")
                desc.append(dp)
                print("Processando...")
                time.sleep(1)
                qp = int(input("Agora, escreva a quantia atual do produto: "))
                nprodutos.append(qp)
                print("Processando...")
                time.sleep(1)
                cp = int(input("Agora, escreva o código do produto: "))
                cod.append(cp)
                print("Processando...")
                time.sleep(1)
                print("Produto adicionado! Indo para a tela inicial...")
                time.sleep(0.5)
            elif d == 4:
                msg = input("Escreva a mensagem ao ADM: ")
                admmsg.append(msg)
                print("Mensagem enviada! Retornando à tela inicial...")
                time.sleep(0.5)
            elif d == 0:
                p = False
                break
    elif nomeu == "Filipe" and senhau == 4321:
        print("Entrando...")
        time.sleep(1)
        while True:
            
            time.sleep(1)
            d = int(input("Digite um número para o que você quer fazer:\n1)Modificar quantidade de produtos;\
                          \n2)Modificar usuários;\n3)Adicionar novo produto;\n4)Verificar Pedidos de Produtos;\n0)Sair.\nDigite Aqui: "))
            if d == 1:
                print("Processando...")
                time.sleep(1)
                print("Escreva o número do produto a ser modificado: ")
                for i,j in enumerate(produtos):
                    print(i,j)
                d1 = int(input("Digite Aqui: "))
                print("Processando...")
                time.sleep(1)
                print(produtos[d1], "\nDescrição: ",desc[d1],"\nQuantia Atual: ", nprodutos[d1],"\nCódigo: ", cod[d1])
                time.sleep(0.1)
                ae = int(input("Você quer adicionar(1) ou excluir(2)? "))
                if ae == 1:
                    qr = int(input("Digite quantas unidades serão retiradas: "))
                    print("Processando...")
                    time.sleep(1)
                    if nprodutos[d1] >= qr:
                        qt = nprodutos[d1] - qr
                        nprodutos.insert(d1,qt)
                        print("Quantia retirada! Voltando à tela inicial...")
                        time.sleep(0.5)
                    else:
                        print("Não há produtos suficientes... retornando à tela inicial.")
                    time.sleep(0.5)
                elif ae == 2:
                    qa = int(input("Digite quantas unidades serão adicionadas: "))
                    print("Processando...")
                    time.sleep(1)
                    qt = qa + nprodutos[d1]
                    nprodutos.insert(d1,qt)
                    print("Quantia Adicionada! Voltando à tela inicial...")
                    time.sleep(0.5)
                else:
                    print("Resposta inválida. Retornando à tela inicial...")
                    time.sleep(0.5)
            elif d == 2:
                print("Processando...")
                time.sleep(1)
                ae = int(input("Você quer adicionar(1) ou Excluir(2) algum usuário? "))
                if ae == 1:
                    nuser = input("Escreva o nome do novo usuário: ")
                    nomes.append(nuser)
                    print("Processando...")
                    time.sleep(1)
                    ns = input("Agora, escreva a senha dele: ")
                    senhas.append(ns)
                    print("Processando...")
                    time.sleep(1)
                    print("Usuário adicionado! Indo para a tela inicial...")
                    time.sleep(0.5)
                elif ae == 2:
                    print("Processando...")
                    time.sleep(1)
                    print("Escreva o número do usuário a ser modificado: ")
                    for i,j in enumerate(nomes):
                        print(i,j)
                    d1 = int(input("Digite Aqui: "))
                    print("Processando...")
                    time.sleep(1)
                    print("Nome: ", nomes[d1])
                    d2 = input("Você tem certeza dessa ação(s ou n)? ")
                    print("Processando...")
                    time.sleep(1)
                    if d2 == "s":
                        nomes.remove(nomes[d1])
                        senhas.remove(senhas[d1])
                        print("Usuário removido! Retornando à tela inicial...")
                        time.sleep(0.5)
                    elif d2 == "n":
                        print("Ação cancelada. Retornando à tela inicial...")
                        time.sleep(0.5)
            elif d == 3:
                np = input("Escreva o nome do novo produto: ")
                produtos.append(np)
                print("Processando...")
                time.sleep(1)
                dp = input("Escreva a descrição do produto: ")
                desc.append(dp)
                print("Processando...")
                time.sleep(1)
                qp = int(input("Agora, escreva a quantia atual do produto: "))
                nprodutos.append(qp)
                print("Processando...")
                time.sleep(1)
                cp = int(input("Produto, escreva o código do produto: "))
                cod.append(cp)
                print("Processando...")
                time.sleep(1)
                print("Produto adicionado! Indo para a tela inicial...")
                time.sleep(0.5)
            elif d == 4:
                if len(admmsg) > 0:
                    print("Você recebeu as seguintes mensagens:")
                    for i in admmsg:
                        print(i)
                    ok = input('Digite "ok" ou pressione "Enter" para marcar como lida e voltar à tela inicial: ')
                    print("Mensagens lidas! Retornando à tela inicial...")
                else:
                    print("Não chegaram novas mensagens. Retornando à tela inicial...")
                time.sleep(0.5)
            elif d == 0:
                p = False
                break
    else:
        print("Usuário ou senha inválidos.")