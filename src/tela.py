import pygame

from src.config import (
    LARGURA_TELA, ALTURA_TELA, FONTE, TAMANHO_FONTE_HUD,
    COR_FUNDO, COR_HUD, COR_TEXTO_HUD, COR_MOLDURA,
    COR_BARRA_FUNDO, COR_BARRA_CHEIA, COR_BARRA_MEIO, COR_BARRA_FIM,
    ALTURA_HUD, Y_BARRA_TEMPO, ALTURA_BARRA_TEMPO, MARGEM,
    ESPACO_IMAGENS, Y_IMAGENS, TAMANHO_MAX_IMAGEM, CAMINHO_FUNDO,
)

# Tamanho das imagens quando a rodada tem 2 (o jogo.py já importa estes nomes)
LARGURA_IMG = TAMANHO_MAX_IMAGEM
ALTURA_IMG = TAMANHO_MAX_IMAGEM

_fontes = {}  # guarda as fontes já criadas para não recriar a cada quadro


def desenhar_texto(tela, texto, tamanho, cor, posicao, centralizado=False):
    """Escreve um texto na tela. Se centralizado=True, a posição é o centro do texto."""
    if tamanho not in _fontes:
        _fontes[tamanho] = pygame.font.Font(FONTE, tamanho)
    superficie = _fontes[tamanho].render(str(texto), True, cor)
    retangulo = superficie.get_rect()
    if centralizado:
        retangulo.center = posicao
    else:
        retangulo.topleft = posicao
    tela.blit(superficie, retangulo)


def carregar_imagem(caminho, largura, altura):
    """Abre uma imagem e deixa ela no tamanho pedido. Se não achar, devolve um quadrado cinza."""
    try:
        imagem = pygame.image.load(caminho).convert()
        return pygame.transform.smoothscale(imagem, (largura, altura))
    except (FileNotFoundError, pygame.error):
        print("Imagem não encontrada:", caminho)
        reserva = pygame.Surface((largura, altura))
        reserva.fill((120, 120, 120))
        return reserva


def carregar_fundo():
    """Carrega a imagem de fundo. Devolve None se ela não existir."""
    try:
        imagem = pygame.image.load(CAMINHO_FUNDO).convert()
        return pygame.transform.smoothscale(imagem, (LARGURA_TELA, ALTURA_TELA))
    except (FileNotFoundError, pygame.error):
        return None


def desenhar_fundo(tela, fundo=None):
    """Desenha a imagem de fundo ou, se não houver, pinta com a cor de fundo."""
    if fundo is None:
        tela.fill(COR_FUNDO)
    else:
        tela.blit(fundo, (0, 0))


def grade_imagens(quantidade):
    """Quantas colunas e linhas usar: até 3 imagens numa linha, 4 ou mais em 2 linhas."""
    colunas = quantidade if quantidade <= 3 else (quantidade + 1) // 2
    linhas = (quantidade + colunas - 1) // colunas
    return colunas, linhas


def tamanho_imagem(quantidade):
    """Lado (em pixels) de cada imagem para todas caberem na tela."""
    colunas, linhas = grade_imagens(quantidade)
    largura_livre = LARGURA_TELA - 2 * MARGEM - (colunas - 1) * ESPACO_IMAGENS
    altura_livre = ALTURA_TELA - Y_IMAGENS - MARGEM - (linhas - 1) * ESPACO_IMAGENS
    return min(largura_livre // colunas, altura_livre // linhas, TAMANHO_MAX_IMAGEM)


def retangulo_imagem(i, quantidade):
    """Retângulo (posição e tamanho) da imagem número i, com as linhas centralizadas."""
    colunas, linhas = grade_imagens(quantidade)
    lado = tamanho_imagem(quantidade)
    linha, coluna = i // colunas, i % colunas

    na_linha = min(colunas, quantidade - linha * colunas)  # a última linha pode ter menos
    largura_linha = na_linha * lado + (na_linha - 1) * ESPACO_IMAGENS
    x = (LARGURA_TELA - largura_linha) // 2 + coluna * (lado + ESPACO_IMAGENS)

    altura_bloco = linhas * lado + (linhas - 1) * ESPACO_IMAGENS
    altura_livre = ALTURA_TELA - Y_IMAGENS - MARGEM
    y = Y_IMAGENS + (altura_livre - altura_bloco) // 2 + linha * (lado + ESPACO_IMAGENS)
    return pygame.Rect(x, y, lado, lado)


def posicao_imagem(i, quantidade):
    """Calcula o x da imagem número i."""
    return retangulo_imagem(i, quantidade).x


def carregar_imagens_rodada(caminhos):
    """Carrega as imagens de uma rodada já no tamanho certo para a quantidade."""
    lado = tamanho_imagem(len(caminhos))
    return [carregar_imagem(caminho, lado, lado) for caminho in caminhos]


def desenhar_imagens(tela, imagens):
    """Desenha as imagens na tela (ajusta o tamanho se vierem diferentes)."""
    for i, imagem in enumerate(imagens):
        retangulo = retangulo_imagem(i, len(imagens))
        if imagem.get_size() != retangulo.size:
            imagem = pygame.transform.scale(imagem, retangulo.size)
        tela.blit(imagem, retangulo)


def desenhar_moldura(tela, selecionada, quantidade, cor=COR_MOLDURA):
    """Desenha uma borda em volta da imagem selecionada."""
    retangulo = retangulo_imagem(selecionada, quantidade).inflate(12, 12)
    pygame.draw.rect(tela, cor, retangulo, 5)


def imagem_clicada(posicao_mouse, quantidade):
    """Índice da imagem que está na posição do clique, ou None se não clicou em nenhuma."""
    for i in range(quantidade):
        if retangulo_imagem(i, quantidade).collidepoint(posicao_mouse):
            return i
    return None


def desenhar_hud(tela, pontos, chances, fase, recorde, rodada, total_rodadas):
    """Desenha a faixa do topo com pontos, chances, fase, rodada e recorde."""
    pygame.draw.rect(tela, COR_HUD, (0, 0, LARGURA_TELA, ALTURA_HUD))
    itens = [f"Pontos: {pontos}", f"Chances: {chances}", f"Fase: {fase}",
             f"Rodada: {rodada}/{total_rodadas}", f"Recorde: {recorde}"]
    coluna = LARGURA_TELA // len(itens)
    for i, texto in enumerate(itens):
        centro = (coluna * i + coluna // 2, ALTURA_HUD // 2)
        desenhar_texto(tela, texto, TAMANHO_FONTE_HUD, COR_TEXTO_HUD, centro, centralizado=True)


def desenhar_barra_tempo(tela, restante, total):
    """Barra que diminui com o tempo: verde, depois laranja, depois vermelha."""
    fracao = max(0, min(1, restante / total)) if total > 0 else 0
    largura_maxima = LARGURA_TELA - 2 * MARGEM
    pygame.draw.rect(tela, COR_BARRA_FUNDO,
                     (MARGEM, Y_BARRA_TEMPO, largura_maxima, ALTURA_BARRA_TEMPO), border_radius=8)

    if fracao > 0.5:
        cor = COR_BARRA_CHEIA
    elif fracao > 0.25:
        cor = COR_BARRA_MEIO
    else:
        cor = COR_BARRA_FIM
    largura = int(largura_maxima * fracao)
    if largura > 0:
        pygame.draw.rect(tela, cor,
                         (MARGEM, Y_BARRA_TEMPO, largura, ALTURA_BARRA_TEMPO), border_radius=8)
