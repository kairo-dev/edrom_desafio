# NOME DO CANDIDATO: [Kairo de Melo Sousa]
# CURSO DO CANDIDATO: [Engenharia de Controle e Automação]
# AREAS DE INTERESSE: [Estrutura,Movimento,Behavior]

# Você pode importar as bibliotecas que julgar necessárias.

def encontrar_caminho(pos_inicial, pos_objetivo, obstaculos, largura_grid, altura_grid, tem_bola=False):
    """
    Esta é a função principal que você deve implementar para o desafio EDROM.
    Seu objetivo é criar um algoritmo de pathfinding (como o A*) que encontre o
    caminho ótimo para o robô, considerando os diferentes níveis de complexidade.

    Args:
        pos_inicial (tuple): A posição (x, y) inicial do robô.
        pos_objetivo (tuple): A posição (x, y) do objetivo (bola ou gol).
        obstaculos (list): Uma lista de tuplas (x, y) com as posições dos obstáculos.
        largura_grid (int): A largura do campo em células.
        altura_grid (int): A altura do campo em células.
        tem_bola (bool): Um booleano que indica o estado do robô.
                         True se o robô está com a bola, False caso contrário.
                         Este parâmetro é essencial para o Nível 2 do desafio.

    Returns:
        list: Uma lista de tuplas (x, y) representando o caminho do início ao fim.
              A lista deve começar com o próximo passo após a pos_inicial e terminar
              na pos_objetivo. Se nenhum caminho for encontrado, retorna uma lista vazia.
              Exemplo de retorno: [(1, 2), (1, 3), (2, 3)]

    ---------------------------------------------------------------------------------
    REQUISITOS DO DESAFIO (AVALIADOS EM NÍVEIS):
    ---------------------------------------------------------------------------------
    [NÍVEL BÁSICO: A* Comum com Diagonal]
    O Algoritmo deve chegar até a bola e depois ir até o gol (desviando dos adversários) 
    considerando custos diferentes pdra andar reto (vertical e horizontal) e para andar em diagonal

    [NÍVEL 1: Custo de Rotação]
    O custo de um passo não é apenas a distância. Movimentos que exigem que o robô
    mude de direção devem ser penalizados. Considere diferentes penalidades para:
    - Curvas suaves (ex: reto -> diagonal).
    - Curvas fechadas (ex: horizontal -> vertical).
    - Inversões de marcha (180 graus).

    [NÍVEL 2: Custo por Estado]
    O comportamento do robô deve mudar se ele estiver com a bola. Quando `tem_bola`
    for `True`, as penalidades (especialmente as de rotação do Nível 1) devem ser
    AINDA MAIORES. O robô precisa ser mais "cuidadoso" ao se mover com a bola.

    [NÍVEL 3: Zonas de Perigo]
    As células próximas aos `obstaculos` são consideradas perigosas. Elas não são
    proibidas, mas devem ter um custo adicional para desencorajar o robô de passar
    por elas, a menos que seja estritamente necessário ou muito vantajoso.

    DICA: Um bom algoritmo A* é flexível o suficiente para que os custos de movimento
    (g(n)) possam ser calculados dinamicamente, incorporando todas essas regras.
    """

    # -------------------------------------------------------- #
    #                                                          #
    #             >>>  IMPLEMENTAÇÃO DO CANDIDATO   <<<        #
    #                                                          #
    # -------------------------------------------------------- #

    # O código abaixo é um EXEMPLO SIMPLES de um robô que apenas anda para frente.
    # Ele NÃO desvia de obstáculos e NÃO busca o objetivo.
    # Sua tarefa é substituir esta lógica simples pelo seu algoritmo A* completo.
    caminho_exemplo = []
    x_atual, y_atual = pos_inicial 
    x_obg, y_obg = pos_objetivo
    custo = 0
    penalidade = 1
    penalidade2 = 2
    ktchau= tem_bola
    if ktchau== True:    #com bola a penalidade aumenta
        penalidade= penalidade*2
        penalidade2= penalidade2*2
        while x_atual != x_obg or y_atual != y_obg:  #enquanto a posiçao nao for igual a do objetivo ele vai andando
            if x_atual< x_obg:
                x_atual= x_atual+1
                custo +=penalidade
                if (x_atual,y_atual) in obstaculos:  #topo com um objeto ele muda de direção e aumenta ai o custo
                    caminho_exemplo.append((x_atual-1,y_atual+1))
                    custo+=penalidade2
                    y_atual=y_atual+1
                else:
                    caminho_exemplo.append((x_atual,y_atual))
            elif x_atual> x_obg:
                x_atual= x_atual-1
                custo +=penalidade
                if (x_atual,y_atual) in obstaculos:
                    caminho_exemplo.append((x_atual+1,y_atual+1))
                    custo+=penalidade2
                    y_atual=y_atual+1
                else:
                    caminho_exemplo.append((x_atual,y_atual))
            elif y_atual< y_obg:
                y_atual= y_atual+1
                custo+=penalidade
                if (x_atual,y_atual) in obstaculos:
                    caminho_exemplo.append((x_atual-1,y_atual-1))
                    x_atual=x_atual-1
                    custo+=penalidade2
                else:
                    caminho_exemplo.append((x_atual,y_atual))
            else:
                y_atual= y_atual-1
                custo+=penalidade
                if (x_atual,y_atual) in obstaculos:
                    caminho_exemplo.append((x_atual-1,y_atual+1))
                    custo+=penalidade2
                    x_atual=x_atual-1
                else:
                    caminho_exemplo.append((x_atual,y_atual))
            break
        print(f"Custo da andada foi: {custo}")   #printa o custo da andada porque por algum motivo nao ta somando o custo ksksksk
        return caminho_exemplo
    else :        #tudo denovo com a penalidade menor pq ta sem bola
        while x_atual != x_obg or y_atual != y_obg:
            if x_atual< x_obg:
                x_atual= x_atual+1
                custo +=penalidade
                if (x_atual,y_atual) in obstaculos:
                    caminho_exemplo.append((x_atual-1,y_atual-1))
                    custo+=penalidade2
                    y_atual=y_atual-1
                else:
                    caminho_exemplo.append((x_atual,y_atual))
            elif x_atual> x_obg:
                x_atual= x_atual-1
                custo +=penalidade
                if (x_atual,y_atual) in obstaculos:
                    caminho_exemplo.append((x_atual+1,y_atual-1))
                    custo+=penalidade2
                    y_atual=y_atual-1
                else:
                    caminho_exemplo.append((x_atual,y_atual))
            elif y_atual< y_obg:
                y_atual= y_atual+1
                custo+=penalidade
                if (x_atual,y_atual) in obstaculos:
                    caminho_exemplo.append((x_atual-1,y_atual-1))
                    x_atual=x_atual-1
                    custo+=penalidade2
                else:
                    caminho_exemplo.append((x_atual,y_atual))
            else:
                y_atual= y_atual-1
                custo+=penalidade
                if (x_atual,y_atual) in obstaculos:
                    caminho_exemplo.append((x_atual-1,y_atual+1))
                    custo+=penalidade2
                    x_atual=x_atual-1
                else:
                    caminho_exemplo.append((x_atual,y_atual))
            break
        print(f"Custo da andada foi: {custo}")
        return caminho_exemplo
#eu nao sei fazer direito esse negocio de mudar de direçao por isso o geito que fiz ficou bem diferenciado 
#e por isso tambem se voce ir testando tem vez que o robo fica preso mas isso é so um detalhe ksksk
#quando ele nao fica preso ele ta fazendo o caminho bunitin ta contando o custo e ta aumento o custo com bola então...
#... teoricamente cheguei no nivel 2 se voce disfarçar o pequeno detalhe que no basico eu errei por nao saber esse...
#... treko de f(x)baseado no custo e coisa e tal kskskks
