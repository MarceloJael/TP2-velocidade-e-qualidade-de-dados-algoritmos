class Fila:
    def __init__(self):
        self.pacientes = []

    def adicionar(self, paciente):
        self.pacientes.append(paciente)

    def remover(self):
        if not self.esta_vazia():
            return self.pacientes.pop(0)
        return None

    def esta_vazia(self):
        return len(self.pacientes) == 0

    def tamanho(self):
        return len(self.pacientes)

    def __str__(self):
        return str(self.pacientes)

def inverter_fila(fila_de_pacientes):
    # Inverte a fila usando a função reverse
    fila_de_pacientes.pacientes.reverse()
    return fila_de_pacientes

# Exemplo de uso
if __name__ == "__main__":
    fila_de_pacientes = Fila()
    fila_de_pacientes.adicionar("Paciente 1")
    fila_de_pacientes.adicionar("Paciente 2")
    fila_de_pacientes.adicionar("Paciente 3")
    fila_de_pacientes.adicionar("Paciente 4")

    print("Fila original:", fila_de_pacientes)

    fila_invertida = inverter_fila(fila_de_pacientes)
    print("Fila invertida:", fila_invertida)