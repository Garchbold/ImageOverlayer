from __future__ import division
import pygame
import os
import sys
from PIL import Image

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class GameObject(pygame.sprite.Sprite):
	def __init__(self, image, pos):
		pygame.sprite.Sprite.__init__(self) # sprite initializer
		self.image = image
		self.area = pygame.display.get_surface().get_rect()
		self.rect = self.image.get_rect()
		self.rect.center = pos # center(x, y)
		self.x = 0
		self.y = 0

pygame.init() 

def resize(folder, fileName):
    filePath = os.path.join(folder, fileName)
    all_sprites_list = pygame.sprite.Group()
    screen_width = 1000
    screen_height = 610
    size = (screen_width, screen_height)
    screen = pygame.display.set_mode(size)

    background_image = pygame.image.load("flux.jpg").convert()
    
    logo_image = pygame.image.load(fileName).convert_alpha()
    size = logo_image.get_rect()
    width = size.width
    height = size.height

    # LOGO 1 CENTER = (460, 320)
    # LOGO 2 CENTER = (890, 350)

    # conditionals for different logo sizes

    ratio = (height/width)

    if ratio < 0.25:
        flux_scale = (290/width)
    elif ratio < 0.5:
        flux_scale = (270/width)
    elif ratio < 1.1:
        flux_scale = (135/width)
    elif ratio < 1.5:
        flux_scale = (100/width)
    elif ratio < 2:
        flux_scale = (60/width)

    logo_image = pygame.transform.scale(logo_image, (int(width*flux_scale), int(height*flux_scale)))
    logo = GameObject(logo_image, (460, 320))
    all_sprites_list.add(logo)

    logo_image_2 = pygame.image.load(fileName).convert_alpha()
    logo_image_2 = pygame.transform.scale(logo_image_2, (int(width*flux_scale), int(height*flux_scale)))
    logo_image_2 = pygame.transform.rotate(logo_image_2, 90)
    logo_2 = GameObject(logo_image_2, (890, 350))
    all_sprites_list.add(logo_2)
    
    clock = pygame.time.Clock()
    done = False

    while not done:

        # ----- Main Event Loop ----- #

        screen.blit(background_image, [0, 0])	# background image in event loop
        all_sprites_list.update()	# this calls update on all the sprites
        all_sprites_list.draw(screen)	# draw sprites
        pygame.display.flip()
        clock.tick(60)
        pygame.image.save(screen, "final/"+fileName)
	done = True 

    pygame.quit()

def bulkResize(imageFolder):
    imgExts = ["png", "bmp", "jpg"]

    for path, dirs, files in os.walk(imageFolder):
        for fileName in files:
            ext = fileName[-3:].lower()
            if ext not in imgExts:
                continue

            resize(path, fileName)

if __name__ == "__main__":
    imageFolder=sys.argv[1]	# first arg is path to image folder
    bulkResize(imageFolder)


