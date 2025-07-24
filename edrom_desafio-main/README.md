# Desafio Individual EDROM - Robô A*
# ATT feita domingo
### Eita codigo dificil ksksk tentei fazer de mais algums jeitos mas não melhorei muito, mesmo assistindo algums videos desse algoritimo A* e videos de programação em pygame não consegui melhorar o codigo o melhorsin foi esse primeiro codigo mesmo o robo ficando preso de vez enquando ksksk
### As outras tentativas que fiz foi essa abaixo com direções mas o robo nem moveu de lugar por algum motivo skks (obs agora na att de segunda que vi o motivo nao funcionou pq eu nao pus o return com o caminho kskskskks mas vou deixar do meu geito mesmo porque esse de direção nao puz muita fé)
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
### resumindo me diverti tentando fazer esse codigo mas não consegui fazer certin, mas curti ter aprendido esse treko de pygame vou tentar fazer uma coisa ou outra nele kskskks
## erros por enquanto o codigo testando umas 5 vezes ele falha uma ficando preso, nao anda na diagonal e nao usei o f=g+h pra fazer ele escolher o melhor caminho e esse if da bola ta horroroso kskksks
# ATT segunda
### melhorei bastante o codigo deixando ele menor adicionei andar na diagonal e diminui bastante os erros dele ficando preso, antes em 5 testes ele falhava um agora tem que testar umas 15 vez pra falhar uma e melhorei o if da bola aumentando a penalidade

# att de quarta
### a mais o prazo nao e so terça? isso é um mero detalhe ksksks (inclusive deveriam pensar e que e uma baita qualidade mesmo depois da entrega do trabalho o caba ta se esforçando pra deixar o trabalho melhor) continuando o problema do robo ficando preso resolvido hehehe agora ele nao fica mais preso os erros agora sao apenas o de nao ter usado f g e h e quando o robo muda de caminho por causa de um obstaculo ele as vezaas ele entra num obstaculo

