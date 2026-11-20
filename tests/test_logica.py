from src.funcoes import calcular_pontos, jogador_chance, limitar_valor, verificar_resposta, mover_selecao, tempo_restante, tempo_acabou, proxima_rodada, rodadas_acabaram

def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando o total de vidas chega a zero."""
    assert jogador_perdeu(0) is True


def test_jogador_nao_perdeu_com_vidas():
    """Nao deve indicar derrota quando o jogador ainda tem vidas."""
    assert jogador_perdeu(3) is False


def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o limite minimo quando o valor informado for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o limite maximo quando o valor informado for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando ele ja estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50

# Rodada fictícia usada nos testes para verificar se a função identifica corretamente a imagem gerada por IA
RODADA = {"imagens": ["a.jpg", "b.jpg"], "ia": "b.jpg"}


def test_verificar_resposta_acerto():
    assert verificar_resposta(RODADA, 1) is True


def test_verificar_resposta_erro():
    assert verificar_resposta(RODADA, 0) is False


def test_mover_selecao_nao_passa_do_limite():
    assert mover_selecao(0, -1, 2) == 0
    assert mover_selecao(1, 1, 2) == 1
    assert mover_selecao(0, 1, 2) == 1

def test_tempo_restante_no_meio():
    """Deve devolver os segundos que sobram depois de 5 s decorridos (limite 15)."""
    assert tempo_restante(1000, 6000, 15) == 10


def test_tempo_restante_nunca_negativo():
    """Não deve passar de 0 mesmo se o tempo decorrido for maior que o limite."""
    assert tempo_restante(0, 30000, 15) == 0


def test_tempo_acabou():
    """Deve indicar fim de tempo só quando o restante chega a 0."""
    assert tempo_acabou(0) is True
    assert tempo_acabou(3.5) is False


def test_proxima_rodada():
    """Deve devolver o índice seguinte."""
    assert proxima_rodada(0) == 1


def test_rodadas_acabaram():
    """Deve indicar quando o índice passa da última rodada."""
    assert rodadas_acabaram(5, 5) is True
    assert rodadas_acabaram(4, 5) is False