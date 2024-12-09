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

def tarefa_no_topo(pilha_de_tarefas):
    return pilha_de_tarefas.topo()

if __name__ == "__main__":
    pilha_de_tarefas = Pilha()
    pilha_de_tarefas.empilhar("Tarefa 1")
    pilha_de_tarefas.empilhar("Tarefa 2")
    pilha_de_tarefas.empilhar("Tarefa 3")

    tarefa_recente = tarefa_no_topo(pilha_de_tarefas)
    print("A tarefa mais recente no topo da pilha é:", tarefa_recente)