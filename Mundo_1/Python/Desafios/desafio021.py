# ==============================================================
# DESAFIO 021: PLAYER DE MÚSICA INTERATIVO (VERSÃO PYGAME)
# ==============================================================
import pygame # Agora sim, com Python 3.12 funcionando!
import os
import time

# 1. INICIALIZAÇÃO DO MOTOR DE ÁUDIO
pygame.mixer.init()
pygame.init()

# 2. CONFIGURAÇÃO DO CAMINHO
# Usando o caminho absoluto que você confirmou
caminho = r'C:\Users\Rafael\Documents\Rafael\Cursos\Curso em video\Python\src\primavera.mp3'

print(f"{' MP3 PLAYER PRO ':=^50}")

# 3. CARREGAMENTO COM VERIFICAÇÃO
if os.path.exists(caminho):
    pygame.mixer.music.load(caminho)
    print(f"✅ Arquivo: primavera.mp3 carregado!")
else:
    print(f"❌ ERRO: Arquivo não encontrado no caminho:\n{caminho}")
    exit() # Encerra se não achar o arquivo

# 4. MENU INTERATIVO
opcao = ''
while opcao != '4':
    print("""
    [ 1 ] PLAY / RESUMIR ⏯️
    [ 2 ] PAUSAR ⏸️
    [ 3 ] REINICIAR 🔄
    [ 4 ] SAIR ⏹️
    """)
    opcao = str(input('Escolha uma opção: ')).strip()

    if opcao == '1':
        # Se a música estiver pausada, unpause. Se estiver parada, play.
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.unpause()
            print("=> Áudio retomado!")
        else:
            pygame.mixer.music.play()
            print("=> Tocando: Primavera 🎶")

    elif opcao == '2':
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            print("=> Áudio pausado.")

    elif opcao == '3':
        pygame.mixer.music.play()
        print("=> Reiniciando música...")

    elif opcao == '4':
        pygame.mixer.music.stop()
        print("=> Fechando o player. Até mais!")

# -----------------------------------------------------------
# POR QUE O PYGAME É MELHOR? (Nota de Estudo)
# -----------------------------------------------------------
# - Multitarefa: O Python continua lendo o seu 'input' enquanto
#   a música toca ao fundo.
# - Mixer: Permite carregar vários sons e controlar o volume.
# - Estabilidade: No Python 3.12, essa é a ferramenta padrão
#   para áudio em jogos e apps.
# ==============================================================