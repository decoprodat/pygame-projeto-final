# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na etapa inicial do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com **Python e Pygame** dentro do prazo disponível. Consulte o enunciado publicado no Canvas para conhecer o eixo temático e as orientações vigentes.

## 1. Nome provisório do jogo

Informe o nome provisório do jogo.

**Nome:**

> IA GAME 

## 2. Integrantes do grupo

- Nome 1: Andre Luiz Pinheiro Lopes
- Nome 2: Diego Ribeiro Gil
- Nome 3: Gabriel Tavares
- Nome 4: Samuel Abreu

## 3. Tema escolhido

Indique qual tema específico o grupo escolheu **dentro do eixo temático definido no enunciado**.

**Tema:**

> Conteúdos reais e artificiais: reconhecimento de sinais que indicam que uma imagem foi gerada por Inteligência Artificial.

**Como esse tema se relaciona com o jogo?** Explique brevemente (2 a 4 linhas) como ele aparecerá nos objetivos, nas regras ou nos desafios, e não apenas nas imagens ou no cenário.

> O tema é a própria mecânica do jogo: a cada rodada, o jogador precisa descobrir, entre duas ou mais imagens, qual foi gerada por IA. Acertar vai passando de etapa e errar vai diminuindo as chances. Depois de cada resposta, o jogo mostra a pista e a dificuldade aumenta com mais imagens por rodada e menos tempo para responder.

**Aspecto de uso responsável abordado:**

> O jogo trabalha três aspectos do uso responsável da IA, todos ligados diretamente às regras:
>
> - **Análise crítica dos resultados:** o jogador precisa observar os detalhes com atenção antes de decidir, em vez de confiar na primeira impressão, o mesmo cuidado necessário antes de acreditar em uma imagem ou compartilhá-la.
> - **Transparência:** após cada resposta, o jogo revela qual era a imagem de IA e explica a pista que a denunciava (dedos deformados, textos sem sentido, sombras incoerentes, fundos distorcidos), ensinando o jogador a reconhecer esses sinais.
> - **Confiabilidade da informação:** nos níveis mais altos, as imagens ficam mais difíceis de distinguir, mostrando que conteúdos gerados por IA podem ser muito realistas e que nem tudo o que parece verdadeiro é real.

**Relevância do tema:**

> Imagens geradas por IA estão cada vez mais realistas e circulam todos os dias em redes sociais, notícias e anúncios. Elas podem ser usadas para enganar, desinformar ou manipular opiniões. Saber identificar sinais de conteúdo artificial e analisar o que se vê antes de acreditar ou compartilhar é uma habilidade importante no cotidiano, e o jogo treina isso de forma prática e divertida.

## 4. Tipo de jogo

Indique o estilo do jogo. Exemplos: desviar de obstáculos, coleta de itens, labirinto, perguntas e respostas, memória, Pong, Snake, Breakout, corrida ou sobrevivência simples.

**Tipo escolhido:**

> Perguntas e respostas visual (jogo de observação), com tempo limite, vidas e níveis de dificuldade.

## 5. Descrição geral do jogo

Explique, em poucas linhas, como o jogo funcionará. O que aparece na tela? O que o jogador controla? O que ele precisa fazer e quais desafios encontrará?

**Descrição:**

> Na tela aparecem duas ou mais imagens lado a lado, além da pontuação, das chances,da fase, teremos também o recorde de maior sequenciência acertada e por fim um tempo para o jogador responder. Apenas uma das imagens foi gerada por IA, e as outras são fotos reais. O jogador controla uma moldura de seleção, movendo-a entre as imagens com as setas ou clicando com o mouse, e confirma a imagem que acredita ser artificial. Depois da resposta, o jogo revela a imagem correta e mostra a pista que a denunciava. O desafio aumenta a cada fase: aparecem mais imagens por rodada, o tempo para responder diminui e as imagens ficam mais parecidas, dependendo da fase mudando apenas detalhes.

## 6. Objetivo do jogador

Descreva o objetivo principal. Por exemplo: coletar itens, sobreviver por determinado tempo, chegar ao final de um percurso ou completar desafios.

**Objetivo:**

> Identificar corretamente a imagem gerada por IA no maior número possível de rodadas, sem perder todas as chances. O jogador vence ao completar todas as rodadas e tenta fazer a maior pontuação possível para bater o recorde.

## 7. Regras principais

Liste até cinco regras que expliquem o funcionamento do jogo. Exemplos: o jogador começa com três vidas; acertos somam pontos; colisões retiram vidas.

- Regra 1: A cada rodada aparecem várias imagens, e apenas uma foi gerada por IA; o jogador deve escolher qual é ela antes que o tempo acabe.
- Regra 2: Cada acerto vale 10 pontos mais um bônus pelo tempo que sobrou, e acertos seguidos aumentam um multiplicador de pontos.
- Regra 3: O jogador começa com 2 chances por fase e perde uma a cada erro ou quando o tempo acaba sem resposta.
- Regra 4: Após cada resposta, o jogo mostra qual era a imagem de IA.
- Regra 5: O jogo tem 3 níveis, com 10, 10 e 20 imagens por rodada e menos tempo a cada nível.

## 8. Condição de vitória

Explique como o jogador vence ou conclui a partida. Exemplos: alcançar uma pontuação, finalizar uma fase ou completar todas as tarefas.

**Condição de vitória:**

> O jogador vence ao completar todas as rodadas dos 3 níveis sem perder todas as chances. Ao final, é exibido um relatório com a pontuação, a quantidade de acertos e erros e a maior sequência de acertos, e se a pontuação superar o recorde salvo em arquivo, o recorde é atualizado.

## 9. Condição de derrota ou encerramento

Explique quando a partida termina ou como o jogador perde. Exemplos: esgotar as vidas, acabar o tempo ou atingir o limite de erros.

**Condição de derrota ou encerramento:**

> O jogador perde quando fica sem chances, ou seja, ao errar duas vezes (incluindo rodadas em que o tempo acabou sem resposta). O jogador também pode encerrar o jogo a qualquer momento pressionando ESC. Ao final, a pontuação é comparada com o recorde salvo.

## 10. Elementos previstos no jogo

Descreva brevemente os elementos mais importantes, sem precisar detalhar a implementação.

- **Personagem ou elemento principal:** uma moldura de seleção que o jogador move entre as imagens para escolher a que acredita ser gerada por IA.
- **Obstáculos ou desafios:** o tempo limite de cada rodada e imagens cada vez mais realistas e numerosas a cada nível.
- **Itens ou objetos de interação:** as imagens de cada rodada (fotos reais e uma imagem gerada por IA) e a tela de pista exibida após cada resposta.
- **Pontuação, vidas, tempo ou progresso:** pontuação, multiplicador por acertos seguidos, 3 chances, barra de tempo, nível atual, número da rodada e recorde salvo em arquivo.

## 11. Controles previstos

Informe como o jogador vai interagir com o jogo (por exemplo, setas para movimentar, espaço para agir ou mouse para selecionar).

**Controles:**

> Setas para esquerda e direita movem a seleção entre as imagens; Enter ou Espaço confirmam a escolha; o clique do mouse escolhe uma imagem diretamente; Enter na tela de pista avança para a próxima rodada; ESC sai do jogo.

## 12. Principais dificuldades esperadas

Cite até três dificuldades que o grupo espera enfrentar. Exemplos: movimentação, colisões, controle de tempo, testes ou uso do GitHub.

- Dificuldade 1: Reunir imagens reais com licença livre e gerar imagens de IA parecidas com elas, registrando corretamente a origem de cada uma.
- Dificuldade 2: Carregar, redimensionar e posicionar as imagens na tela de acordo com a quantidade de cada nível, além de controlar o tempo de cada rodada.
- Dificuldade 3: Organizar o trabalho em grupo no GitHub e escrever testes para as funções de lógica do jogo.
- Dificuldade 4: Encontrar um jogo intuitivo, interessante que coubesse na proposta e também que todos estivessem de acordo com a ideia.  
## 13. Escopo mínimo para a entrega final

Descreva a **versão mais simples que já seria jogável**, com as interações e regras essenciais. Evite planejar funcionalidades demais.

**Escopo mínimo:**

> Pelo menos 30 rodadas carregadas de um arquivo em `data/`, divididas em 3 níveis (10, 20 e 30 imagens). O jogador escolhe a imagem de IA com as setas e o Enter, com tempo limite por rodada. Acertos somam pontos, erros tiram vidas, e após cada resposta aparece a pista. A partida termina ao completar todas as rodadas ou perder as 3 vidas, e o recorde é salvo em arquivo.

## 14. Possíveis melhorias, caso haja tempo

Liste até três funcionalidades extras para implementar somente depois que a versão mínima estiver funcionando. Exemplos: sons, fases, ranking, animações ou menu inicial.

- Melhoria 1: Menu inicial com instruções e tela de fim de jogo com opção de reiniciar a partida.
- Melhoria 2: Ranking com as 5 melhores pontuações e o nome do jogador, salvo em arquivo.
- Melhoria 3: Efeitos sonoros de acerto e erro, e animação ao revelar a imagem gerada por IA.

## 15. Organização inicial do código

O grupo vai manter a estrutura de arquivos do template, adaptando cada módulo:

- `main.py`: ponto de entrada; apenas chama a função que inicia o jogo.
- `src/config.py`: constantes do jogo (tamanho da tela, cores, FPS, tempo por nível, número de vidas e caminhos dos arquivos).
-`src/jogo.py`: loop principal (eventos, atualização e desenho) e controle das telas (rodada, pista e fim de jogo).
- `src/funcoes.py`: funções de lógica, como verificar a resposta, calcular pontos e bônus de tempo, controlar vidas, sequência de acertos e nível. Funções do template como `calcular_pontos`, `tomar_dano` e `jogador_perdeu` serão reaproveitadas.
- `src/dados.py`: leitura das rodadas a partir de `data/rodadas.json` e leitura e gravação do recorde em `data/recorde.txt`.
- `src/sprites.py`: carregamento e redimensionamento das imagens de cada rodada.
- `tests/test_logica.py`: testes com `pytest` para as funções de `funcoes.py` e `dados.py`.

## 16. Recursos previstos

> Fotos reais de sites com licença livre (propria biblioteca dos desenvolvedores do jogo, ou Unsplash, Pexels e Wikimedia Commons), sem pessoas identificáveis, e imagens geradas por uma ferramenta de IA de geração de imagens. Todas as imagens terão sua origem, autor, licença ou ferramenta utilizada registrados na seção "Recursos externos utilizados" do README.md.

## 17. Declaração de originalidade

> Declaramos que este projeto é de autoria do grupo, desenvolvido especificamente para esta disciplina a partir do template oficial. Ele não reutiliza jogos de semestres anteriores nem é cópia de tutoriais ou repositórios prontos. Qualquer código, imagem, som ou fonte externa utilizada será devidamente referenciada no README.md.