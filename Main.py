import pygame
import traceback
from pygame.locals import *

pygame.init()

try:
	#Ouverture de la fenêtre Pygame
	fenetre = pygame.display.set_mode((1400, 800))

	#Chargement et collage du fond
	fond = pygame.image.load("images/platresDouble.jpg").convert()
	fenetre.blit(fond, (0, 0))

	#Chargement et collage du personnage
	perso = pygame.image.load("images/tribalSunshine.png").convert_alpha()
	position_perso = perso.get_rect()
	fenetre.blit(perso, (200, 300))

	#Rafraîchissement de l'écran
	pygame.display.set_caption("Crypto Racoon")
	pygame.display.flip()

	# BOUCLE INFINIE
	continuer = 1
	while continuer:
		for event in pygame.event.get():  	# Attente des événements
			if event.type == QUIT:
				continuer = 0

			# Détails des events : https://openclassrooms.com/fr/courses/1399541-interface-graphique-pygame-pour-python/1399995-gestion-des-evenements-1
			if event.type == KEYDOWN:			# Evènements claviers
				if event.key == K_DOWN:
					position_perso = position_perso.move(0, 25)
				if event.key == K_UP:
					position_perso = position_perso.move(0, -25)
				if event.key == K_LEFT:
					position_perso = position_perso.move(-25, 0)
				if event.key == K_RIGHT:
					position_perso = position_perso.move(25, 0)

			# 1 - Clic gauche
			# 2 - Milieu ou gauche+droite
			# 3 - Clic droit
			# 4 - Molette haute
			# 5 - Molette basse
			if event.type == MOUSEBUTTONDOWN:	# Evènements clic souris
				if event.button == 1:
					perso_x = event.pos[0]
					perso_y = event.pos[1]

			if event.type == MOUSEMOTION:  		# Evènements mouvements souris
				perso_x = event.pos[0]
				perso_y = event.pos[1]

		# Re-collage
		fenetre.blit(fond, (0, 0))
		fenetre.blit(perso, position_perso)
		# Rafraichissement
		pygame.display.flip()
except:
	traceback.print_exc()
finally:
	pygame.quit()
	exit()
