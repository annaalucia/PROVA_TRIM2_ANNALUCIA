from datetime import datetime

estacoes = ["Verão", "Outono", "Inverno", "Primavera"]

def determinar_estacao(data):
    dia = data.day
    mes = data.month
    
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia < 21):
        return estacoes[0]  # Verão
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia < 21):
        return estacoes[1]  # Outono
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia < 23):
        return estacoes[2]  # Inverno
    elif (mes == 9 and dia >= 23) or (mes in [10, 11]) or (mes == 12 and dia < 21):
        return estacoes[3]  # Primavera

while True:
    data_input = input("Digite a data desejada (no formato dd/mm): ")
    try:
        data = datetime.strptime(data_input + "/2000", "%d/%m/%Y")
        break
    except ValueError:
        print("Formato de data inválido. Por favor, tente novamente.")

estacao = determinar_estacao(data)
print(f"A estação do ano em {data.strftime('%d/%m')} é {estacao}.")
