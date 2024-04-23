from collections import deque

# Classe para representar o estado do tabuleiro em um determinado momento
class EstadoTabuleiro:
    def __init__(self, tabuleiro, rainhas_colocadas=[]):
        self.tabuleiro = tabuleiro  # Representa o estado atual do tabuleiro
        self.rainhas_colocadas = rainhas_colocadas  # Lista das posições das rainhas

    # Verifica se é possível colocar uma rainha na posição especificada
    def valida_posicao(self, linha, coluna):
        for rainha_linha, rainha_coluna in self.rainhas_colocadas:
            if (linha == rainha_linha or coluna == rainha_coluna or
                    abs(linha - rainha_linha) == abs(coluna - rainha_coluna)):
                return False
        return True

    # Gera todos os possíveis estados do tabuleiro após colocar uma nova rainha
    def expandir(self):
        proximos_estados = []
        linha = len(self.rainhas_colocadas)
        for coluna in range(len(self.tabuleiro)):
            if self.valida_posicao(linha, coluna):
                novo_tabuleiro = [linha[:] for linha in self.tabuleiro]
                novo_tabuleiro[linha][coluna] = "Q"  # Coloca uma nova rainha no tabuleiro
                proximos_estados.append(
                    EstadoTabuleiro(novo_tabuleiro, self.rainhas_colocadas + [(linha, coluna)]))
        return proximos_estados

    # Verifica se o estado atual é o estado objetivo (todas as rainhas estão colocadas)
    def objetivo_alcancado(self):
        return len(self.rainhas_colocadas) == len(self.tabuleiro)

    # Método especial para imprimir o tabuleiro
    def __str__(self):
        return '\n'.join([' '.join(linha) for linha in self.tabuleiro])


# Função para a busca em largura
def busca_largura(estado_inicial):
    fila = deque([estado_inicial])

    while fila:
        estado_atual = fila.popleft()
        if estado_atual.objetivo_alcancado():
            return estado_atual
        fila.extend(estado_atual.expandir())

    return None


# Função para a busca em profundidade
def busca_profundidade(estado_atual):
    pilha = [estado_atual]

    while pilha:
        estado_atual = pilha.pop()
        if estado_atual.objetivo_alcancado():
            return estado_atual
        pilha.extend(estado_atual.expandir())

    return None


# Função principal para resolver o problema das Oito Rainhas
def resolver_oito_rainhas(tamanho_tabuleiro, busca='largura'):
    tabuleiro = [['.' for _ in range(tamanho_tabuleiro)] for _ in range(tamanho_tabuleiro)]
    estado_inicial = EstadoTabuleiro(tabuleiro)
    if busca == 'largura':
        resultado = busca_largura(estado_inicial)
    elif busca == 'profundidade':
        resultado = busca_profundidade(estado_inicial)
    else:
        raise ValueError("Tipo de busca inválido. Escolha entre 'largura' e 'profundidade'.")
    
    if resultado:
        print("Solução encontrada:")
        print(resultado)
    else:
        print("Nenhuma solução encontrada.")

# Função principal
def main():
    tamanho_tabuleiro = int(input("Digite o tamanho do tabuleiro (por exemplo, 8 para um tabuleiro 8x8): "))
    busca = input("Digite o tipo de busca desejado (largura ou profundidade): ").lower()
    resolver_oito_rainhas(tamanho_tabuleiro, busca)

if __name__ == "__main__":
    main()