import pygame


# 1. Caminho do arquivo
caminho = r'C:\Users\Rafael\Documents\Rafael\Cursos\Curso em video\Python\src\primavera.mp3'

# 2. Inicialização
pygame.init()
pygame.mixer.init() # Inicializa o mixer especificamente

try:
    # 3. Carregar e dar o Play
    pygame.mixer.music.load(caminho)
    pygame.mixer.music.play()

    # 4. Manter o programa vivo enquanto a música toca
    print("Tocando música... Pressione Ctrl+C para parar.")
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10) # Reduz o uso de CPU no loop

except pygame.error as e:
    print(f"Erro ao carregar o arquivo: {e}")

finally:
    pygame.quit()