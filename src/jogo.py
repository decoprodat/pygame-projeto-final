import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    CINZA,
    CAMINHO_RECORDE,
    CAMINHO_RODADAS,
    TEMPO_RODADA,
)

from src.funcoes import (
    calcular_pontos,
    jogador_chance,
    limitar_valor,
    errar,
    verificar_resposta,
    mover_selecao,
    tempo_restante,
    tempo_acabou,
    proxima_rodada,
    rodadas_acabaram,
)

from src.funcoes import (
    calcular_pontos,
    jogador_chance,
    limitar_valor,
    errar,
    verificar_resposta,
    mover_selecao,
    tempo_fase
)
from src.dados import (
    salvar_recorde,
    carregar_recorde,
    carregar_rodada,
    salvar_rodada
)

from src.tela import(

    carregar_imagem,
    posicao_imagem,
    desenhar_imagens,
    desenhar_moldura,
    LARGURA_IMG,
    ALTURA_IMG
    
    
)

def carregar_imagens(rodada):

    """Carrega as imagens"""

    lista_imagens = []

    for img in rodada["imagens"]:

        lista_imagens.append(carregar_imagem(img,LARGURA_IMG,ALTURA_IMG))


    return lista_imagens



def executar_jogo():
    """Executa o loop principal do jogo e controla estado, pontuações, erros e acertos."""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    rodando = True
    
    pontos = 0
    chance = 2
    recorde = carregar_recorde(CAMINHO_RECORDE)

    rodadas = carregar_rodada(CAMINHO_RODADAS)
    if not rodadas:
        print("Nenhuma rodada encontrada.")
        pygame.quit()
        return

    indice_rodada = 0                 # qual a rodada que está sendo jogada
    rodada = rodadas[indice_rodada]   # a rodada atual
    imagens = carregar_imagens(rodada) 
    selecionada = 0                   # qual imagem está marcada

    inicio_rodada = pygame.time.get_ticks()   # vai pegar o instante (EM MS, NÃO EM SEGS) em que a rodada começou

    # Loop principal: processa entrada, atualiza estado e renderiza a cena.
    while rodando:
        relogio.tick(FPS)

        avancar = False #vai virar true quando a rodada terminar 

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            # Verifica se alguma tecla foi pressionada
            if evento.type == pygame.KEYDOWN:

                # ESC: encerra o jogo
                if evento.key == pygame.K_ESCAPE:
                    rodando = False

                # Seta esquerda: seleciona a imagem anterior
                elif evento.key == pygame.K_LEFT:
                    selecionada = mover_selecao(selecionada, -1, len(rodada["imagens"]))

                # Seta direita: seleciona a próxima imagem
                elif evento.key == pygame.K_RIGHT:
                    selecionada = mover_selecao(selecionada, 1, len(rodada["imagens"]))

                # Enter ou Espaço: confirma a imagem escolhida
                elif evento.key in (pygame.K_RETURN, pygame.K_SPACE):
                    acertou = verificar_resposta(rodada, selecionada)
                    if not acertou:
                        chance = errar(chance, 1)
                    
                    avancar = True

                    # Vai exibir o resultado no terminal
                    if acertou:
                        print("Acertou!")
                    else:
                        print("Errou!")
        # Cronômetro: calcula quanto tempo ainda resta na rodada
        restante = tempo_restante(inicio_rodada, pygame.time.get_ticks(), tempo_fase(rodada["fase"]))

        # Se o tempo acabou sem resposta, conta como erro e tira uma chance
        if not avancar and tempo_acabou(restante):
            print("Tempo esgotado!")
            chance = errar(chance, 1)
            avancar = True

        # olha se o jogador tem chance, se sim, passa, se não, não passa
        if avancar and not jogador_chance(chance):
            indice_rodada = proxima_rodada(indice_rodada)

            # Acabaram as rodadas: encerra o jogo (a tela de fim fica para a Tarefa 3)
            if rodadas_acabaram(indice_rodada, len(rodadas)):
                rodando = False
            else:
                rodada = rodadas[indice_rodada]                 # carrega a nova rodada
                imagens = carregar_imagens(rodada)
                selecionada = 0                                 # volta a seleção para a primeira imagem
                inicio_rodada = pygame.time.get_ticks()         # reinicia o cronômetro
                restante = tempo_fase(rodada["fase"])
        # Regras de fim de jogo e recorde
        if jogador_chance(chance):
            rodando = False

        if pontos > recorde:
            recorde = pontos
            salvar_recorde(CAMINHO_RECORDE, recorde)

        pygame.display.set_caption(
            f"{TITULO_JOGO} | Pontos: {pontos} | Recorde: {recorde} | chance: {chance}"
        )

        tela.fill(CINZA)
        desenhar_imagens(tela,imagens)
        desenhar_moldura(tela,selecionada,len(imagens)) 
        pygame.display.flip()


    pygame.quit()