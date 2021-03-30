import TrieNode
class Trie():
    def __init__(self):
        self.indice = 0
        self.root = TrieNode.TrieNode("", None)
        self.root.array.append(self.indice)
        self.indice += 1
            
    def insert(self, texto, indice, arq_saida):
     
        node = self.root
        while(True):
            if(indice == len(texto)):
                arq_saida.write((0).to_bytes(3, byteorder='big'))
                return
            if(node.pref == ""):
                if texto[indice] in node.children:
                    node = node.children[texto[indice]]
                else:
                    novo_no = TrieNode.TrieNode(texto[indice], node)
                    novo_no.array.append(self.indice)
                    self.indice +=1
                    node.children[texto[indice]] = novo_no
                    arq_saida.write(int(node.array[0]).to_bytes(3, byteorder='big'))
                    arq_saida.write(ord(novo_no.pref).to_bytes(2, byteorder='big'))
                    indice += 1
                    node = self.root
            else:
                if(len(node.pref) > 1):
                    prefixo = 0
                    while((texto[indice] == node.pref[prefixo]) and prefixo < len(node.pref)-1 and indice < len(texto)-1):
                        indice += 1
                        prefixo+=1
                    if(texto[indice] != node.pref[prefixo]):
                        prefixo -= 1
                    if(prefixo == len(node.pref)-1):
                        if(len(node.children) == 0):
                            if(indice < len(texto)-1):
                                indice += 1
                                node.pref = node.pref + texto[indice]
                                arq_saida.write(int(node.array[-1]).to_bytes(3, byteorder='big'))
                                arq_saida.write(ord(texto[indice]).to_bytes(2, byteorder='big'))
                                node.array.append(self.indice)
                                self.indice += 1
                                indice += 1
                                node = self.root
                            else:
                                arq_saida.write(int(node.array[-1]).to_bytes(3, byteorder='big'))
                                arq_saida.write(ord(" ").to_bytes(2, byteorder='big'))
                                return
                        else:
                            if(indice < len(texto)-1):
                                indice +=1
                                novo_no = TrieNode.TrieNode(texto[indice], node)
                                novo_no.array.append(self.indice)
                                self.indice += 1
                                node.children[texto[indice]] = novo_no
                                arq_saida.write(int(node.array[-1]).to_bytes(3, byteorder='big'))
                                arq_saida.write(ord(novo_no.pref).to_bytes(2, byteorder='big'))
                                indice += 1
                                node = self.root
                            else:
                                arq_saida.write(int(node.array[-1]).to_bytes(3, byteorder='big'))
                                arq_saida.write(ord(" ").to_bytes(2, byteorder='big'))
                                return
                    else:
                        antes_prefixo = node.pref[:prefixo+1]
                        depois_prefixo = node.pref[prefixo+1:]
                        novo_no = TrieNode.TrieNode(depois_prefixo, node)
                        novo_no.children = node.children.copy()
                        for i in range(prefixo+1, len(node.array)):
                            novo_no.array.append(node.array[i])
                        novo_no_2 = TrieNode.TrieNode(texto[indice], node)
                        novo_no_2.array.append(self.indice)
                        self.indice += 1
                        node.children.clear()
                        copia = node.array.copy()
                        node.pref = antes_prefixo
                        node.array.clear()
                        for x in range (0, prefixo+1):
                            node.array.append(copia[x])
                                
                        node.children[texto[indice]] = novo_no_2
                        arq_saida.write(int(novo_no_2.pai.array[-1]).to_bytes(3, byteorder='big'))
                        arq_saida.write(ord(texto[indice]).to_bytes(2, byteorder='big'))
                            
                        node.children[depois_prefixo[0]] = novo_no
                        indice += 1
                        node = self.root
                else:
                    if(len(node.children) == 0):
                        if(indice < len(texto)-1):
                            indice += 1
                            node.pref = node.pref + texto[indice]
                            arq_saida.write(int(node.array[-1]).to_bytes(3, byteorder='big'))
                            arq_saida.write(ord(texto[indice]).to_bytes(2, byteorder='big'))
                            node.array.append(self.indice)
                            self.indice += 1
                            indice += 1
                            node = self.root
                        else:
                            arq_saida.write((0).to_bytes(3, byteorder='big'))
                            arq_saida.write(ord(" ").to_bytes(2, byteorder='big'))
                            indice += 1
                            return
                    else:
                        if(indice < len(texto)):
                            indice += 1
                            if(indice == len(texto)):
                                arq_saida.write((0).to_bytes(3, byteorder='big'))
                                arq_saida.write(ord(" ").to_bytes(2, byteorder='big'))
                                return
                            elif texto[indice] in node.children:
                                node = node.children[texto[indice]]
                            else:
                                novo_no = TrieNode.TrieNode(texto[indice], node)
                                novo_no.array.append(self.indice)
                                self.indice += 1
                                node.children[texto[indice]] = novo_no
                                arq_saida.write(int(novo_no.pai.array[0]).to_bytes(3, byteorder='big'))
                                arq_saida.write(ord(novo_no.pref).to_bytes(2, byteorder='big'))
                                indice += 1
                                node = self.root
                        else:
                            arq_saida.write((0).to_bytes(3, byteorder='big'))
                            arq_saida.write(ord(" ").to_bytes(2, byteorder='big'))
                            return

