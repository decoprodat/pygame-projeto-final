def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos


def errar(vida_atual, erro):
    """Reduz a quantidade de chances atual com base no erro recebido que é automaticamente 1, de 1 em 1."""
    return vida_atual - erro


def jogador_chance(chance):
    """Indica se o jogador ficou sem chances."""
    return chance <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_resposta(rodada, indice_escolhido):
    """esse retorna True se a imagem escolhida é a gerada por IA."""
    return rodada["imagens"][indice_escolhido] == rodada["ia"]


def mover_selecao(selecionada, direcao, total_imagens):
    """Move a seleção (-1 = esquerda, +1 = direita) sem sair dos limites"""
    return limitar_valor(selecionada + direcao, 0, total_imagens - 1)

def tempo_restante(inicio_ms, agora_ms, limite_segundos):
    """Calcula quantos segundos ainda restam na rodada"""
    decorrido = (agora_ms - inicio_ms) / 1000   # milissegundos para segundos
    return limitar_valor(limite_segundos - decorrido, 0, limite_segundos)

def tempo_acabou(restante):
    """Indica se o tempo da rodada chegou a zero."""
    return restante <= 0


def proxima_rodada(indice_rodada):
    """Devolve o número da próxima rodada."""
    return indice_rodada + 1

def rodadas_acabaram(indice_rodada, total_rodadas):
    """Indica se o índice já passou da última rodada."""
    return indice_rodada >= total_rodadas