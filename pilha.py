# pilha = [1,1,2,3,5]

# pilha.append(8) 
# print("Inserindo um elemento: ",pilha)

# pilha.append(13)
# print("Inserindo um outro elemento: ",pilha)

# pilha.pop() #remove do final
# print("Removendo um elemento: ",pilha)

# pilha.pop() 
# print("Removendo um outro elemento: ",pilha)


class Nodo:
    
    def __init__(self,dado =0,nodo_anterior = None):
        self.dado = dado 
        self.anterior = nodo_anterior
    
    
    def __repr__(self):
        return '%s -> %s' %(self.dado,self.anterior)
    


class Pilha:
    
    def __init__(self):
        self.topo = None 
        self.size = 0
    

    def __repr__(self):
        return "["+str(self.topo)+ "]"
    

    def insert(self,novo_dado):
        #insere um elemento no final da pilha
        
        #Cria um novo nodo com o dado a ser armazenado
        novo_nodo = Nodo(novo_dado) 
        
        
        #Faz com que o novo nodo sejao topo da pilha
        novo_nodo.anterior = self.topo

        #Faz com que a cabeca da lista referencieo novo nodo    
        self.topo = novo_nodo

        self.size += 1
    

    def remove (self):
        #remove o elemento  que esta no topo da pilha

        assert self.topo, "Impossivel remover valor de pilha vazia"

        self.topo = self.topo.anterior

        self.size -= 1




# 1  Escrever uma função que receba como parâmetro uma pilha. A função deve retornar o maior elemento da pilha.
def buscaMax(pilha):
    maior = pilha.topo.dado
    if pilha.size == 0:
            print('Lista Vazia')

    while pilha.size > 0:
        if pilha.topo.dado > maior:
            maior = pilha.topo.dado
        pilha.remove()

    return maior

p  = Pilha()


p.insert(20)
p.insert(21)
p.insert(22)
p.insert(23)


print(buscaMax(p))

#-----------------------------------------------------------

# 2 Utilizando uma pilha resolver o exercício a seguir: Dada uma sequência contendo N (N >0) números reais, imprimi-la na ordem inversa.
def inverter():
    seq = Pilha()
    x = int(input("\nCaso queira encerrar digite um numero <= 0\nDigite um número: "))
    seq.insert(x)
    while x > 0:
        x = int(input("\nCaso queira encerrar digite um numero <= 0\nDigite um número: "))
        if x > 0:
            seq.insert(x)
    
    return seq

# print(inverter())

#-----------------------------------------------------------

# 3  Escreva uma função que receba como parâmetro duas pilhas e verifique de elas são iguais.
#  Duas pilhas são iguais se possuem os mesmos elementos, na mesma ordem
def comparar(pilha1,pilha2):
    if pilha1.size == pilha2.size:
        x = pilha1.topo.dado
        y = pilha2.topo.dado
        while (x == y) and (pilha1.size>0):
            pilha1.remove()
            pilha2.remove()
        if pilha1.size == 0:
            print("São iguais")
        else:
            print("São diferentes")

    else:
        print("Não são iguais")

p1 = Pilha()

p2 = Pilha()

p1.insert(5)
p1.insert(15)
p1.insert(20)
p1.insert(21)


p2.insert(5)
p2.insert(15)
p2.insert(20)
p2.insert(21)



comparar(p1,p2)

#-----------------------------------------------------------

#4 Construa um programa utilizando uma pilha que resolva o seguinte problema: 

# Armazene as placas dos carros (apenas os números) que estão estacionados numa rua sem saída estreita. 
# Dado uma placa verifique se o carro está estacionado na rua. 
# Caso esteja, informe a sequência de carros que deverá ser retirada para que o carro em questão consiga sair.

def verificarPlaca(pilha,placa):
    qntd = 0
    carro = 0
    if placa == pilha.topo.dado:
        print(" O seu carro é o primeiro a sair")
    else:
        while placa != pilha.topo.dado and pilha.topo.anterior != None:
            pilha.remove()
            qntd += 1
            if placa == pilha.topo.dado:
                carro +=1

        if carro > 0:     
            print(f"Será necessário remover {qntd} para o carro com a placa {placa} sair")
        
        else:
            print("Carro não encontrado")


p  = Pilha()


p.insert(285)
p.insert(288)
p.insert(283)
p.insert(282)

verificarPlaca(p,282)

verificarPlaca(p,285)

verificarPlaca(p,289)

#---------------------------------------------------------------------

#5 implemente uma função chamada TPilha, que receba um vetor de inteiros com 15 elementos. Para cada um deles, como segue: 

# Se o número for par, insira-o na pilha; 
# Se o número lido for ímpar, retire um número da pilha; 
# Ao final, esvazie a pilha imprimindo os elementos.


def tPilha(vetor):
    p = Pilha()
    for i in range(len(vetor)):
        if vetor[i] % 2 == 0:
            p.insert(vetor[i])
        
        else:
            if p.size == 0:
                continue
            else:
                p.remove()
    if p.size > 0:
        for i in range(p.size):
            print(p.topo.dado)
            p.remove()
    else:
        print("Resultado: Lista Vazia")

        

tPilha([1,2,3,6,2,4,5,6,8])

#-----------------------------------------------------------


# 6. Escreva uma função chamada TPilha2 que recebe como parâmetro 2 pilhas (N e P) e um vetor de inteiros. Para cada um: 
# se positivo, inserir na pilha P; 
# se negativo, inserir na pilha N; 
# se zero, retirar um elemento de cada pilha.


def tPilha2(N,P,vetor):
    for i in range(len(vetor)):
        if vetor[i]  > 0:
            P.insert(vetor[i])
        
        elif vetor[i] < 0:
            N.insert(vetor[i])
        
        else:
            if P.size > 0:
                P.remove()
            elif N.size > 0:
                N.remove()
            
            else:
                continue
    
    print(f"Pilha Positivos: {P}\nPilha de Negativos{N}")
        
N = Pilha()
P = Pilha()

vetor = [5,-1,2,1,0,-1,-2,-4]

tPilha2(N,P,vetor)

#-----------------------------------------------------------