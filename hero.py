import pygame


class Hero(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.jumping = False
        self.x_p = 80
        self.y_p = 630
        self.width = 700
        self.height = 700
        self.velocity = 20
        self.is_attacking = False
        self.hit = False
        self.idle_frames = [pygame.transform.scale(pygame.image.load(f"./assets/hero/hero_idle_{i}.png"),(self.width,self.height)) for i in range(4)]
        self.bk_idle_frames = [pygame.transform.scale(pygame.transform.flip(pygame.image.load(f"./assets/hero/hero_idle_{i}.png"),True, False),(self.width,self.height)) for i in range(4)]
        self.run_frames = [pygame.transform.scale(pygame.image.load(f"./assets/hero/hero_run_{i}.png"),(self.width,self.height)) for i in range(8)]
        self.bk_run_frames = [pygame.transform.scale(pygame.transform.flip(pygame.image.load(f"./assets/hero/hero_run_{i}.png"), True , False),(self.width,self.height)) for i in range(8)]
        self.attack_frame = pygame.transform.scale(pygame.image.load(f"./assets/hero/attack_2.png"),(self.width,self.height)) 
        self.bk_attack_frame = pygame.transform.scale(pygame.transform.flip(pygame.image.load(f"./assets/hero/attack_2.png"), True, False),(self.width,self.height))

        self.take_hit_frame = pygame.transform.scale(pygame.image.load(f"./assets/hero/hit.png"),(self.width,self.height)) 
        self.bk_take_hit_frame = pygame.transform.scale(pygame.transform.flip(pygame.image.load(f"./assets/hero/hit.png"),True, False),(self.width,self.height)) 


        self.jump_frame = pygame.transform.scale(pygame.image.load(f"./assets/hero/hero_jump_0.png"),(self.width,self.height))
        self.bk_jump_frame = pygame.transform.scale(pygame.transform.flip(pygame.image.load(f"./assets/hero/hero_jump_0.png"),True, False),(self.width,self.height))


        self.current_sprite = 0
        self.image = self.idle_frames[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_p,self.y_p)
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_img = self.mask.to_surface()
        self.facing_forward = True
        self.sword_rect = pygame.Rect(self.x_p, 550, 220, 140)
        self.health_bar = pygame.Rect(40,40 ,600 ,30)
    
        


    def idel_update(self):
        if self.current_sprite >= len(self.idle_frames):
            self.current_sprite = 0
        if self.facing_forward:
            self.image = self.idle_frames[int(self.current_sprite)]
        else:
            self.image = self.bk_idle_frames[int(self.current_sprite)]
#
    def move_forward(self):
        if self.x_p < 1760:
            self.facing_forward = True
            self.x_p += 6
            self.current_sprite += 0.2
            if self.current_sprite >= len(self.run_frames):
                self.current_sprite = 0
            self.image = self.run_frames[int(self.current_sprite)]


    def move_backward(self):

        if self.x_p > 40 :
            self.facing_forward = False
            self.x_p -= 6
            self.current_sprite += 0.2
            if self.current_sprite >= len(self.bk_run_frames):
                self.current_sprite = 0
            self.image = self.bk_run_frames[int(self.current_sprite)]
        

    def attack(self):
        if self.facing_forward:
            self.image = self.attack_frame
        else:
            self.image = self.bk_attack_frame




    
    def take_hit(self):
        
        self.health_bar.width -= 50
        if self.facing_forward:
            self.image = self.take_hit_frame
        else:
            self.image = self.bk_take_hit_frame


    def jump(self):
        if self.jumping:

            self.y_p -= self.velocity
            self.velocity -= 1
        
            if self.facing_forward:
                self.image = self.jump_frame
            else:
                self.image = self.bk_jump_frame
                    

            if self.velocity < -20:
                self.velocity = 20
                self.jumping = False

    def hero_update(self, screen):
        pygame.draw.rect(screen , (255,0,0), self.health_bar)
        self.current_sprite += 0.1
        self.idel_update()
        if self.hit:
            self.take_hit()
            self.hit = False
        if self.is_attacking:
            self.attack()
            self.is_attacking = False

        self.rect.center = (self.x_p ,self.y_p)
        if self.jumping:
            self.sword_rect.y = self.y_p -80
        if self.facing_forward:
            self.sword_rect.x = self.x_p + 60
        else:
            self.sword_rect.x = self.x_p - 280


