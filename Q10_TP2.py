class Fila:
    def __init__(self):
        self.livros = []

    def adicionar(self, livro_id):
        self.livros.append(livro_id)

    def remover(self):
        if not self.esta_vazia():
            return self.livros.pop(0)
        return None

    def esta_vazia(self):
        return len(self.livros) == 0

    def tamanho(self):
        return len(self.livros)

    def __str__(self):
        return str(self.livros)

def contar_livros_impares(fila_de_livros):
    contador = 0
    for livro_id in fila_de_livros.livros:
        if livro_id % 2 != 0:
            contador += 1
    return contador

if __name__ == "__main__":
    fila_de_livros = Fila()
    fila_de_livros.adicionar(101)
    fila_de_livros.adicionar(202)
    fila_de_livros.adicionar(303)
    fila_de_livros.adicionar(404)
    fila_de_livros.adicionar(505)

    print("Fila de livros:", fila_de_livros)
    quantidade_impares = contar_livros_impares(fila_de_livros)
    print("Quantidade de livros com ID ímpar:", quantidade_impares)