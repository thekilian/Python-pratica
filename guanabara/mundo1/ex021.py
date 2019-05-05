# 021 - Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
pygame.init()
pygame.mixer.music.load('music.wav')
pygame.mixer.music.play()
pygame.event.wait()

# o arquivo deve estar na mesma pasta do script.
