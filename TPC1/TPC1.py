def reverte(palavra):
    return palavra[::-1]

def contaA(palavra):
    A=[x for x in palavra if x=="A"]
    a=[x for x in palavra if x=="a"]
    Aa=[x for x in palavra if x=="a" or x=="A"]
    print("A: " + str(len(A)) + "; a: " + str(len(a)) + "; A/a: " + str(len(Aa)))
    
def vogais(palavra):
    i=0
    vogais=["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    lista = [l for l in palavra if l in vogais]
    print(len(lista))
    
def minuscula(palavra):
    return palavra.lower()

def maiuscula(palavra):
    return palavra.upper()

def capicua(palavra):
    r=palavra[::-1]
    if r==palavra:
        return True
    else:
        return False
    
def balanceado(p1, p2):
    for elem in p1:
        if elem not in p2:
            return False
    return True

def ocorrencias(p1, p2):
    p1=p1.lower()
    p2=p2.lower()
    tamanho=len(p1)
    conta=0
    for i in range(len(p2)):
        if p2[i:i+tamanho] == p1:
            conta +=1
    return conta

def anagrama(p1, p2):
    p1=sorted(p1.lower())
    p2=sorted(p2.lower())
    if p1==p2:
        return True
    else: 
        return False

def classes():
    file=open('CIH Bilingual Medical Glossary English-Spanish.txt', encoding="utf8")
    text= file.read()
    caracteres=[",", ".", ":", "-", "—", "/", "(", ")", "'", ";", "&", "?"]  # Caracteres especiais a ser removidos
    for i in range(0,10):
        caracteres.append(str(i))                        # Adição de números à lista de caracteres a serem removidos
    for elem in caracteres:
        text=text.replace(elem, " ")                     # Substituição de todos os caracteres especiais por espaço
    text=text.lower()                                    # Todas as letras em minuscula para que os anagramas sejam analisados corretamente
    anagramas={}                                         # Dicionário que tem como chave as letras ordenadas de cada anagrama e como valores os próprios anagramas 
    tokens = text.split()                                # A lista tokens contem todas as palavras existentes no documento
    tokens = list(set(tokens))                           # Criação de uma lista sem palavras repetidas
    tokens=[elem for elem in tokens if len(elem)>1]      # Remover palavras com apenas uma letra, uma vez que se considerou que as mesmas não podem ter anagramas
    for token in tokens:
        ordem=''.join(sorted(token))
        if ordem in anagramas.keys():            # Se já foi encontrada uma palavra com as mesmas letras
            lista=anagramas[ordem]               # Adiciona-se a nova palavra encontrada à lista
            lista.append(token)
            anagramas[ordem] = lista
        else:                                    # Caso contrário
            anagramas[ordem] = [token]           # Cria-se uma nova chave para o dicionário
  
    for key, value in anagramas.items():
        print(key, ":", value)
    
classes()


