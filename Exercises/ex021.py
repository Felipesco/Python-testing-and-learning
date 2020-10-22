# Tocar música MP3 <3 (ex021-imagine-lyrics)
# No CMD da certo (...\diretorio>ex021.py) 
import pygame

pygame.mixer.init()
pygame.mixer.music.load('ex021-imagine-lyrics.mp3')
pygame.mixer.music.play()

while(pygame.mixer.music.get_busy()):
    pass