class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()
        return None

    def esta_vazia(self):
        return len(self.itens) == 0

    def topo(self):
        if not self.esta_vazia():
            return self.itens[-1]
        return None

    def tamanho(self):
        return len(self.itens)

def ordenar_pilha(pilha):
    pilha_ordenada = Pilha()
    
    while not pilha.esta_vazia():
        
        temp = pilha.desempilhar()
        
        while not pilha_ordenada.esta_vazia() and pilha_ordenada.topo() > temp:
            pilha.empilhar(pilha_ordenada.desempilhar())
        
        pilha_ordenada.empilhar(temp)
    
    return pilha_ordenada

if __name__ == "__main__":
    pilha = Pilha()
    pilha.empilhar(5)
    pilha.empilhar(1)
    pilha.empilhar(3)
    pilha.empilhar(4)
    pilha.empilhar(2)

    print("Pilha original (do topo para a base):", pilha.itens)

    pilha_ordenada = ordenar_pilha(pilha)

    print("Pilha ordenada (do topo para a base):", pilha_ordenada.itens)