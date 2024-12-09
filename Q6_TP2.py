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

def contar_pedidos_impares(pilha_de_pedidos):
    contador = 0
    pilha_auxiliar = Pilha()
    
    while not pilha_de_pedidos.esta_vazia():
        pedido = pilha_de_pedidos.desempilhar()
        pilha_auxiliar.empilhar(pedido)
        
        if pedido % 2 != 0:
            contador += 1
    
    while not pilha_auxiliar.esta_vazia():
        pilha_de_pedidos.empilhar(pilha_auxiliar.desempilhar())
    
    return contador

if __name__ == "__main__":
    pilha_de_pedidos = Pilha()
    pilha_de_pedidos.empilhar(101)
    pilha_de_pedidos.empilhar(202)
    pilha_de_pedidos.empilhar(303)
    pilha_de_pedidos.empilhar(404)
    pilha_de_pedidos.empilhar(505)

    quantidade_impares = contar_pedidos_impares(pilha_de_pedidos)
    print("Quantidade de pedidos com ID ímpar:", quantidade_impares)