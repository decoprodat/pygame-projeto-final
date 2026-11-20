from src.funcoes import calcular_pontos, jogador_chance, limitar_valor, verificar_resposta, mover_selecao

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