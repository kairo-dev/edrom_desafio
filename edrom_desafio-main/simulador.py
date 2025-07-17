# SIMULADOR DESAFIO INDIVIDUAL EDROM - 2025

import pygame
import sys
import candidato
import random

# Configurações
COR_FUNDO = (20, 80, 40)
COR_LINHA = (255, 255, 255)
COR_ROBO = (0, 0, 255)
COR_ROBO_COM_BOLA = (100, 140, 255)
COR_BOLA = (255, 165, 0)
COR_OBSTACULO = (255, 0, 0)
COR_CAMINHO = (0, 255, 255)
COR_GOL = (255, 255, 0)
COR_PAINEL = (40, 40, 40)
COR_BOTAO = (80, 80, 80)
COR_TEXTO_BOTAO = (255, 255, 255)

# Dimensões da Grade e da Tela
LARGURA_GRID = 20
ALTURA_GRID = 15
TAMANHO_CELULA = 45
ALTURA_PAINEL = 75

LARGURA_TELA = LARGURA_GRID * TAMANHO_CELULA
ALTURA_TELA = ALTURA_GRID * TAMANHO_CELULA + ALTURA_PAINEL

# Desenho
def desenhar_grade(tela):
    for x in range(0, LARGURA_TELA, TAMANHO_CELULA):
        pygame.draw.line(tela, COR_LINHA, (x, 0), (x, ALTURA_GRID * TAMANHO_CELULA))
    for y in range(0, ALTURA_GRID * TAMANHO_CELULA + 1, TAMANHO_CELULA):
        pygame.draw.line(tela, COR_LINHA, (0, y), (LARGURA_TELA, y))

def desenhar_retangulo(tela, pos_grid, cor):
    x, y = pos_grid
    rect = pygame.Rect(x * TAMANHO_CELULA, y * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA)
    pygame.draw.rect(tela, cor, rect)
    
def desenhar_circulo(tela, pos_grid, cor, raio_fator=0.4):
    x, y = pos_grid
    centro_x = int(x * TAMANHO_CELULA + TAMANHO_CELULA / 2)
    centro_y = int(y * TAMANHO_CELULA + TAMANHO_CELULA / 2)
    raio = int(TAMANHO_CELULA * raio_fator)
    pygame.draw.circle(tela, cor, (centro_x, centro_y), raio)

def desenhar_caminho(tela, caminho):
    for passo in caminho:
        desenhar_circulo(tela, passo, COR_CAMINHO, raio_fator=0.2)
        
def desenhar_botao(tela, fonte, rect, texto, cor_fundo, cor_texto):
    pygame.draw.rect(tela, cor_fundo, rect, border_radius=8)
    superficie_texto = fonte.render(texto, True, cor_texto)
    rect_texto = superficie_texto.get_rect(center=rect.center)
    tela.blit(superficie_texto, rect_texto)

# Lógica
def resetar_cenario():
    # Posições fixas
    pos_robo = (2, ALTURA_GRID // 2)
    pos_gol = (LARGURA_GRID - 1, ALTURA_GRID // 2)

    # Posição da Bola
    while True:
        pos_bola_x = random.randint(LARGURA_GRID // 2, LARGURA_GRID - 1)
        pos_bola_y = random.randint(0, ALTURA_GRID - 1)
        pos_bola = (pos_bola_x, pos_bola_y)
        if pos_bola != pos_gol and pos_bola != pos_robo:
            break

    # Posição dos Adversários (Obstaculos)
    MAX_OBSTACULOS = 20
    obstaculos = []
    posicoes_ocupadas = {pos_robo, pos_gol, pos_bola}
    
    tentativas = 0
    while len(obstaculos) < MAX_OBSTACULOS:
        obs_x = random.randint(3, LARGURA_GRID - 1)
        obs_y = random.randint(0, ALTURA_GRID - 1)
        pos_obs = (obs_x, obs_y)

        dist_do_robo = abs(pos_obs[0] - pos_robo[0]) + abs(pos_obs[1] - pos_robo[1])
        dist_do_gol = abs(pos_obs[0] - pos_gol[0]) + abs(pos_obs[1] - pos_gol[1])

        if pos_obs in posicoes_ocupadas or dist_do_robo < 3 or dist_do_gol <= 1:
            tentativas += 1
            if tentativas > 1000:
                print(f"AVISO: Não foi possível posicionar {MAX_OBSTACULOS} obstáculos. Continuando com {len(obstaculos)}.")
                break
            continue
        
        obstaculos.append(pos_obs)
        posicoes_ocupadas.add(pos_obs)
        tentativas = 0

    return {
        "pos_robo": pos_robo, "pos_bola": pos_bola, "pos_gol": pos_gol, "obstaculos": obstaculos,
        "tem_bola": False, "caminho_atual": [], "simulacao_rodando": False,
        "mensagem": "Cenário aleatório gerado!"
    }

# Loop do Simulador
def main():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("EDROM - Desafio A*")
    clock = pygame.time.Clock()
    fonte_botao = pygame.font.Font(None, 28)
    
    try:
        icone_imagem = pygame.image.load("icone_edrom.png")
        pygame.display.set_icon(icone_imagem)
        icone_painel = pygame.transform.scale(icone_imagem, (40, 40))
    except pygame.error as e:
        print(f"Não foi possível carregar a imagem 'icone_edrom.png': {e}")
        icone_painel = pygame.Surface((40, 40), pygame.SRCALPHA)
    
    botao_play_pause = pygame.Rect(20, ALTURA_TELA - ALTURA_PAINEL + 10, 120, 40)
    botao_reset = pygame.Rect(160, ALTURA_TELA - ALTURA_PAINEL + 10, 120, 40)
    
    estado_jogo = resetar_cenario()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_play_pause.collidepoint(event.pos):
                    estado_jogo["simulacao_rodando"] = not estado_jogo["simulacao_rodando"]
                    estado_jogo["mensagem"] = "Simulação em andamento..." if estado_jogo["simulacao_rodando"] else "Simulação pausada."
                if botao_reset.collidepoint(event.pos):
                    estado_jogo = resetar_cenario()

        if estado_jogo["simulacao_rodando"]:
            if not estado_jogo["caminho_atual"]:
                objetivo_atual = estado_jogo["pos_bola"] if not estado_jogo["tem_bola"] else estado_jogo["pos_gol"]
                estado_jogo["caminho_atual"] = candidato.encontrar_caminho(
                    pos_inicial=estado_jogo["pos_robo"], pos_objetivo=objetivo_atual, obstaculos=estado_jogo["obstaculos"],
                    largura_grid=LARGURA_GRID, altura_grid=ALTURA_GRID, tem_bola=estado_jogo["tem_bola"])
            if estado_jogo["caminho_atual"]:
                estado_jogo["pos_robo"] = estado_jogo["caminho_atual"].pop(0)
            if not estado_jogo["tem_bola"] and estado_jogo["pos_robo"] == estado_jogo["pos_bola"]:
                estado_jogo["tem_bola"] = True
                estado_jogo["caminho_atual"] = []
                estado_jogo["mensagem"] = "Bola capturada! Rumo ao gol!"
            if estado_jogo["tem_bola"] and estado_jogo["pos_robo"] == estado_jogo["pos_gol"]:
                estado_jogo["mensagem"] = "GOL! Cenário resetado."
                pygame.display.flip()
                pygame.time.wait(2000)
                estado_jogo = resetar_cenario()

        tela.fill(COR_FUNDO)
        desenhar_grade(tela)
        
        if estado_jogo["caminho_atual"]:
            desenhar_caminho(tela, estado_jogo["caminho_atual"])

        desenhar_retangulo(tela, estado_jogo["pos_gol"], COR_GOL)
        for obs in estado_jogo["obstaculos"]:
            desenhar_retangulo(tela, obs, COR_OBSTACULO)

        if estado_jogo["tem_bola"]:
            desenhar_retangulo(tela, estado_jogo["pos_robo"], COR_ROBO_COM_BOLA)
            desenhar_circulo(tela, estado_jogo["pos_robo"], COR_BOLA, raio_fator=0.3)
        else:
            desenhar_retangulo(tela, estado_jogo["pos_robo"], COR_ROBO)
            desenhar_circulo(tela, estado_jogo["pos_bola"], COR_BOLA)
            
        painel_rect = pygame.Rect(0, ALTURA_GRID * TAMANHO_CELULA, LARGURA_TELA, ALTURA_PAINEL)
        pygame.draw.rect(tela, COR_PAINEL, painel_rect)
        
        texto_play = "Pause" if estado_jogo["simulacao_rodando"] else "Play"
        desenhar_botao(tela, fonte_botao, botao_play_pause, texto_play, COR_BOTAO, COR_TEXTO_BOTAO)
        desenhar_botao(tela, fonte_botao, botao_reset, "Reset", COR_BOTAO, COR_TEXTO_BOTAO)
        
        superficie_msg = fonte_botao.render(estado_jogo["mensagem"], True, COR_TEXTO_BOTAO)
        tela.blit(superficie_msg, (botao_reset.right + 20, botao_reset.centery - superficie_msg.get_height() // 2))

        pos_icone_x = LARGURA_TELA - icone_painel.get_width() - 20
        pos_icone_y = ALTURA_TELA - ALTURA_PAINEL / 2 - icone_painel.get_height() / 2
        tela.blit(icone_painel, (pos_icone_x, pos_icone_y))

        pygame.display.flip()
        clock.tick(5)

if __name__ == '__main__':
    main()