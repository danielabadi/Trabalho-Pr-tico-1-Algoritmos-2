import sys
import Trie
import Descomprime

def compressao(entrada, saida):
    with open(entrada, 'r') as file:
        texto = file.read()
    trie = Trie.Trie()
    arq_saida = open(saida, 'wb')
    indice = 0
    indice = trie.insert(texto, indice, arq_saida)
    file.close()
    arq_saida.close()
    
def descompressao(entrada, saida):
    dic = {}
    arq_saida = open(saida, 'w')
    dic[0] = ""
    contador = 1
    with open(entrada,"rb") as arq_entrada:
        byte = arq_entrada.read(3)
        while byte != b"":
            if(contador == 1):
                inteiro = int.from_bytes(byte, byteorder='big')
            else:
                byte = arq_entrada.read(3)
                inteiro = int.from_bytes(byte, byteorder='big') 
            byte = arq_entrada.read(2)
            letra = int.from_bytes(byte, byteorder='big')
            letra = chr(letra)
            dic[contador] = [inteiro, letra]
            Descomprime.Descomprime(dic, contador, arq_saida)
            contador += 1
    arq_entrada.close()
    arq_saida.close()

 
def main(args):
    if len(args) < 3:
        print("Há argumentos faltando.")
        return 0
    
    if args[1] == '-c':
        if len(args) < 4:
            nome = args[2].replace("txt", "z78")
        else:
            nome = args[4]
        compressao(args[2], nome)
        
    elif args[1] == '-x':
        if len(args) < 4:
            nome = args[2].replace("z78", "txt")
        else:
            nome = args[4]
        descompressao(args[2], nome)
    return 0
 
if __name__ == '__main__':
    sys.exit(main(sys.argv))
    