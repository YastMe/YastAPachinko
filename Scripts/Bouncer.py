from random import randint

import pygame.draw


class Bouncer:

    def __init__(self, dims, size):
        self.left = randint(100, dims[0] - 100)
        self.top = randint(100, dims[1] - 100)
        self.rect = pygame.Rect(self.left, self.top, size, size)
        self.bouncer_top = pygame.Rect(self.left, self.top, size-1, 1)
        self.bouncer_bottom = pygame.Rect(self.left, self.top, size-1, 1)
        self.bouncer_bottom.center = (self.rect.centerx, self.rect.centery + (size/2) - 1)
        self.bouncer_left = pygame.Rect(self.left, self.top, 1, size-1)
        self.bouncer_right = pygame.Rect(self.left + size-1, self.top, 1, size-1)

    def set_coords(self, dims):
        self.rect.center = (randint(100, dims[0] - 100), randint(100, dims[1] - 100))

    def set_exact_coords(self, x, y, side):
        if side == "left":
            self.rect.topleft = (x, y)
        else:
            self.rect.topright = (x, y)

    def set_size(self, size):
        self.rect.size = size

    def update_hitbox(self, side):
        if side == "left":
            self.bouncer_right.size = (1, self.rect.size[1] - 2)
            self.bouncer_right.center = self.rect.midright
            self.bouncer_left.size = (0, 0)
            self.bouncer_left.center = self.rect.midleft
        else:
            self.bouncer_left.size = (1, self.rect.size[1] - 2)
            self.bouncer_left.center = self.rect.midleft
            self.bouncer_right.size = (0, 0)
            self.bouncer_right.center = self.rect.midright

        self.bouncer_bottom.size = (self.rect.size[0] - 2, 0)
        self.bouncer_top.size = (self.rect.size[0] - 2, 1)
        self.bouncer_bottom.center = self.rect.midbottom
        self.bouncer_top.center = self.rect.midtop
