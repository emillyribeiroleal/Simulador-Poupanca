print ("=====SISTEMA SIMULADOR DE POUPANÇA=====\n")

while True:
    totalguar = float(input("Quanto você deseja guardar?:").replace(",","."))
   


    if totalguar <= 0:
        print("\nO valor não pode ser menor que zero ou negativo!")
    else:
        break

while True:
    meses = int(input("\nPor quantos meses deseja guardar? "))

    if meses <= 0:
            print("\nO valor não pode ser menor que zero ou negativo!\n")
    else:
            break


while True:
    rendimento = input("\nDeseja adicionar algum valor para rendimento? (Sim ou Não): ").strip().upper()

    if rendimento == "SIM":
        valor = float(input("\nQual a taxa de rendimento anual/mensal desejada (em %)? ").replace(",", ".").replace("%", ""))

        break 
  
    elif rendimento == "NÃO" or rendimento == "NAO":
        valor = 0.0
        print("\n=====OBRIGADA PELA PREFERÊNCIA=====")
        print("=====SISTEMA ENCERRADO=====")
        break 
        
    else:
        print("\nOpção inválida! Por favor, responda com 'Sim' ou 'Não'.")


total_limpo = totalguar*meses
ganho_rendimento = total_limpo*(valor/100)
valor_final = total_limpo + ganho_rendimento


print ("\n=====RELATÓRIO DA SIMULAÇÃO====\n")
print(f"O total guardado foi de: R${totalguar}")
print(f"A quantidades escolhida para fazer a simulação foi de:  {meses} meses")
print(f"Se o depósito for de R${totalguar} por {meses} meses o valor final será de: {totalguar*meses:.2f}")
print(f"O valor escolhido para simular o rendimento foi de: {valor}%")
print(f"O total final da simulação com acréscimo do rendimento é de: {valor_final} ")


