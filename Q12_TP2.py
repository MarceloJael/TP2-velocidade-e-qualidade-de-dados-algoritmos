class TabelaHash:
    def __init__(self, tamanho_inicial):
        """Construtor que aceita um tamanho inicial para a tabela."""
        self.tamanho = tamanho_inicial
        self.tabela = [[] for _ in range(self.tamanho)]

    def _funcao_hash(self, chave):
        """Função de hash simples que calcula o índice para uma chave."""
        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):
        """Adiciona uma chave e seu valor correspondente à tabela."""
        indice = self._funcao_hash(chave)
        for i, (chave_existente, _) in enumerate(self.tabela[indice]):
            if chave_existente == chave:
                self.tabela[indice][i] = (chave, valor)
                break
        else:
            self.tabela[indice].append((chave, valor))

    def buscar(self, chave):
        """Recupera o valor associado a uma chave."""
        indice = self._funcao_hash(chave)
        for chave_existente, valor in self.tabela[indice]:
            if chave_existente == chave:
                return valor
        return None

    def remover(self, chave):
        """Remove uma chave (e seu valor) da tabela."""
        indice = self._funcao_hash(chave)
        for i, (chave_existente, _) in enumerate(self.tabela[indice]):
            if chave_existente == chave:
                del self.tabela[indice][i]
                break

    def __str__(self):
        """Retorna uma representação em string da tabela."""
        return str(self.tabela)

# Exemplo de uso
if __name__ == "__main__":
    tabela_hash = TabelaHash(10)

    tabela_hash.inserir("chave1", "valor1")
    tabela_hash.inserir("chave2", "valor2")
    tabela_hash.inserir("chave3", "valor3")

    print("Tabela Hash:", tabela_hash)

    print("Buscar chave1:", tabela_hash.buscar("chave1"))
    print("Buscar chave2:", tabela_hash.buscar("chave2"))
    print("Buscar chave3:", tabela_hash.buscar("chave3"))

    tabela_hash.remover("chave2")

    print("Tabela Hash após remoção:", tabela_hash)