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


