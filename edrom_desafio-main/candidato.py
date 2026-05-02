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
    REQUISITOS QUE EU CUMPRI OU NAO KSKSK (AVALIADOS EM NÍVEIS):
    ---------------------------------------------------------------------------------
    
    """

    # -------------------------------------------------------- #
    #                                                          #
    #             >>>  IMPLEMENTAÇÃO DO CANDIDATO   <<<        #
    #                                                          #
    # -------------------------------------------------------- #
    melhor_caminho_talvezksksk = []
    x_atual, y_atual = pos_inicial 
    x_obg, y_obg = pos_objetivo
    custo = 0
    penalidade = 1
    penalidade2 = 3       
    penalidadedig = 2
    ktchau= tem_bola
    if (ktchau == True):      
        penalidade = penalidade*2
        penalidade2 = penalidade2*2
        penalidadedig = penalidadedig*2
    else :
        pass
    while x_atual != x_obg or y_atual != y_obg:   
        if x_atual<x_obg and y_atual>y_obg:      
            x_atual+=1
            y_atual-=1
            custo+= penalidadedig
            if (x_atual,y_atual) in obstaculos:    
                melhor_caminho_talvezksksk.append((x_atual,y_atual+1))
                custo+=penalidade2
                y_atual=y_atual+1
            else:
                melhor_caminho_talvezksksk.append((x_atual,y_atual))    
        elif x_atual<x_obg and y_atual<y_obg:   
            x_atual+=1
            y_atual+=1
            custo+=penalidadedig
            if (x_atual,y_atual) in obstaculos:
                melhor_caminho_talvezksksk.append((x_atual,y_atual-1))
                custo+=penalidade2
                y_atual=y_atual-1
            else:
                melhor_caminho_talvezksksk.append((x_atual,y_atual))
        elif x_atual>x_obg and y_atual>y_obg:
            x_atual-=1
            y_atual-=1
            if (x_atual,y_atual) in obstaculos:
                melhor_caminho_talvezksksk.append((x_atual+1,y_atual))
                custo+=penalidade2
                x_atual=x_atual+1
            else:
                melhor_caminho_talvezksksk.append((x_atual,y_atual))
        elif x_atual>x_obg and y_atual<y_obg:
            x_atual-=1
            y_atual+=1
            if (x_atual,y_atual) in obstaculos:
                melhor_caminho_talvezksksk.append((x_atual+1,y_atual))
                custo+=penalidade2
                x_atual=x_atual+1
            else:
                melhor_caminho_talvezksksk.append((x_atual,y_atual))
        elif x_atual< x_obg:     
            x_atual= x_atual+1
            custo +=penalidade
            if (x_atual,y_atual) in obstaculos:
                melhor_caminho_talvezksksk.append((x_atual-1,y_atual+1))
                custo+=penalidade2
                y_atual=y_atual+1
            else:
                melhor_caminho_talvezksksk.append((x_atual,y_atual))
        elif x_atual> x_obg:
            x_atual= x_atual-1
            custo +=penalidade
            if (x_atual,y_atual) in obstaculos:
                melhor_caminho_talvezksksk.append((x_atual+1,y_atual+1))
                custo+=penalidade2
                y_atual=y_atual+1
            else:
                melhor_caminho_talvezksksk.append((x_atual,y_atual))
        elif y_atual< y_obg:
            y_atual= y_atual+1
            custo+=penalidade
            if (x_atual,y_atual) in obstaculos:
                melhor_caminho_talvezksksk.append((x_atual-1,y_atual))
                x_atual=x_atual-1
                custo+=penalidade2
            else:
                melhor_caminho_talvezksksk.append((x_atual,y_atual))
        else:
            y_atual= y_atual-1
            custo+=penalidade
            if (x_atual,y_atual) in obstaculos:
                melhor_caminho_talvezksksk.append((x_atual-1,y_atual))
                custo+=penalidade2
                x_atual=x_atual-1
            else:
                melhor_caminho_talvezksksk.append((x_atual,y_atual))
        break
    print(f"Custo da andada foi: {custo}")   
    return melhor_caminho_talvezksksk  
