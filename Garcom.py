#Funções:
 
def instruçao(n):
    print("""-----------------------------------------------INSTRUÇÃO-----------------------------------------------
 
Em todas as opções onde você quer escrever você poderá digitar "voltar" e então você voltará para opção anterior
 
 
------------------------AÇÃO------------------------\n
Como primeira opção de execução, você fará uma ação que destinará
seu proximo passo, são eles:
OBS: Você precisa digitar, alguma das opções abaixo de compra/cardapio/terminar/ajuda/excluir/conta, para prosseguir com a ação
Digite tudo corretamente de acordo com as instruções ("Sem espaço a mais, ou qualquer caracter diferente")
 
----------------------comprar-----------------------\n
Nesta etapa você irá escolher quais as opções de refeições que deseja, são elas:
                     |almoço   |
                     |lanche   |
                     |bebidas  |
                     |sobremesa|
 
Quando ele perguntar oque você quer escolher digite uma das opçãoes acima
Na escolha, você optrará o tipo de comida que contém em almoço/lanche/bebida/sobremesa ou poderá digitar:
Voltar
Cardápio
ajuda/help
 
OBS: Na opção de bebida você terá a opção de escolha de vizualizar todo o cárdapio, ou as alcoolicas e não alcoolicas
 
Você escolherá qual dessas opções deseja comprar
Siga todas as instruções para realizar a compra do seu produto
 
Em cada uma delas você receberá o cardápio dos alimentos disponíveis que você deseja comprar\n
 
------------------------cardápio------------------------
Nesta opção você receberá o cardápio completo de todos os alimentos disponíveis do restaurante\n
 
------------------------terminar------------------------
Você encerrará seu pedido, e o programa lhe informará o preço final de todo o seu carrinho de compra\n
 
------------------------ajuda/help------------------------
Você poderá rever todas as instruções deste sistema de ajuda no seu código\n
 
------------------------excluir/apagar------------------------
Nesta opção você poderá excluir algum pedido que você tem feito no seu carrinho
Você escreverá o item da sua lista que você deseja excluir 
Ele também perguntará o cardapio do item, ou seja se o item excluido for um 'Suco', 
ele fará parte de 'bebida', então você digitará  'bebida' se for 'Lasanha', você digitaria almoço\n
 
------------------------conta------------------------
Nesta opção você verá o valor total de sua compra\n
  
""") 
    time.sleep(n)
    
def Encerrar():                                                                 #Função para encerrar programa
    print(f'\n Carrinho do cliente: {Lista_Cliente}')
    print(f'\n Total a pagar R${total:.2f}')
    while True:
        Passar = input('\nSe você deseja continuar com o pedido, pressione "ENTER", ou digite "E" para encerrar a compra: ')
        
        if Passar.lower() == 'e':                                               #Obriga a string minuscula
            print("\nSeja Bem-vindo e volte sempre! ")
            sys.exit(0)
        elif Passar == '':                                                      #Se apertar enter o programa segue
            print('')
            break
        else:                                                                   #Se apertar qualquer outro tecla aleatoria vai perguntar novamente
            continue
 
def cardapio_almoco():
 
    print("---------------------------------------------")
    for a in almoco:                                                            #Percorre a lista do almoço
        print(f"Você pode escolher {a[0]} R${a[1]}")
        print("---------------------------------------------")                  #Mostra as opções do cardapio
 
def alcool():    
 
    print("--------------------------------------------")
    for o,b in bebidas[0].items():
        for i in b:
            print(f"Você pode escolher {i[0]} R${i[1]}")
            print("---------------------------------------------")
 
def naoAlcool():  
    
    print("--------------------------------------------")
    for o,b in bebidas[1].items():                      
        for i in b:
            print(f"Você pode escolher {i[0]} R${i[1]}")
            print("---------------------------------------------")
 
 
def CalcularBebidas():
    global i
    global x
    global n
    global preco
    global total
    global escolha
    global sabor
 
    if x < 2:                                                                   #Tive que criar uma função, para uma verificação mais rápida, sem precisar por 2 for, o jeito que eu econtrei foi este 1
        for k,v in bebidas[x].items():                                          #O x começa com 1, se a bebida não for encontrada, ela voltará pra o while lá em baixo em bebida e retornará com o x valendo 2
            for c in v:
                if c[0] == escolha:
                    if c[0] == 'Suco':                                          #Especialmente para sucos, se a escolha for suco, ela exibirá os sabores
                        print("\n------------------SUCOS DISPONÍVEIS------------------")
                        print("")
                        for su in suco:                                         #Exibição dos sabores dos sucos, que está la listá suco
                            print(f"{su}", end=' | ')
                        print("\n")
                        sabor = input("Você quer o suco de qual sabor: ").title() #Escolha do sabor do suco
                        while True:
                            if sabor in suco:
                                Lista_Cliente.append(c[0] + " De " + sabor)     #Guarda o nome suco + o seu sabor na lista/carrinho do cliente
                                print("")
                                print("--" * 35)
                                print(f'O seu pedido foi {escolha} de {sabor}, e foi adicionado no seu carrinho !')  
                                print("--" * 35)
                                sabor = ''
                                break
                            elif sabor == 'Voltar':
                                break
                            else:
                                sabor = input("Sabor não encontrado, digite novamente: ").title()
                       
                    else: 
                        Lista_Cliente.append(c[0])
                        print("")
                        print("--" * 35)
                        print(f'O seu pedido foi {escolha}, e está adicionado no seu carrinho !')
                        print("--" * 35)
                    
                    if sabor == 'Voltar':                                           #Se o input do sabor receber voltar, o pedido do suco será cancelado
                        print("Pedido cancelado, refaça seu pedido! ")
                        i = 0
                        x = 0
                        n += 1
                        break    
 
                    preco = preco + c[1]                                            #Chama a variavel preço para capturar o preço do alimento escolhido
                    total += preco                                                  #Total que o cliente ira gastar, este total ficará guardado na váriavel
                    preco = 0                                                       #Zera o preço atual para ser usado em outra opção de escolha
                    i = 0                                                           #Zera o i em caso da escolha estar na lista
                    n += 1
                    x = 0 
                    break
                elif escolha not in c[0]:                                           #Se a escolha não estiver na lista acrescenta um i para mandar a mensagem no laço após o for abaixo
                    i+=1
    else:
        print("\nEste alimento não pertence ao cardápio"
        "\nFavor verifique novamente o cardápio e refaça seu pedido")               # Sendo x o dicionario de alcool e sem alcool, ele vai repetir 3 vezes se caso uma bebida...
        n += 1                                                                      #Não estiver na lista, então ele ira chegar neste laço e parar de procurar, enviando a mensagem
 
def cardapio_sobremesas():
    print("---------------------------------------------")
    for a in sobremesas:
        print(f"Você pode escolher: {a[0]} R${a[1]}")
        print("---------------------------------------------")
 
def cardapio_lanche():
    print("---------------------------------------------")
    for l in lanches:
        print(f"Você pode escolher: {l[0]} R${l[1]}")
        print("---------------------------------------------")
 
def help():
    print("""Se quiser parar com alguma escolha ou ação, digite 'voltar'
para encerrar todo seu pedido volte até a ação de o que você quer fazer? e digite 'terminar'
Digite alguma opção que está nas instruções e continue com o pedido""")
 
def verificacaoExclusao():
    global exclusao
    global totalA
    global total
    
    if exclusao == '':
        print('O preço ja foi alterado '
        f'Preço anterior: {totalA:.2f}'
        f' Preço atual: {total:.2f}')
    
    else:
        print("O preço não foi alterado, digite o cárdapio corretamente !")
        
 
 
#Importações:
import time
import sys
 
#Váriaveis:
sabores = ''                                                                        #Variavel usada nos lanches e sobremesas
sabor = ''                                                                          #Variavel usada no suco
preco = 0                                                                           #Está variavel sera usada para pegar o preco dos produtos que o cliente escolheu
total = 0                                                                           #Total da função
totalA = 0                                                                          #Total usado para ver o antigo preço, usado na remoção dos pedidos
i = 0                                                                               #Será utilizado nos for para verificar se o item escolhido contém na lista do cliente
x = 0                                                                               #X para mudar a bebida
n = 0
 
#Listas:
Lista_Cliente = []
 
almoco = ['Carne Grelhada', 60], ['Frango Frito', 50], ['Lasanha',39.99],['Carne De Sol',70],['Peixe',100]
 
bebidas = [
           {'alcoolicas': [['Whisky', 100],['Pitu',40],['Cerveja Brahma' ,10]]},
           {'nao_alcoolicas':[['Coca Cola', 10],['Guarana Antartica',10],['Suco',8]]}
           ]
suco = ['Manga','Goiaba', 'Acerola', 'Caja', 'Caju', 'Abacaxi', 'Maracuja', 'Gengibre Com Acerola']
 
sobremesas = ['Sorvete', 5],['Bolo', 5],['Milk Shake', 10],['Pudim', 7],['Salgado', 3]
sabor_S = ['Chocolate', 'Coco', 'Manga']                                            #SORVETE
sabor_B = ['Chocolate', 'Branco', 'Cenoura']                                        #BOLO
sabor_P = ['Chocolate', 'Morango']                                                  #PUDIM
sabor_M = ['Baumilha', 'Chocolate', 'Morango','Maracuja']                           #MILK SHAKE
salgado = ['Coxinha','Enroladinho','Pao Pizza','Pastel']
 
lanches = ['Hamburguer', 12],['Pizza', 26],['Cachorro Quente', 5],['Bolo' , 5],['Milk shake', 10],['Pudim', 7], ['Salgado', 3] 
 
 
#Primeiro página:
instruçao(5)
 
 
#Segunda Página:
 
while True:
    acao = input("\nEscolha sua próxima ação: ")
    print("Digite voltar para retroceder sua ação")
 
    if acao.lower() == "terminar":                                                  #Terminar o progrma
        Encerrar()                                                                  #Chama a função de encerrar o programa 
    elif acao.lower() == "ajuda" or acao.lower() == "help":
        help()
        instruçao(1)
        continue    
    
    elif acao.lower() == "comprar":                                                 #Atribuir ao pedido do cliente "Almoço,Bebidas..."   
        acessarLista = input("\nDigite qual opção do cardápio você quer acessar: ").lower() #Acesso das listas do cardapio
        
        if acessarLista == 'almoco' or acessarLista == 'almoço':   
            cardapio_almoco()
           
            while True:
                escolha = input("\nDigite a escolha do cárdapio ou alguma ação descrita nas instruções: ").title() #Oque o cliente quer pedir
                
                if escolha == 'Voltar':                                             #Parar de acrescentar pedido 
                    print(f'Carrinho do cliente: {Lista_Cliente}')            
                    break
                elif escolha == "Ajuda" or acao.lower() == "Help":
                    help()
                    continue    
                elif escolha == 'Cardapio':
                    cardapio_almoco()
                    continue
 
                for p in almoco:                                                    #Percorrer lista atras do preço
                    if escolha == p[0]:                                             #Encontra o nome do alimento de acordo com a escolha
                        preco = preco + p[1]                                        #Cria uma variavel preço para capturar o preço do alimento escolhido
                        total += preco                                              #Chama a variavel total e armazena o quanto o cliente gastou até o momento em todos os pedidos feitos 
                        Lista_Cliente.append(p[0])
                        preco = 0                                                   #Zera o preço atual
                        i=0                                                         #Zera o i em caso da escolha estar na lista
                        print("")
                        print("--" * 35)
                        print(f'O seu pedido foi "{escolha}", e está adicionado ao carrinho !')
                        print("--" * 35)
                        break
                    elif escolha not in p[0]:                                       #Se a escolha não estiver na lista acrescenta um i para mandar a mensagem no laço abaixo
                        i+=1                               
                
                if i == len(almoco):                                                #Se o i for igual a quantidade de item da lista do almoço, então o programa fará com que o cliente refaça o pedido
                    print("\nEste alimento não pertence ao cardápio"
                    "\nFavor verifique novamente o cardápio e refaça seu pedido")
                    i = 0                                                           #Zera o i para o proximo pedido se entrar neste laço
                    continue 
 
 
        elif acessarLista == 'bebidas' or acessarLista == 'bebida':
            while True:
                alcool_naoAlcool = input("\nEscolha a opção de cárdapio para vizualizar\n" 
                "bebidas Alcoolicas ou nao Alcoolicas\n" 
                "ou digite completo para ver as 2 opções: ").lower()                #Escolha de opções de bebidas que você quer escolher
 
                if alcool_naoAlcool == 'alcoolicas':
                    alcool()                                                        #Chama a função do cardapio alcool
                
                elif alcool_naoAlcool == 'nao alcoolicas':
                    naoAlcool()                                                     #Chama a função das bebidas sem alcool
                
                elif alcool_naoAlcool == 'completo':                                #Mostrar as bebidas alcoolicas e não alcoolicas
                    print("\nBebidas ALCOOLICAS\n") 
                    alcool()    
                    
                    print("\nBebidas NAO ALCOOLICAS\n")
                    naoAlcool()
               
                elif alcool_naoAlcool == 'help':                                    #Função de ajuda para o usuario que não está sabendo oque fazer
                    help()                                                          #Função criada
                    
                elif alcool_naoAlcool == 'passar':
                    pass    
                elif alcool_naoAlcool.title() == 'Voltar':
                    break
                else:
                    print("Você digitou incorretamente, descreva o cardápio desejado! \n")
                    continue    
                
                while True:
 
                    escolha = input("\nDigite a escolha do cárdapio ou alguma ação descrita nas instruções: ").title() #Oque o cliente quer pedir
                    
                    if escolha == 'Voltar':                                         #Voltar para a ação anterior
                        print(f'Carrinho do cliente: {Lista_Cliente}')            
                        break    
                    
                    elif escolha == 'Cardapio':                                     #Volta para a opção de vizualização de cardapio      
                        break
 
                    elif escolha.lower == "Ajuda" or escolha.lower() == "Help":
                        help()
                        continue
 
                    else:
                        while True:
                            CalcularBebidas()
                            if n == 0:
                                x +=1                                               # Vai para a proxima opção de cardapio
                            else:
                                break
 
                        x = 0                                                       #Zerando as variaveis para uma proxima ação
                        n = 0                                  
 
 
        elif acessarLista == 'sobremesa' or acessarLista == 'sobremesas':
 
            cardapio_sobremesas()
 
            while True:
                escolha = input("\nDigite a escolha do cárdapio ou alguma ação descrita nas instruções: ").title()
 
                if escolha == 'Voltar':                 
                    print(f'Carrinho do cliente: {Lista_Cliente}')            
                    break    
                    
                elif escolha == 'Cardapio':                    
                    cardapio_sobremesas()
                    continue
 
                elif escolha == "Ajuda" or escolha == "Help":
                    help()
                    continue
 
                for s in sobremesas:                                                 #Percorre a lista de sobremesas                                                      
                    if escolha == s[0]:                                              #Verifica se a escolha contém na lista sobremesas
                        if s[0] == 'Sorvete':                                        #Cada if e elif,neste for, serve para adicionar o sabor requerido pelo cliente (Não muda o preço)
                            print("--------SABORES DISPONÍVEIS--------")
                            for sa in sabor_S:
                                print(f"Sorvete de {sa}")
                            sabores = input(f"\nVocê deseja um {escolha} de que sabor: ").title() #
                            
                            while True:                                              #Verifica se o sabor contém na lista de sabor de sorvete
                                if sabores in sabor_S:
                                    break
                                else:
                                    sabores = input("\nSabor não identificado! Digite novamente a escolha do sabor: ").title() #Se caso o sabor não estiver, ele perguntará novamente
                        
                        elif s[0] == 'Bolo':                                         #Ocorre da mesma forma com os outros
                            print("--------SABORES DISPONÍVEIS--------")
                            for sa in sabor_B:
                                print(f"Bolo de {sa}")                            
                            sabores = input(f"\nVocê deseja um {escolha} de que sabor: ").title()
 
                            while True:
                                if sabores in sabor_B:
                                    break
                                else:
                                    sabores = input("\nSabor não identificado! Digite novamente a escolha do sabor: ").title()                            
                                                                             
                        elif s[0] == 'Milk Shake':
                            print("--------SABORES DISPONÍVEIS--------")
                            for sa in sabor_M: 
                                print(f"Milk shake de {sa}")
                            sabores = input(f"\nVocê deseja um {escolha} de que sabor: ").title()                       
                            
                            while True:
                                if sabores in sabor_M:
                                    break
                                else:
                                    sabores = input("\nSabor não identificado! Digite novamente a escolha do sabor: ").title()
 
                        elif s[0] == 'Pudim':
                            print("--------SABORES DISPONÍVEIS--------")
                            for sa in sabor_P:
                                print(f"Pudim de {sa}")
                            sabores = input(f"\nVocê deseja um {escolha} de que sabor: ").title()                        
                            
                            while True:
                                if sabores in sabor_P:
                                    break
                                else:
                                    sabores = input("\nSabor não identificado! Digite novamente a escolha do sabor: ").title()
 
                        elif s[0] == 'Salgado':
                            print("--------SALGADOS DISPONÍVEIS--------")
                            for sa in salgado:
                                print(f"{sa}")
                            sabores = input(f"\nDigite o tipo de salgado desejado: ").title()                        
                            
                            while True:
                                if sabores in salgado:
                                    break
                                else:
                                    sabores = input("\nSalgado não identificado! Digite novamente a escolha do sabor: ").title()
 
                        #----------Capturar o preço e levar alimento para o carrinho do cliente----------

                        preco += s[1]
                        total += preco
                        Lista_Cliente.append(s[0] + ' De ' + sabores)                                   #Adicionara o nome do alimento e seu sabor a lsita do cliente
                        i = 0
                        print("")
                        print("--" * 35)
                        print(f'O seu pedido foi {escolha} de {sabores}, e foi adicionado no seu carrinho !')  #nesta linha será mostrado além da escolha, também o sabor da sobremesa
                        print("--" * 35)
                        sabores = ""
                        break
                    
                    else:
                        
                        i += 1
 
                if i == len(sobremesas):
                    i = 0
                    print("\nEste alimento não pertence ao cardápio"
                    "\nFavor verifique novamente o cardápio e refaça seu pedido")                                                                            
 
 
        elif acessarLista == 'lanche' or acessarLista == 'lanches':
            cardapio_lanche()
            
            while True:
                escolha = input("\nDigite a escolha do cárdapio ou alguma ação descrita nas instruções: ").title()
 
                if escolha == 'Voltar':                 
                    print(f'Carrinho do cliente: {Lista_Cliente}')                      
                    break    
                    
                elif escolha == 'Cardapio':                    
                    cardapio_lanche()
                    continue
 
                elif escolha == "Ajuda" or escolha == "Help":
                    help()
                    continue
 
                for la in lanches:
                    if escolha in la[0]:                                                                #Ocorrerá tudo QUASE igual o de sobremesa
                        if la[0] == 'Salgado' or la[0] == 'Salgados':
                            print("\n--------SABORES DISPONÍVEIS--------")
                            for sa in salgado:
                                print(f"Você pode escolher o salgado de: {sa}")
                            
                            sabores = input("\nDigite o tipo de salgado desejado: ").title()                        
                                
                            while True:
                                if sabores in salgado:
                                    break
                                else:
                                    sabores = input("\nSalgado não identificado! Digite novamente a escolha do sabor: ").title()
 
                        elif la[0] == 'Bolo':
                            print("\n--------SABORES DISPONÍVEIS--------")
                            for sa in sabor_B:
                                print(f"Bolo de {sa}")                            
                            sabores = input(f"\nVocê deseja um {escolha} de que sabor: ").title()
 
                            while True:
                                if sabores in sabor_B:
                                    break
                                else:
                                    sabores = input("\nSabor não identificado! Digite novamente a escolha do sabor: ")                            
                                                                                
                        elif la[0] == 'Milk Shake':
                            print("\n--------SABORES DISPONÍVEIS--------")
                            for sa in sabor_M: 
                                print(f"Milk shake de {sa}")
                            sabores = input(f"\nVocê deseja um {escolha} de que sabor: ").title()                       
                                
                            while True:
                                if sabores in sabor_M:
                                    break
                                else:
                                    sabores = input("\nSabor não identificado! Digite novamente a escolha do sabor: ")
 
                        elif la[0] == 'Pudim':
                            print("\n--------SABORES DISPONÍVEIS--------")
                            for sa in sabor_P:
                                print(f"Pudim de {sa}")
                            sabores = input(f"\nVocê deseja um {escolha} de que sabor: ").title()                        
                                
                            while True:
                                if sabores in sabor_P:
                                    break
                                else:
                                    sabores = input("\nSabor não identificado! Digite novamente a escolha do sabor: ")
 
                        #----------Capturar o preço e levar alimento para o carrinho do cliente----------
                        preco += la[1]
                        total += preco
                        i = 0
                        print("")
                        print("--" * 35)
                        if sabores != '':                                                           # Se sabores for diferente de vazio ele automaticamente identificará que o alimento contém um sabor
                            Lista_Cliente.append(la[0] + ' De ' + sabores)
                            print(f'O seu pedido foi {escolha} de {sabores}, e está adicionado no seu carrinho !')
                            sabores = ''    
                        else:                                                                       # Se não for diferente de vazio, então ele saberá que não tem um sabor e só enviará o nome do alimento, sem sabor algum
                            Lista_Cliente.append(la[0])                 
                            print(f'O seu pedido foi {escolha}, e está adicionado no seu carrinho !')
                        print("--" * 35)
                        sabores = ''
                        break
                    else:
                        i+=1
 
                if i == len(lanches):
                    i = 0
                    print("\nEste alimento não pertence ao cardápio"
                    "\nFavor verifique novamente o cardápio e refaça seu pedido")
 
        else:
            print("Opção não encontrada, reescreva a opção de alimento desejável !")                #Se nenhum tipo de cardapio for encontado, ele enviará está mensagem
 
    elif acao == 'cardapio':                                                                        #Mostrará os cardapios completos de todos os alimentos
        print("\n" + "-" * 25 + "ALMOÇO" + "-" * 25 + "\n")
        cardapio_almoco()
 
        print("\n" + "-" * 25 + "Bebidas Alcoolicas" + "-" * 25 + "\n")
        alcool()
 
        print("\n" + "-" * 25 + "Bebidas NÃO Alcoolicas" + "-" * 25 + "\n")
        naoAlcool()
 
        print("\n" + "-" * 25 + "SOBREMESAS" + "-" * 25 + "\n")
        cardapio_sobremesas()
 
        print("\n" + "-" * 25 + "LANCHE" + "-" * 25 + "\n")
        cardapio_lanche()
 
        
    elif acao == "excluir" or acao == "apagar":                                                     #Este laço serve para excluir algum alimento do carrinho
        print(Lista_Cliente)
        
        while True:
            print("\nPara apagar toda sua lista de pedido, digite 'Lista'\n")                       #Se o usuario digitar Lista apagará tudo
            exclusao = input("Oque você deseja apagar de sua lista: ").title()
            
            if exclusao == 'Voltar':
                break
            elif exclusao == 'Lista':
                while True:
                    print("Digite (S ou N)")
                    confirm = input(f"Você tem certeza que deseja excluir {exclusao}? ").title()[0] #Confirmação da exclusão do item
                    
                    if confirm == 'S':                                                              #Se o usuario digitar Sim ou S, irá apagar toda a lista
                        Lista_Cliente.clear()
                        total = 0
                        break
 
                    elif confirm == 'N':                                                           #Se o usuario digitar Nao ou N, cancelará a exclusao
                        print("Exlusão cancelada !")
                        break
 
                    else:
                        print("Não entendi, refaça novamente sua ação !")  
 
            elif exclusao in Lista_Cliente:
                while True:
                    print("Digite (S ou N)")    
                    confirm = input(f"Você tem certeza que deseja excluir {exclusao}? ").title()[0] #Confirmação da exclusão do item
                    
                    if confirm == 'S':
                        for ex in Lista_Cliente:
                            if exclusao == ex:
                                Lista_Cliente.remove(ex)                                          #O item será removido da lista
                                print("\nITEM DELETADO!\n")
                                print(Lista_Cliente)
                                
                                while True:
                                    Lista = input("Por favor, informe a opção de cardápio do item que foi excluido: ").lower() #Perguntará de qual lista do cardápio o item foi excluido para identificação no código
                                    
                                    if Lista == 'almoco' or Lista == 'almoço':              
                                        for a in almoco:
                                            if a[0] == exclusao:
                                                totalA = total                                    #O total Anterior será igual o total atual
                                                total -= a[1]                                     #Então o total perderá o valor do item excluido
                                                print(f"Total gasto atualmente: R${total:.2f}\n")   #Então mostrará o valor total atual
                                                exclusao = ''
                                                break
                                            
                                        verificacaoExclusao()                                     #Nestá verificação de exclusão, o programa mostrará o total anterior e o atual, para o cliente saber que a diminuição foi feita corretamente
                                        if exclusao == '':
                                            break  
 
                                    elif Lista == 'bebida' or Lista == 'bebidas':                 #Aqui em bebidas teve que se codificado fazer 2 for, para que ele lesse o dicionario de alcoolicas e nao alcoolicas
                                        for k,v in bebidas[0].items():
                                            for c in v:
                                                if c[0] == exclusao:
                                                    totalA = total
                                                    total -= c[1]
                                                    print(f"Total gasto atualmente: R${total:.2f}\n")
                                                    exclusao = ''
                                                    break
 
                                        for k,v in bebidas[1].items():
                                            for c in v:
                                                if c[0] == exclusao:
                                                    totalA = total
                                                    total -= c[1]
                                                    print(f"Total gasto atualmente: R${total:.2f}\n")
                                                    exclusao = ''
                                                    break
 
                                                elif c[0] == 'Suco':                                #Quando c do for, for igual a suco de alguma coisa, ele entrará neste laço
                                                    if exclusao[0:4] == 'Suco':                     #Nesta linha foi identificado se as primeiras 4 palavras de exclusao é Suco, se caso for ele saberá que a exclusao foi um suco e pegará o item suco da lista de bebidas e exlcuirá o valor
                                                        totalA = total
                                                        total -= c[1]
                                                        print(f"Total gasto atualmente: R${total:.2f}\n")
                                                        exclusao = ''
                                                        break
                                      
                                        verificacaoExclusao()
                                        if exclusao == '':
                                            break      
                                            
                                    elif Lista == 'sobremesas' or Lista == 'sobremesa':             #Em sobremesa foi feita a mesma ideia do suco
                                        for s in sobremesas:
                                            if s[0] == 'Sorvete':
                                                if exclusao[0:7] == 'Sorvete':
                                                    totalA = total
                                                    total -= s[1]
                                                    print(f"Total gasto atualmente: R${total:.2f}\n")
                                                    exclusao = ''
                                                    break
                                            
                                            elif s[0] == 'Bolo':    
                                                if exclusao[0:4] == 'Bolo':
                                                    totalA = total
                                                    total -= s[1]
                                                    print(f"Total gasto atualmente: R${total:.2f}\n")
                                                    exclusao = ''
                                                    break
 
                                            elif s[0] == 'Milk Shake':
                                                if exclusao[0:10] == 'Milk Shake':
                                                    totalA = total
                                                    total -= s[1]
                                                    print(f"Total gasto atualmente: R${total:.2f}\n")
                                                    exclusao = ''
                                                    break
 
                                            elif s[0] == 'Pudim':
                                                if exclusao[0:5] == 'Pudim':
                                                    totalA = total
                                                    total -= s[1]
                                                    print(f"Total gasto atualmente: R${total:.2f}\n")
                                                    exclusao = ''
                                                    break
                                            
                                            elif s[0] == 'Salgado':
                                                if exclusao[0:7] == 'Salgado':
                                                    totalA = total
                                                    total -= s[1]
                                                    print(f"Total gasto atualmente: {total:.2f}\n")
                                                    exclusao = ''
                                                    break
                                        verificacaoExclusao()
                                        if exclusao == '':
                                            break      
 
                                    elif Lista == 'lanches' or Lista == 'lanche':                   #Em lanche foi feito a mesma ideia do suco e sobremesa, mas... leia abaixo !
                                        for la in lanches:
                                            if la[0] == exclusao:                                   #Neste laço em especifico verificará se o item escolhido não é algum alimento que contém sabor!
                                                totalA = total                                      #Assim não precisará verificar a primeira palavra, para saber se é um alimento em especifico
                                                total -= la[1]
                                                print(f"Total gasto atualmente: R${total:.2f}\n")  
                                                exclusao = ''
                                                break
 
                                            elif la[0] == 'Sorvete':
                                                if exclusao[0:7] == 'Sorvete':
                                                    totalA = total
                                                    total -= la[1]
                                                    print(f"Total gasto atualmente: R${total:.2f}\n")
                                                    exclusao = ''
                                                    break
                                            
                                            elif la[0] == 'Bolo':    
                                                if exclusao[0:4] == 'Bolo':
                                                    totalA = total
                                                    total -= la[1]
                                                    print(f"Total gasto atualmente: R${total:.2f}\n")
                                                    exclusao = ''
                                                    break
 
                                            elif la[0] == 'Milk Shake':
                                                if exclusao[0:10] == 'Milk Shake':
                                                    totalA = total
                                                    total -= la[1]
                                                    print(f"Total gasto atualmente: R${total:.2f}\n")
                                                    exclusao = ''
                                                    break
 
                                            elif la[0] == 'Pudim':
                                                if exclusao[0:5] == 'Pudim':
                                                    totalA = total
                                                    total -= la[1]
                                                    print(f"Total gasto atualmente: R${total:.2f}\n")
                                                    exclusao = ''
                                                    break
                                            
                                            elif la[0] == 'Salgado':
                                                if exclusao[0:7] == 'Salgado':
                                                    totalA = total
                                                    total -= la[1]
                                                    print(f"Total gasto atualmente: R${total:.2f}\n")
                                                    exclusao = ''
                                                    break
                                        
                                        verificacaoExclusao()
                                        if exclusao == '':
                                            break        
            
                                    else:
                                        print("Cardápio não encontrado, por favor, reescreva novamente !") #Cardapio do cliente não identificado, enviará está mensagem
                        break
  
 
                    elif confirm == 'N':                                                                #Se digitar Nao na confirmação, a exlusao será cancelada
                        print("Exlusão cancelada !")
                        break
                    
                    else:
                        print("Não entendi, refaça novamente sua ação !")                               #Se não indentificar a confirmação, enviará isto e perguntará de novo
 
            else:
                print("Item não encontrado!")                                                           #Item de exclusão não identificado, eviará este alerta e perguntará de novo
    
    elif acao == "conta":
        print(f"O valor que você gastou até agora é R${total:.2f}\n")                                   #Envia a conta atual, o valor atual do dinheiro gasto do cliente
        time.sleep(3)
 
    else:
        print("\nAção não encontrada..."                                                                #Se a acao não for identificada enviará a mensagem e perguntará de novo
        "Tente novamente!")