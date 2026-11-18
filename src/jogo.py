import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    CINZA,
    CAMINHO_RECORDE,

)

from src.funcoes import (
    calcular_pontos,
    jogador_chance,
    limitar_valor,
    errar
)
from src.dados import (
    salvar_recorde,
    carregar_recorde,
    carregar_rodada,
    salvar
)


def executar_jogo():
    """Executa o loop principal do jogo e controla estado, pontuações, erros e acertos."""
    pygame.init()
    

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    rodando = True
    
    pontos = 0
    chance = 3
    recorde = carregar_recorde(CAMINHO_RECORDE)

    # Loop principal: processa entrada, atualiza estado e renderiza a cena.
    while rodando:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        # Regras de fim de jogo e recorde
        if errar(chance):
            rodando = False

        if pontos > recorde:
            recorde = pontos
            salvar_recorde(CAMINHO_RECORDE, recorde)

        pygame.display.set_caption(
            f"{TITULO_JOGO} | Pontos: {pontos} | Recorde: {recorde} | chance: {chance}"
        )

        tela.fill(CINZA)


    pygame.quit()