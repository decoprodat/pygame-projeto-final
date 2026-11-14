# IA GAME

Projeto final da disciplina de Introdução a Algoritmos/Programação (PUC Minas), desenvolvido com Python e Pygame.

## Integrantes do grupo

- Andre Luiz Pinheiro Lopes
- Diego Ribeiro Gil
- Gabriel Tavares
- Samuel Abreu

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, rodadas e dados).
- `assets/`: imagens reais, imagens geradas por IA, fontes e sons.
- `data/`: arquivos persistentes (banco de rodadas e recorde).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

IA GAME é um jogo de observação em que o jogador precisa descobrir qual imagem foi gerada por Inteligência Artificial. A cada rodada, aparecem na tela duas ou mais imagens parecidas: apenas uma delas foi criada por IA, e as outras são fotos reais. O jogador escolhe a imagem que acredita ser artificial antes que o tempo acabe. Acertos somam pontos e erros tiram vidas. Depois de cada resposta, o jogo revela a imagem correta e mostra uma pista que denunciava a IA, como dedos deformados, textos sem sentido, sombras incoerentes ou fundos distorcidos. Conforme o jogador avança de nível, aumenta o número de imagens por rodada e diminui o tempo para responder.

## Tema: IA no cotidiano e uso responsável

O jogo aborda o tema **conteúdos reais e artificiais**. Imagens geradas por IA estão cada vez mais realistas e circulam todos os dias em redes sociais, notícias e anúncios, podendo ser usadas para enganar ou desinformar. O jogo treina o jogador a observar os detalhes com atenção e a analisar criticamente o que vê antes de acreditar ou compartilhar (análise crítica). Após cada resposta, ele mostra a pista que denunciava a imagem artificial (transparência), e nos níveis mais altos as imagens ficam mais difíceis de distinguir, mostrando que nem tudo o que parece verdadeiro é real (confiabilidade da informação).

## Objetivo do jogador

Identificar corretamente a imagem gerada por IA no maior número possível de rodadas, sem perder todas as vidas. O jogador vence ao completar todas as rodadas e tenta fazer a maior pontuação possível para bater o recorde.

## Regras do jogo

- A cada rodada, aparecem na tela várias imagens, e apenas uma delas foi gerada por IA.
- O jogador deve escolher a imagem que acredita ter sido gerada por IA.
- Cada rodada tem um tempo limite; se o tempo acabar sem resposta, conta como erro.
- Cada acerto vale 10 pontos, mais um bônus pelo tempo que sobrou.
- Acertos seguidos aumentam um multiplicador de pontos; um erro zera a sequência.
- O jogador começa com 3 vidas e perde uma a cada erro.
- Após cada resposta, o jogo mostra qual era a imagem de IA e a pista que a denunciava.
- O jogo tem 3 níveis: no nível 1 aparecem 2 imagens, no nível 2 aparecem 3 e no nível 3 aparecem 4, com menos tempo por rodada.
- O jogador vence ao completar todas as rodadas e perde ao ficar sem vidas.
- Ao final, a pontuação é comparada com o recorde salvo em arquivo.

## Controles

- Seta para esquerda e seta para direita: mover a seleção entre as imagens
- Enter ou Espaço: confirmar a escolha
- Clique do mouse: escolher uma imagem diretamente
- Enter (na tela de pista): ir para a próxima rodada
- ESC: sair do jogo

## Como executar o projeto

```bash
git clone https://github.com/decoprodat/pygame-projeto-final.git
cd pygame-projeto-final
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Recursos externos utilizados

### Imagens reais

| Arquivo | Origem | Autor | Licença |
|---|---|---|---|
| `assets/imagens/real/exemplo.jpg` | Unsplash / Pexels / Wikimedia Commons (link) | Nome do autor | Licença |

### Imagens geradas por IA

| Arquivo | Ferramenta utilizada | Data de geração |
|---|---|---|
| `assets/imagens/ia/exemplo.png` | Nome da ferramenta | dd/mm/aaaa |

### Outros recursos

Nenhum até o momento.

## Decisões técnicas

- O projeto mantém a estrutura do template da disciplina (`config.py`, `jogo.py`, `funcoes.py`, `dados.py` e `sprites.py`), organizada em funções e dicionários.
- As rodadas ficam no arquivo `data/rodadas.json`. Cada rodada é um dicionário com o caminho das imagens, qual delas é a de IA, o nível e a pista explicativa. Assim, novas rodadas podem ser adicionadas sem alterar o código.
- As imagens de cada rodada são embaralhadas com `random.shuffle`, para que a imagem de IA não apareça sempre na mesma posição.
- O recorde é salvo em `data/recorde.txt`, usando as funções `salvar_recorde` e `carregar_recorde` do template.
- As fotos reais foram escolhidas sem pessoas identificáveis (paisagens, animais, comidas e objetos), para evitar problemas de direitos de imagem.
- A lógica do jogo (verificar resposta, calcular pontos, controlar vidas e níveis) fica separada do desenho na tela, para facilitar os testes com `pytest`.