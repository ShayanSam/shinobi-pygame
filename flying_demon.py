from sys import pycache_prefix
import pygame
from settings import *

class FlyingDeamon(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.x_p = 2000
        self.y_p = 600
        self.width = 220
        self.height = 210
        self.health = 80
        self.count = 10
        self.is_it_stop = False
        self.projectile_x = 900
        self.projectile_y = 640
        self.flying_frames = [pygame.transform.scale(pygame.image.load(f"./assets/flying_demon/demon_flying_{i}.png"),(self.height,self.width)) for i in range(4)]
        self.attack_frames = [pygame.transform.scale(pygame.image.load(f"./assets/flying_demon/demon_attack_{i}.png"),(self.height,self.width)) for i in range(8)]
        self.bk_flying_frames = [pygame.transform.scale(pygame.transform.flip(pygame.image.load(f"./assets/flying_demon/demon_flying_{i}.png"), True, False),(self.height,self.width)) for i in range(4)]
        self.hurt_frame = pygame.transform.scale(pygame.image.load(f"./assets/flying_demon/hurt_1.png"),(self.height,self.width))
        self.bk_hurt_frame = pygame.transform.scale(pygame.transform.flip(pygame.image.load(f"./assets/flying_demon/hurt_1.png"),True, False),(self.height,self.width)) 
        self.projectile = pygame.transform.scale(pygame.image.load(f"./assets/flying_demon/projectile.png"),(48, 32))
        self.projectile_rect = self.projectile.get_rect()
        self.projectile_rect.center = (self.projectile_x, self.projectile_y)
        self.bk_projectile = pygame.transform.scale(pygame.transform.flip(pygame.image.load(f"./assets/flying_demon/projectile.png"), True, False),(48, 32))
        self.bk_projectile_rect = self.projectile.get_rect()
        self.bk_projectile_rect.center = (self.projectile_x, self.projectile_y)
        self.bk_mask_projectile = pygame.mask.from_surface(self.bk_projectile)
        self.current_sprite = 0
        self.image = self.flying_frames[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_p,self.y_p)
        
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_projectile = pygame.mask.from_surface(self.projectile)

    def update(self, hero, keys, screen, group):
        if self.count > 0: 
            self.current_sprite += 0.3
            self.rect.center = (self.x_p ,self.y_p)
            self.fly_forward()
            self.look_forward(hero)
            self.attack(screen, hero)
            self.hurt(hero.facing_forward, hero.sword_rect, keys ) 
            self.death()
            group.draw(screen)
        
            



    def fly_forward(self):
        if self.x_p > (screen_width / 2):
            self.x_p -= 12
            if self.current_sprite >= len(self.flying_frames):
                self.current_sprite = 0
            self.image = self.flying_frames[int(self.current_sprite)]
        else:
            self.is_it_stop = True
    
    
    def look_forward(self, hero):
        if self.current_sprite >= len(self.flying_frames):
            self.current_sprite = 0
        if hero.x_p < self.x_p and self.is_it_stop:
            self.image = self.flying_frames[int(self.current_sprite)]
        elif hero.x_p > self.x_p and self.is_it_stop:
            self.image = self.bk_flying_frames[int(self.current_sprite)]

    def attack(self, screen, hero):
        if not self.is_it_stop:
            self.bk_projectile_rect.x = int(screen_width / 2)
            self.projectile_rect.x = int((screen_width / 2) - 30)

        elif hero.x_p < self.x_p and self.is_it_stop:
            screen.blit(self.projectile, self.projectile_rect)
            self.projectile_rect.x -= 4
            if hero.mask.overlap(self.mask_projectile, (self.projectile_rect.x - hero.rect.x, self.projectile_rect.y - hero.rect.y)): 
                hero.hit = True
                self.projectile_rect.x = int((screen_width / 2) - 30)
         
            elif self. projectile_rect.x < 0:
                self.projectile_rect.x = int((screen_width / 2) - 30)
        elif hero.x_p > self.x_p and self.is_it_stop:
            screen.blit(self.bk_projectile, self.bk_projectile_rect)
            self.bk_projectile_rect.x += 4
            if hero.mask.overlap(self.bk_mask_projectile, (self.bk_projectile_rect.x - hero.rect.x, self.bk_projectile_rect.y - hero.rect.y)):
                hero.hit = True
                self.bk_projectile_rect.x = int(screen_width / 2)

            elif self.bk_projectile_rect.x > screen_width:
                self.bk_projectile_rect.x = int(screen_width / 2)


    def hurt(self, facing_forward, sword_rect, keys):
        
        arrow_keys_pressed = keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_n]

        if self.rect.colliderect(sword_rect) and keys[pygame.K_SPACE] and not arrow_keys_pressed:
            if facing_forward:
                self.image = self.hurt_frame
            else:
                self.image = self.bk_hurt_frame

            self.health -= 20



    def death(self):
        if self.health < 0 : 
            self.is_it_stop = False
            self.count -= 1
            self.x_p = 2300
            self.health = 80
