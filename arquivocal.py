print ("=====SISTEMA SIMULADOR DE POUPANÇA=====\n")

while True:
    totalguar = float(input("Quanto você deseja guardar?: ").replace(",","."))
   


    if totalguar <= 0:
        print("\nO valor não pode ser menor que zero ou negativo!")
    else:
        break

while True:
    meses = int(input("\nPor quantos meses deseja guardar? "))

    if meses <= 0:
            print("\nO valor não pode ser menor que zero ou negativo!")
    else:
            break

print ("\n=====RESULTADO====\n")
print(f"O total guardado foi de: R${totalguar}")
print(f"A quantidades escolhida para fazer a simulação foi de:  {meses} meses")
print(f"Se o deposito for de R${totalguar} por {meses} meses o valor final será de: {totalguar*meses:.2f}")
