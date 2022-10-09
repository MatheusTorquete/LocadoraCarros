## Locação de Carros

carros = [
            ("Chevrolet Tracker", 120),
            ("Chevrolet Onix", 90),
            ("Chevrolet Spin", 150),
            ("Hyundai HB20", 85),
            ("Hyundai Tucson", 120),
            ("Fiat Uno", 60),
            ("Fiat Mobi", 70),
         ] 

## alocamos os carros em TUPLAS, com o Nome e os Valores


alugados = []


## função que printa o valor dos carros e o alugados, desmembrando as duas.
def mostrar_lista_de_carros(lista_de_carros):
    for i, car in enumerate(lista_de_carros): ## percorrendo a lista e enumerando, formatando para aparecer na forma melhor visivel
        print("[{}] {} - R$ {} /dia.".format(i,car[0], car[1])) ## o 1 é o código do carro, o 2 nome do carro, e valor do carro



# enquanto for verdade faça isso
while True:
    print("========")
    print("Bem vindo à locadora de carros!")
    print("=========")
    print("O que deseja fazer?")
    print("0 Mostrar portifólio de carros || 1 - Alugar um carro || 2 - Devolver um carro")
    op = int(input()) ## escolhendo a opção e formatando para inteiro

# verificando as opções desejadas e mostrando para o usuário
    if op == 0:
        mostrar_lista_de_carros(carros)

    elif op == 1:
        mostrar_lista_de_carros(carros)
        print("=========")
        print("Escolha o código do carro:")
        cod_car = int(input()) ## seleciona código do carro formatado para inteiro
        print("Por quantos dias você deseja alugar este carro?")
        dias = int(input()) ## selecao dias e formatado inteiro
        print("")
        print("Você escolhe {} por {}dias".format(carros[cod_car][0], dias)) ## acessando a lista dos carros a posição e os dias
        print("O aluguel totalizaria R$ {}. Deseja Alugar?".format(dias * carros[cod_car][1])) ## realizando a contagem dos dias e mostrando o valor do aluguel

        print("0 - SIM || 1 - NÃO")
        conf = int(input()) 
        if conf == 0:
            print("Parabéns você alugou o {} por {} dias".format(carros[cod_car][0], dias))
            alugados.append(carros.pop(cod_car)) ## pega a lista de carros , extrai o codigo do carro e insere no alugados
            ## operacao pythonica
    
    elif op == 2:
        if len(alugados) == 0: ## se o tamanho da lista de alugados for 0
            print("Não há carros para devolver.")
        else:
            print("Segue a lista de carros alugados. Qual você deseja devolver?")
            mostrar_lista_de_carros(alugados) ## mostrar a lista de carros alugados
            print("")
            print("Escolha o código do carro que deseja devolver:")
            cod = int(input())
            if conf == 0:
                print("Obrigado por devolver o carro {}".format(alugados[cod][0])) ## apresentando os alugados 
                carros.append(alugados.pop(cod))

## mostrar opção de saída se for igual a 1 digitado
    print("")
    print("========")
    print("0 para CONTINUAR || 1 para SAIR")
    if int(input()) == 1:
        break