'''
Descrição da solução para os Pacientes.
Já para o cliente teremos um aplicativo (APP) para os pacientes, destacando a praticidade de acesso
aos históricos, medicamentos e exames prescritos, com a opção de gerar receitas ou solicitações digitais.
'''

dados_consulta = {'Data': "25/08/2023", 'Sintomas': "Diarreia", 'Medicação': "Nitazoxanida", 'Exames': "Exame de sangue", 'Descrição': "Dor no estômago, fraqueza, febre."}
dados_hospitalar = {'Carterinha': 48459563265, 'Peso': 92, 'Nascimento': "23/11/1990", 'Sangue': "-O", 'Alergia': "Não", 'Cirurgia': "Não", 'Fratura': "Não"}
lista_consultas = ({'Data': "25/08/2023", 'Sintomas': "Diarreia", 'Medicação': "Nitazoxanida", 'Exames': "Exame de sangue", 'Descrição': "Dor no estômago, fraqueza, febre."}, {'Data': "25/07/2023", 'Sintomas': "Febre", 'Medicação': "Dipirona", 'Exames': "Exame de sangue", 'Descrição': "Fraqueza, febre."}, {'Data': "25/08/2021", 'Sintomas': "conjuntivite ", 'Medicação': "Colírio Legrand", 'Exames': "Não aplicavel", 'Descrição': "Vermelhidão e inchasso nos olhos."})

# Função para mostrar o histórico de consultas
def mostrar_historico_consultas(consultas):
    for i, consulta in enumerate(consultas):
        print(f"Histórico da {i + 1}ª consulta:")
        print(f"Data da consulta: {consulta['Data']}")
        print(f"Sintoma: {consulta['Sintomas']}")
        print(f"Medicação prescrita: {consulta['Medicação']}")
        print(f"Exame prescrito: {consulta['Exames']}")
        print(f"Descrição da consulta: {consulta['Descrição']}\n")

# Função para mostrar exames prescritos
def mostrar_exames_prescritos(consultas):
    for consulta in consultas:
        print(f"Sintoma: {consulta['Sintomas']}")
        print(f"Exame prescrito: {consulta['Exames']}\n")

# Função para mostrar medicação prescrita
def mostrar_medicacao_prescrita(consultas):
    for consulta in consultas:
        print(f"Sintoma: {consulta['Sintomas']}")
        print(f"Medicação prescrita: {consulta['Medicação']}\n")

# Função para a página de login do paciente
def pagina_login_paciente():
    print("Página de Login Paciente.")
    print("\n\n")
    nome = input("Informe o seu nome: ")
    senha = input("Informe sua senha: ")
    print(f"Olá paciente: {nome}")
    return nome

# Função para exibir o menu de opções
def menu_opcoes():
    print("Deseja consultar histórico de consultas - Opção 1")
    print("Exames prescritos - Opção 2")
    print("Medicações prescritas - Opção 3")

# Função para obter uma opção válida do usuário
def obter_opcao_valida():
    while True:
        try:
            opc = int(input("Informe a opção desejada: "))
            if 1 <= opc <= 3:
                return opc
            else:
                print("Opção inválida. Escolha entre 1 e 3.")
        except ValueError:
            print("Opção inválida. Digite um número.")

# Função principal
def main():
    login = 1
    while login:
        # Página de login do paciente
        nome_paciente = pagina_login_paciente()
        on = int(input("Ok para o login? (1-SIM 0-NÃO): "))
        while on == 1:
            print(f"Paciente: {nome_paciente}")

            # Exibindo o menu de opções
            menu_opcoes()
            opc = obter_opcao_valida()

            if opc == 1:
                # Chamando a função para mostrar o histórico de consultas
                mostrar_historico_consultas(lista_consultas)
            elif opc == 2:
                # Chamando a função para mostrar exames prescritos
                mostrar_exames_prescritos(lista_consultas)
            elif opc == 3:
                # Chamando a função para mostrar medicação prescrita
                mostrar_medicacao_prescrita(lista_consultas)

            # Perguntando ao usuário se deseja continuar
            on = int(input("Deseja continuar? (1-SIM 0-NÃO): "))

if __name__ == "__main__":
    main()