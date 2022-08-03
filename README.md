# Trabalho Prático 1: Manipulação de sequências
## Objetivos

Nesse trabalho serão abordados os aspectos práticos de manipulação de sequências. Especificamente, serão explorados aspectos de implementação de árvores de prefixo aplicada ao problema de compressão de arquivos.

O objetivo secundário é fixar o conteúdo. Entende-se que ao implementar a estrutura o aluno conseguirá compreender melhor os conceitos explorados. Dessa forma, o conteúdo teórico será melhor absorvido e fixado. Além disso, os alunos terão a oportunidade de ver conceitos não abordados na disciplina, no caso específico, um método de compressão de arquivos.

## Tarefas

Os alunos deverão implementar um algoritmo para resolver o problema de comprimir arquivos texto através do método LZ78. Esse método é baseado em dicionários e, basicamente, substitui strings que se repetem no texto por códigos. Como o algoritmo executa muitas buscas e inserções nesse dicionário, é comum utilizar árvores de prefixo na sua implementação. O LZ78, apesar de simples, é a base de vários algoritmos implementados nas ferramentas de compressão utilizadas atualmente. A seguir é apresentada uma breve descrição do algoritmo.

O LZ78 foi proposto por Lempel e Ziv em 1978. Como dito, a ideia do algoritmo é substituir strings que se repetem no texto por um código, diminuindo assim o número de bytes gravados na saída. O dicionário é inicializado com a string vazia associada ao código 0. Então, o texto é processado da esquerda para a direita, caracter a caracter. Uma string 'padrão' é mantida para verificar se essa substring já ocorreu anteriormente no texto. Se o padrão acrescido do próximo caracter lido ocorrer no dicionário, então mais um símbolo é lido e o ciclo se repete. Caso contrário, o par (código_padrão; caracter) deve ser emitido na saída, e a sequência padrão + caracter deve ser inserida no dicionário com um novo código. O ciclo se repete até que todo o arquivo tenha sido processado. A descompressão do arquivo segue o mesmo algoritmo. O dicionário é inicializado com a string vazia associada ao código 0. Sempre que um par (código_padrão, caracter) for lido, o padrão associado ao código deve ser emitido na saída, e um novo código deve ser associado à sequência padrão + caracter. O ciclo se repete até que todo o arquivo tenha sido processado. Veja um exemplo na Wikipedia https://pt.wikipedia.org/wiki/LZ78#Exemplo.

Deve-se construir um programa que implemente a compressão e descompressão de arquivos, usando o algoritmo LZ78. O dicionário deve ser implementado através de uma árvore trie compacta. As implementações deverão ser feitas em Python 3.6+,  podendo usar NumPy como biblioteca de suporte para estrutura de dados básicas.  Alternativamente, serão admitidas implementações em C/C++ compiláveis com GCC.  Nesse caso, o aluno também deverá incluir um arquivo Makefile para geração do executável.

Mais detalhes no arquivo de especificação.
