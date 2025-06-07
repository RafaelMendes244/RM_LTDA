from datetime import datetime, timezone

# Lista que armazena as motos disponíveis para aluguel
Motos = []

# Lista que armazena as motos que já foram alugadas
MotosAlugadas = []

# Função principal do sistema administrativo
def Sistema():
    while True:
        # Cabeçalho do menu administrativo
        print("\n" + "="*40)
        print("\tSistema - RM Motos LTDA")
        print("" + "="*40)
        print("1 - Adicionar Moto")
        print("2 - Motos Alugadas")
        print("3 - Localizar Moto")
        print("4 - Remover Moto")
        print("5 - Voltar ao Inicio")

        try:
            sistema = int(input("Escolha uma Opção Acima: "))

            # Chama a função de adicionar nova moto
            if sistema == 1:
                adc_moto()

            # Mostra as motos que já foram alugadas
            elif sistema == 2:
                lista_alugadas()

            # Permite buscar por locatário ou placa
            elif sistema == 3:
                localizar_moto()

            # Remove uma moto do sistema
            elif sistema == 4:
                remover_moto()

            # Retorna ao menu inicial
            elif sistema == 5:
                break
            else:
                print("Opção Invalida!")
        except ValueError:
            print("ERRO: COMANDAO INVALIDO!")

# Menu inicial que o usuário vê ao iniciar o sistema
def Inicio():
    while True:
        print("\n" + "="*40)
        print("\tBem Vindo - RM Motos LTDA")
        print("" + "="*40)
        print("1 - Sistema")
        print("2 - Alugar Moto")
        print("3 - Motos Disponiveis")
        print("4 - Sair")

        try:
            inicio = int(input("Escolha a Opção: "))

            if inicio == 1:
                Sistema()
            elif inicio == 2:
                alugar_moto()
            elif inicio == 3:
                motos_disp()
            elif inicio == 4:
                print("Saindo do Sistema...")
                print("Desenvolvido por Rafael Mendes !")
                break
            else:
                print("Opção Invalida!!")
        except ValueError:
            print("ERRO: COMANDO INVALIDO!")

# Realiza o aluguel de uma moto
def alugar_moto():
    if not Motos:
        print("Nenhuma Moto para Locação no Momento!")
        return

    # Mostra as motos disponíveis para escolha
    print("\n" + "="*40)
    print("\tMotos Disponiveis - RM LTDA")
    print("" + "="*40)
    for i, moto in enumerate(Motos, start=1):
        print(f"{i} - Modelo: {moto['modelo']} - Placa: {moto['placa']}")

    try:
        escolha = int(input("Escolha o Numero da Moto que Deseja Alugar: "))
        if 1 <= escolha <= len(Motos):
            nome = input("Digite o Nome do Locatario: ")
            moto = Motos.pop(escolha - 1)  # Remove da lista de disponíveis
            moto['nome'] = nome            # Adiciona o nome do locatário
            moto['data'] = datetime.now().strftime("%d/%m/%Y - %H:%M")
            MotosAlugadas.append(moto)     # Envia para a lista de alugadas
            print(f"{moto['modelo']} Alugada com Sucesso para {nome} | Data: {moto['data']}")
        else:
            print("Opção Invalida!")
    except ValueError:
        print("ERRO: COMANDO INVALIDO!")

# Lista todas as motos que estão disponíveis
def motos_disp():
    if not Motos:
        print("Nenhuma Moto Disponivel no Momento")
    else:
        print("\n" + "="*40)
        print("\tLista das Motos - RM LTDA")
        print("" + "="*40)
        for i, moto in enumerate(Motos, start=1):
            print(f"{i} - Modelo: {moto['modelo']} Placa: {moto['placa']}")

# Adiciona uma nova moto no sistema
def adc_moto():
    modelo = input("Modelo da Moto: ")
    placa = input("Placa da Moto: ")

    # Verifica se a placa já está cadastrada (em ambas as listas)
    for moto in Motos + MotosAlugadas:
        if moto['placa'] == placa:
            print(f"{placa} Ja esta Cadastrada!")
            return

    Motos.append({"modelo": modelo, "placa": placa})
    print(f"{modelo} Adicionada com Sucesso!")

# Lista todas as motos que já foram alugadas
def lista_alugadas():
    if not MotosAlugadas:
        print("Nenhuma Moto Alugada no Momento!")
    else:
        print("\n" + "="*40)
        print("\tMotos Alugadas - RM LTDA")
        print("" + "="*40)
        for i, moto in enumerate(MotosAlugadas, start=1):
            print(f"{i} - Nome: {moto['nome']} - Modelo: {moto['modelo']} - Placa: {moto['placa']} | Data: {moto['data']}")

# Busca uma moto pelo nome do locatário ou pela placa
def localizar_moto():
    loc = input("Digite o Nome do Locatario ou Placa da Moto: ").lower()

    # Procura na lista de motos alugadas
    for moto in MotosAlugadas:
        if moto['nome'].lower() == loc or moto['placa'].lower() == loc:
            print("\n" + "="*40)
            print("\tMoto localizada - ALUGADA - RM LTDA")
            print("" + "="*40)
            print(f"Locatário: {moto['nome']}")
            print(f"Modelo: {moto['modelo']}")
            print(f"Placa: {moto['placa']}")
            return

    # Procura nas motos disponíveis
    for moto in Motos:
        if moto['modelo'].lower() == loc or moto['placa'].lower() == loc:
            print("\n" + "="*40)
            print("\tMoto localizada - DISPONIVEL - RM LTDA")
            print("" + "="*40)
            print(f"Modelo: {moto['modelo']}")
            print(f"Placa: {moto['placa']}")
            return

    print(f"{loc} Não esta no Sistema!")

# Remove uma moto do sistema (disponível ou alugada)
def remover_moto():
    print("\n" + "="*40)
    print("\tRemoçao de Veiculo - RM LTDA")
    print("" + "="*40)
    remove = input("Digite a Placa da Moto: ")

    # Verifica se está na lista de disponíveis
    for moto in Motos:
        if moto['placa'] == remove:
            Motos.remove(moto)
            print(f"Removeu a Moto de Placa: {remove}")
            return

    # Verifica se está na lista de alugadas
    for moto in MotosAlugadas:
        if moto['placa'] == remove:
            MotosAlugadas.remove(moto)
            print(f"Moto Alugada: Placa {remove} Removida com Sucesso!")
            return

    print(f"{remove} Não esta no Sistema!")

# Inicia o programa chamando o menu principal
Inicio()