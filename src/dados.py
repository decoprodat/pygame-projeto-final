import json

def salvar_recorde(caminho_arquivo, pontuacao):
    """Salva a pontuação recorde em arquivo texto."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(str(pontuacao))

# O recorde é salvo diacordo com o acerto consecutivo 
def carregar_recorde(caminho_arquivo):
    """Carrega o recorde salvo; retorna 0 se não existir valor válido."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()

            if conteudo == "":
                return 0

            return float(conteudo)

    except FileNotFoundError:
        return 0


def carregar_rodada(caminho_arquivo):
    """Carrega a rodada ; retorna VAZIO se não existir RODADA."""
    
    try:
        
        with open (caminho_arquivo,"r", encoding="utf-8") as arquivo:

            conteudo = arquivo.read().strip()

            if conteudo == "":

                return []

            return json.loads(conteudo)


    except FileNotFoundError:

        return []

    except json.JSONDecodeError:

        print("Erro no Rodada.json")
     
        return []
 
def salvar_rodada(caminho_arquivo,rodada):

    with open(caminho_arquivo,"w", encoding="utf-8") as arquivo:

       json.dump(rodada,arquivo,ensure_ascii=False, indent=4)

    