'''
A nossa solução será é a criação de uma central dedicada a gestão de histórico de dados médicos.
Um portal destinado aos médicos e pronto socorros, permitindo acesso fácil e rápido aos históricos durante
consultas e emergências.
E ele será alimentado por médicos e profissionais da saúde com dados do momento como sintomas, medicamentos,
exames e datas e observações...para contribuir a continuidade do acompanhamento por futuros profissionais de
saúde.
'''

dados_consulta = {'Data': "25/08/2023", 'Sintomas': "Diarreia", 'Medicação': "Nitazoxanida", 'Exames': "Exame de sangue", 'Descrição': "Dor no estômago, fraqueza, febre."}
dados_hospitalar = {'Tamanho': 1.90, 'Peso': 92, 'Sangue': "-O", 'Alergia': "Não", 'Cirurgia': "Não", 'Fratura': "Não"}

# Definindo uma função para iniciar uma nova consulta
def iniciar_consulta(paciente):
    # Solicitando informações da consulta ao usuário
    dt_consulta = input("Data da consulta: ")
    sintomas = input("Sintomas: ")
    medicacao = input("Remédio/Medicação: ")
    exames = input("Exames: ")
    desc_consulta = input("Descrição da consulta: ")

    # Criando um dicionário com os dados da consulta
    dados_consulta = {'Data': dt_consulta, 'Sintomas': sintomas, 'Medicação': medicacao, 'Exames': exames, 'Descrição': desc_consulta}

    # Exibindo mensagem de que a consulta foi iniciada
    print("\nConsulta Iniciada:")

    # Chamando uma função para exibir os dados da consulta
    exibir_dados_consulta(dados_consulta)

# Definindo uma função para consultar o histórico do paciente
def consultar_historico(paciente, dados_consulta):

    # Exibindo mensagem sobre a ação sendo realizada
    print("\nHistórico do Paciente:")

    # Chamando uma função para exibir os dados da consulta
    exibir_dados_consulta(dados_consulta)

# Definindo uma função para consultar os dados hospitalares do paciente
def consultar_dados_hospitalares(paciente, dados_hospitalares):
    # Exibindo mensagem sobre a ação sendo realizada
    print("\nDados Hospitalares do Paciente:")

    # Exibindo dados hospitalares específicos do paciente
    print(f"Tamanho: {dados_hospitalares['Tamanho']}")
    print(f"Peso: {dados_hospitalares['Peso']}")
    print(f"Tipo Sanguíneo: {dados_hospitalares['Sangue']}")
    print(f"Possui alergia? Se sim, o que: {dados_hospitalares['Alergia']}")
    print(f"Já fez cirurgia? Se sim, qual: {dados_hospitalares['Cirurgia']}")
    print(f"Já sofreu alguma fratura? Se sim, qual: {dados_hospitalares['Fratura']}")

# Definindo uma função para exibir os dados de uma consulta
def exibir_dados_consulta(dados_consulta):
    # Exibindo informações específicas da consulta
    print(f"Data da consulta: {dados_consulta['Data']}")
    print(f"Sintomas: {dados_consulta['Sintomas']}")
    print(f"Medicação: {dados_consulta['Medicação']}")
    print(f"Exames: {dados_consulta['Exames']}")
    print(f"Descrição da consulta: {dados_consulta['Descrição']}")

# Definindo uma função para exibir o menu de opções
def menu_opcoes():
    print("Opções:")
    print("1. Iniciar Consulta")
    print("2. Consultar Histórico")
    print("3. Consultar Dados Hospitalares")
    print("4. Sair")

# Definindo uma função para obter uma opção válida do usuário
def obter_opcao_valida():
    while True:
        try:
            opc = int(input("Informe a opção desejada: "))
            if 1 <= opc <= 4:
                return opc
            else:
                print("Opção inválida. Escolha entre 1 e 4.")
        except ValueError:
            print("Opção inválida. Digite um número.")

# Função principal do programa
def main():
    # Inicializando variáveis
    login = 1
    dados_hospitalares = {'Tamanho': 170, 'Peso': 70, 'Sangue': "A+", 'Alergia': "Não", 'Cirurgia': "Não", 'Fratura': "Não"}
    dados_consulta = {'Data': "25/08/2023", 'Sintomas': "Diarreia", 'Medicação': "Nitazoxanida", 'Exames': "Exame de sangue", 'Descrição': "Dor no estômago, fraqueza, febre."}

    while login:
        # Página de login do médico
        print("Página de Login do médico.")
        print("\n\n")
        nome = input("Informe o seu nome: ")
        senha = input("Informe sua senha: ")
        print(f"Olá doutor(a): {nome}")

        # Solicitando ao usuário iniciar ou não uma consulta
        on = int(input("Iniciar consulta? (1-SIM 0-NÃO): "))

        while on == 1:
            # Loop para ações durante a consulta
            paciente = input("Informe o nome do paciente: ")

            # Exibindo o menu de opções
            menu_opcoes()

            # Obtendo uma opção válida do usuário
            opc = obter_opcao_valida()

            if opc == 1:
                # Chamando a função para iniciar uma consulta
                iniciar_consulta(paciente)
            elif opc == 2:
                # Chamando a função para consultar o histórico
                consultar_historico(paciente, dados_consulta)
            elif opc == 3:
                # Chamando a função para consultar dados hospitalares
                consultar_dados_hospitalares(paciente, dados_hospitalares)
            elif opc == 4:
                # Saindo do loop quando a opção é 4
                break
            else:
                # Mensagem para opção inválida
                print("Opção inválida!!")

            # Perguntando ao usuário se deseja continuar
            on = int(input("Deseja continuar? (1-SIM 0-NÃO): "))

# Garantindo que a função principal seja chamada apenas quando o script é executado
if __name__ == "__main__":
    main()
