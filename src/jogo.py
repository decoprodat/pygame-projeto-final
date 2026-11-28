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
    PONTOS_ACERTOS,
    MULTIPLICADOR_BONUS,
    VERDE,
    VERMELHO,
    COR_TEXTO,
    TAMANHO_FONTE_TEXTO
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
    tempo_fase,
    calcular_bonus,
    sequencia_acertos,
    multiplicador_pontos
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
    desenhar_texto,
    imagem_clicada,
    desenhar_relatorio,
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
    chance = 3
    recorde = carregar_recorde(CAMINHO_RECORDE)

    rodadas = carregar_rodada(CAMINHO_RODADAS)
    if not rodadas:
        print("Nenhuma rodada encontrada.")
        pygame.quit()
        return

    indice_rodada = 0                 # qual a rodada que está sendo jogada
    rodada = rodadas[indice_rodada]   # a rodada atual
    imagens = carregar_imagens(rodada) 
    sequencia = 0
    selecionada = 0                   # qual imagem está marcada

    mostrando_pista = False   # True quando a pista está na tela
    escolhida = None          # imagem que o jogador escolheu

    acertos = 0
    erros = 0
    fim_de_jogo = False       # True quando o relatório tá na tela

    inicio_rodada = pygame.time.get_ticks()   # vai pegar o instante (EM MS, NÃO EM SEGS) em que a rodada começou

    # Loop principal: processa entrada, atualiza estado e renderiza a cena.
    while rodando:
        relogio.tick(FPS)

        avancar = False #vai virar true quando a rodada terminar 
        # Cronômetro: calcula quanto tempo ainda resta na rodada
        if not mostrando_pista:
            restante = tempo_restante(inicio_rodada, pygame.time.get_ticks(), tempo_fase(rodada["fase"]))

        for evento in pygame.event.get():
            confirmou = False  # vira True quando o jogador responde (teclado ou clique)

            if evento.type == pygame.QUIT:
                rodando = False

            # Verifica se alguma tecla foi pressionada
            if evento.type == pygame.KEYDOWN:

                # ESC: encerra o jogo
                if evento.key == pygame.K_ESCAPE:
                    rodando = False

                # Na tela de pista, só o Enter e o ESC funcionam
                elif mostrando_pista:
                    if evento.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                        avancar = True

                # Seta esquerda: seleciona a imagem anterior
                elif evento.key == pygame.K_LEFT:
                    selecionada = mover_selecao(selecionada, -1, len(rodada["imagens"]))

                # Seta direita: seleciona a próxima imagem
                elif evento.key == pygame.K_RIGHT:
                    selecionada = mover_selecao(selecionada, 1, len(rodada["imagens"]))

                # Enter ou Espaço: confirma a imagem escolhida
                elif evento.key in (pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_SPACE):
                    confirmou = True

            # Clique com o botão esquerdo do mouse (botão 1)
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and not mostrando_pista:
                clicada = imagem_clicada(evento.pos, len(imagens))

                if clicada is not None:  # o clique foi em cima de uma imagem
                    selecionada = clicada
                    confirmou = True

            # Confere a resposta
            if confirmou:
                acertou = verificar_resposta(rodada, selecionada)
                escolhida = selecionada
                mostrando_pista = True

                if acertou:
                    acertos = acertos + 1
                    # int tira as casas decimais do bônus
                    pontos = calcular_pontos(pontos, PONTOS_ACERTOS + int(calcular_bonus(restante, MULTIPLICADOR_BONUS)))
                else:
                    erros = erros + 1
                    chance = errar(chance, 1)
                    print("Errou!")

        # Se o tempo acabou sem resposta, conta como erro e tira uma chance
        if not mostrando_pista and tempo_acabou(restante):
            print("Tempo esgotado!")
            erros = erros + 1
            chance = errar(chance, 1)
            escolhida = None
            mostrando_pista = True
        # olha se o jogador tem chance, se sim, passa, se não, não passa
        if avancar and not jogador_chance(chance):
            indice_rodada = proxima_rodada(indice_rodada)

            # Acabaram as rodadas: encerra o jogo (a tela de fim fica para a Tarefa 3)
            if rodadas_acabaram(indice_rodada, len(rodadas)):
                fim_de_jogo = True
            else:
                rodada = rodadas[indice_rodada]                 # carrega a nova rodada
                imagens = carregar_imagens(rodada)
                selecionada = 0                                 # volta a seleção para a primeira imagem
                inicio_rodada = pygame.time.get_ticks()         # reinicia o cronômetro
                restante = tempo_fase(rodada["fase"])
                mostrando_pista = False
        # Regras de fim de jogo e recorde
        if avancar and jogador_chance(chance):
            fim_de_jogo = True

        if pontos > recorde:
            recorde = pontos
            salvar_recorde(CAMINHO_RECORDE, recorde)


        pygame.display.set_caption(
            f"{TITULO_JOGO} | Pontos: {pontos} | Recorde: {recorde} | chance: {chance} | Acertos {sequencia}"
        )

        tela.fill(CINZA)
        desenhar_imagens(tela,imagens)
        if fim_de_jogo:
            tela.fill(CINZA)  # apaga as imagens para mostrar o relatório
            desenhar_relatorio(tela, pontos, acertos, erros, recorde)
        elif mostrando_pista:
            indice_ia = rodada["imagens"].index(rodada["ia"])  # posição da imagem de IA
            desenhar_moldura(tela, indice_ia, len(imagens), VERDE)

            if escolhida is not None and escolhida != indice_ia:  # escolheu uma imagem errada
                desenhar_moldura(tela, escolhida, len(imagens), VERMELHO)

            desenhar_texto(tela, rodada["pista"], TAMANHO_FONTE_TEXTO, COR_TEXTO, (LARGURA_TELA // 2, 550), True)
        else:
            desenhar_moldura(tela,selecionada,len(imagens))
        pygame.display.flip()


    pygame.quit()