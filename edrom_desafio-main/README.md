# Desafio Individual EDROM - Robô A*
Eita codigo dificil ksksk tentei fazer de mais algums jeitos mas não melhorei muito, mesmo assistindo algums videos desse algoritimo A* e videos de programação em pygame não consegui melhorar o codigo o melhorsin foi esse primeiro codigo mesmo o robo ficando preso de vez enquando ksksk
As outras tentativas que fiz foi essa abaixo com direções mas o robo nem moveu de lugar por algum motivo skks
 melhor_caminho= []
    x_atual, y_atual = pos_inicial 
    x_obg, y_obg = pos_objetivo
    while (x_atual!= x_obg):
        direcao="direita"
        if direcao == "direita":
            x_atual+= 1
            if (x_atual,y_atual)in obstaculos:
                direcao= "esquerda"
                x_atual-=1
            else:
                melhor_caminho.append ((x_atual,y_atual))
        if direcao == "esquerda":
            x_atual-=1
            if (x_atual,y_atual)in obstaculos:
                direcao= "cima"
                x_atual+=1
            else:
                melhor_caminho.append((x_atual,y_atual))
        break
    while (y_atual!=y_obg):
        direcao="cima"
        if direcao == "cima":
            y_atual+=1
            if (x_atual,y_atual)in obstaculos:
                direcao= "baixo"
                y_atual-=1
            else:
                melhor_caminho.append((x_atual,y_atual))
        if direcao == "baixo":
            y_atual-=1
            if (x_atual,y_atual)in obstaculos:
                direcao= "direita"
                y_atual+=1
            else:
                melhor_caminho.append((x_atual,y_atual))
        break
resumindo me diverti tentando fazer esse codigo mas não consegui fazer certin, mas curti ter aprendido esse treko de pygame vou tentar fazer uma coisa ou outra nele kskskks
