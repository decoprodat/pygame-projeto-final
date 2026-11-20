import pygame

LARGURA_IMG = 340
ALTURA_IMG = 340
ESPACO = 40         
Y_IMAGENS = 130      
COR_MOLDURA = (255, 215, 0)   # amarelo (vermelho, verde, azul)


def carregar_imagem(caminho, largura, altura):
    """Abre uma imagem e deixa ela no tamanho pedido."""
    try:
        imagem = pygame.image.load(caminho).convert()
        imagem = pygame.transform.smoothscale(imagem, (largura, altura))
        return imagem
    except FileNotFoundError:
        print("Imagem não encontrada:", caminho)
        reserva = pygame.Surface((largura, altura))
        reserva.fill((120, 120, 120))
        return reserva


def posicao_imagem(i, quantidade):
    """Calcula o x da imagem número i (0, 1, 2...) para ficarem centralizadas."""
    largura_total = quantidade * LARGURA_IMG + (quantidade - 1) * ESPACO
    x_inicial = (800 - largura_total) // 2
    return x_inicial + i * (LARGURA_IMG + ESPACO)


def desenhar_imagens(tela, imagens):
    """Desenha as imagens lado a lado na tela."""
    for i in range(len(imagens)):
        x = posicao_imagem(i, len(imagens))
        tela.blit(imagens[i], (x, Y_IMAGENS))

def desenhar_moldura(tela, selecionada, quantidade):
    """Desenha uma borda em volta da imagem selecionada."""
    x = posicao_imagem(selecionada, quantidade)
    retangulo = pygame.Rect(x, Y_IMAGENS, LARGURA_IMG, ALTURA_IMG)
    retangulo = retangulo.inflate(12, 12)
    pygame.draw.rect(tela, COR_MOLDURA, retangulo, 5)



if __name__ == "__main__":
    pygame.init()
    tela = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Teste da tela")
    relogio = pygame.time.Clock()

    imagens = [
        carregar_imagem("assets/imagens/fase1/r2.IA.png", LARGURA_IMG, ALTURA_IMG),
        carregar_imagem("assets/imagens/fase1/r2.Real.jpg", LARGURA_IMG, ALTURA_IMG),
    ]
    selecionada = 0

    rodando = True
    while rodando:
        relogio.tick(60)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    selecionada = 0
                elif evento.key == pygame.K_RIGHT:
                    selecionada = 1

        tela.fill((212, 212, 212))
        desenhar_imagens(tela, imagens)
        desenhar_moldura(tela, selecionada, len(imagens))
        pygame.display.flip()

    pygame.quit()
