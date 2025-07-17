# Desafio Individual EDROM - Robô A*

Olá, candidato(a)!

Seja bem-vindo(a) ao desafio individual para a equipe de Robótica da EDROM. Este desafio foi projetado para avaliar suas habilidades de resolução de problemas, sua lógica de programação e seu conhecimento em algoritmos fundamentais para a robótica.

Caso tenha dúvidas sobre qualquer coisa, envie uma mensagem em algum dos seguintes canais:
- E-mail: pedrohperescode@gmail.com
- E-mail: victorvasconcelos676@gmail.com
- Grupo do Whatsapp


## O Desafio

O seu objetivo é programar a "inteligência" de um robô de futebol para que ele navegue em um campo 2D. A tarefa consiste em duas fases:
1.  Levar o robô de sua posição inicial até a bola, desviando de robôs adversários.
2.  Após capturar a bola, levá-la até o gol adversário para marcar o ponto da vitória.

O caminho encontrado deve ser **ótimo**, não apenas em distância, mas considerando diversas outras variáveis de custo que simulam um ambiente de jogo real.

## Estrutura dos Arquivos

Você recebeu uma pasta com dois arquivos de código principais. Aqui está um resumo do que cada um faz:

### 📄 `simulador.py` (O Simulador)

Este arquivo é o ambiente de simulação. Ele é responsável por:
-   Criar a janela do jogo e desenhar o campo, o robô, a bola e os obstáculos.
-   Gerenciar o loop principal do jogo e a interface (botões de Play/Reset).
-   Chamar a sua função no arquivo `candidato.py` para obter o caminho que o robô deve seguir.

**Importante:** Você não precisa (e não deve) editar este arquivo. Ele serve apenas como a plataforma para testar e visualizar o seu algoritmo.

### 👨‍💻 `candidato.py` (Sua Área de Trabalho)

**Este é o único arquivo que você deve editar.** Ele contém uma única função principal: `encontrar_caminho()`.

É dentro desta função que toda a sua lógica deve ser implementada. O arquivo já vem com uma documentação detalhada (`docstring`) explicando cada parâmetro da função e os requisitos do desafio em 3 níveis de complexidade.

## Como Começar

1.  **Instale as dependências:** Certifique-se de que você tem Python e a biblioteca Pygame instalados.
    ```bash
    pip install pygame
    ```
2.  **Execute o simulador:** Abra um terminal na pasta do projeto e execute o comando:
    ```bash
    python simulador.py
    ```
3.  **Observe o comportamento inicial:** Ao rodar pela primeira vez, você verá um robô azul que apenas se move para frente, ignorando todo o resto. Este é o comportamento do código de exemplo.

## Seu Objetivo

Sua meta é substituir o código de exemplo em `candidato.py` por uma implementação completa do algoritmo A* que atenda aos seguintes critérios, que representam os níveis de avaliação do desafio:

-   **Nível 1: Custo de Rotação:** O algoritmo deve penalizar movimentos que exijam que o robô mude de direção. Caminhos mais "suaves" devem ser preferidos.

-   **Nível 2: Custo por Estado:** O robô deve ser mais "cuidadoso" ao se mover com a bola. As penalidades, especialmente as de rotação, devem ser maiores quando ele está com a posse de bola (`tem_bola=True`).

-   **Nível 3: Zonas de Perigo:** O algoritmo deve tratar as células próximas aos adversários como "caras", preferindo contorná-las a passar por perto, a menos que seja a única opção viável.

Leia atentamente a documentação dentro da função `encontrar_caminho` para mais detalhes sobre cada nível.

---

Boa sorte! Estamos ansiosos para ver sua solução.

**Equipe EDROM**
