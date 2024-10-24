import math
import sys

import pygame

import flying_demon
from flying_demon import FlyingDeamon
from hero import Hero
from settings import *
from tree import Tree

# pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(game_title)

bg = pygame.image.load(
    "./assets/bg/bg.png"
).convert_alpha()  # Use convert_alpha() if images have transparency

bg_width = bg.get_width()

tiles = math.ceil(screen_width / bg_width)


hero_sprite_group = pygame.sprite.Group()
enemy_sprite_group = pygame.sprite.Group()

hero = Hero()
hero_sprite_group.add(hero)


flying_demon = FlyingDeamon()
enemy_sprite_group.add(flying_demon)

tree = Tree()

clock = pygame.time.Clock()

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                hero.is_attacking = True

    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width, 0))
    screen.blit(tree.tree_1(), (900, 260))

    hero.hero_update(screen)
    flying_demon.update(hero, keys, screen, enemy_sprite_group)

    if keys[pygame.K_RIGHT]:
        hero.move_forward()
    elif keys[pygame.K_LEFT]:
        hero.move_backward()
    elif keys[pygame.K_n]:
        hero.jumping = True

    hero.jump()
    hero_sprite_group.draw(screen)
    pygame.display.flip()

    clock.tick(30)
