def Descomprime(dic, valor, arq_saida):
    letras = ""
    while(int(valor) != 0):
        if(len(dic[valor]) == 2):
            letras = dic[valor][1] + letras
            valor = int(dic[valor][0])
        elif(len(dic[valor]) == 1):
            letras = " " + letras
            valor = int(dic[valor][0])
        else:
            valor = 0
            
    arq_saida.write(letras)
