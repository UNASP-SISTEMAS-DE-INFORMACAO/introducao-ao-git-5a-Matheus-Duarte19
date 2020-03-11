def Maior(): 
    for idade in range(1,20):
        while idade < 18:
            if idade > 18:
                print("Menor de idade")
            else:
                print("Maior de Idade")    

    return Maior

print(Maior)