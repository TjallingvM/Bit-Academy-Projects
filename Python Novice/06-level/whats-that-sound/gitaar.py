'''
Auteur: Tjalling van Mourik
Datum: 04-04-2022

gitaar.py:
De voorbeelduitwerking van Python Novice -> 6. Python Extended -> 4. What's That Sound

Het doel van deze exercise is heel simpel: je krijgt het bestand gitaar.wav aangeleverd.
Speel dit bestand nu af op jouw computer met je eigen Python code.
Je mag zelf kiezen welke packages je hiervoor installeert en hoe je het voor elkaar krijgt,
zolang het geluid maar onaangetast en onbewerkt wordt afgespeeld.
'''

import pygame

pygame.mixer.init()
my_sound = pygame.mixer.Sound('gitaar.wav')
print("> Playing sound...")
my_sound.play()
print("> Sound played!")
