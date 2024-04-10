#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3:

from pygame import mixer

mixer.init()
mixer.music.load('exe021.mp3')
mixer.music.play()
input('Agora você escuta?')

'''No lugar de input('Agora você escuta ?') deveria ser >>> pygame.event.wait()
mas por algum motivo não funciona mesmo o programa estando correto. '''

















