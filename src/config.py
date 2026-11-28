# Configurações centrais do jogo (tela, cores, fontes e caminhos de arquivos).
LARGURA_TELA = 800
ALTURA_TELA = 600
FPS = 60
PONTOS_ACERTOS = 10
MULTIPLICADOR_BONUS = 5

TITULO_JOGO = "IA GAME"

# Cores (vermelho, verde, azul)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (212, 212, 212)
CINZA_ESCURO = (90, 90, 90)
AMARELO = (255, 215, 0)
VERDE = (60, 180, 75)
LARANJA = (245, 130, 48)
VERMELHO = (220, 50, 50)

COR_FUNDO = (205, 212, 225)      # usada se não houver imagem de fundo
COR_TEXTO = PRETO
COR_HUD = (40, 40, 60)            # faixa escura do topo
COR_TEXTO_HUD = BRANCO
COR_MOLDURA = AMARELO
COR_BARRA_FUNDO = CINZA_ESCURO
COR_BARRA_CHEIA = VERDE           # mais da metade do tempo
COR_BARRA_MEIO = LARANJA          # entre metade e um quarto
COR_BARRA_FIM = VERMELHO          # menos de um quarto

# Fontes (None = fonte padrão do pygame; pode trocar pelo caminho de um .ttf em assets/fontes)
FONTE = None
TAMANHO_FONTE_HUD = 30
TAMANHO_FONTE_TITULO = 56
TAMANHO_FONTE_TEXTO = 28

# Layout da tela
ALTURA_HUD = 50                   # altura da faixa de informações no topo
Y_BARRA_TEMPO = 62                # posição da barra de tempo
ALTURA_BARRA_TEMPO = 16
MARGEM = 30                       # margem das laterais e de baixo
ESPACO_IMAGENS = 30               # espaço entre uma imagem e outra
Y_IMAGENS = 100                   # onde começa a área das imagens
TAMANHO_MAX_IMAGEM = 340          # tamanho máximo do lado de cada imagem

TEMPO_RODADA = 10
CAMINHO_RECORDE = "data/recorde.txt"
CAMINHO_RODADAS = "data/rodada.json"
CAMINHO_FUNDO = "assets/imagens/fundo.png"   # opcional: se não existir, usa COR_FUNDO
