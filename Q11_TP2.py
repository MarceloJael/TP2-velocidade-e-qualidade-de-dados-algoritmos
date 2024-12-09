class FilaAtendimento:
    def __init__(self):
        self.fila = []

    def adicionar_cliente(self, nome):
        """Adiciona um cliente ao final da fila."""
        self.fila.append(nome)
        print(f"Cliente '{nome}' adicionado à fila.")

    def atender_cliente(self):
        """Remove o cliente do início da fila e exibe o nome do cliente que está sendo atendido."""
        if not self.esta_vazia():
            cliente_atendido = self.fila.pop(0)
            print(f"Atendendo cliente: '{cliente_atendido}'")
            return cliente_atendido
        else:
            print("Não há clientes na fila para atender.")
            return None

    def tamanho_fila(self):
        """Retorna o número de clientes restantes na fila."""
        return len(self.fila)

    def esta_vazia(self):
        """Verifica se a fila está vazia."""
        return len(self.fila) == 0

    def __str__(self):
        """Retorna uma representação em string da fila."""
        return str(self.fila)


if __name__ == "__main__":
    fila_atendimento = FilaAtendimento()
    
    fila_atendimento.adicionar_cliente("Alice")
    fila_atendimento.adicionar_cliente("Bob")
    fila_atendimento.adicionar_cliente("Charlie")

    print("Tamanho da fila:", fila_atendimento.tamanho_fila())

    fila_atendimento.atender_cliente()
    print("Tamanho da fila após atendimento:", fila_atendimento.tamanho_fila())

    fila_atendimento.atender_cliente()
    fila_atendimento.atender_cliente()
    fila_atendimento.atender_cliente()