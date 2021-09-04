from random import randint

import pygame


class Name:
    font = None
    text_rect = None
    hitbox = None
    pos = None
    color = None
    trajectory = None
    max_vel = 15
    gravity = 0.25
    direction = 0
    ball_bottom_left = None
    ball_bottom_right = None
    ball_top_left = None
    ball_top_right = None

    def __init__(self, x, name):
        pygame.init()
        font = pygame.font.Font('etc/arial.ttf', 10)

        self.name = name

        self.text = font.render(name, True, (0, 0, 0))
        self.text.set_alpha(127)
        self.text_rect = self.text.get_rect()

        top_y = 30
        min_x = 100
        max_x = x - 50
        self.text_rect.topright = (randint(min_x, max_x), top_y)

        self.pos = (self.text_rect.centerx, self.text_rect.centery + 20)
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.size = 10
        x = randint(-10, 10)
        while x == 0:
            x = randint(-10, 10)
        self.trajectory = (x, 5)

        self.hitbox = pygame.Rect(self.pos[0], self.pos[1], 20, 20)

        self.time = 0

    def set_y(self):
        self.text_rect.center = (self.pos[0], self.pos[1] - 20)
        self.set_hitbox()

    def set_hitbox(self):
        self.hitbox.center = self.pos
        self.ball_bottom_right = self.hitbox.clipline(self.hitbox.center, self.hitbox.bottomright)
        self.ball_bottom_right = pygame.Rect(self.ball_bottom_right)
        self.ball_bottom_left = self.hitbox.clipline(self.hitbox.center, self.hitbox.bottomleft)
        self.ball_bottom_left = pygame.Rect(self.ball_bottom_left)
        self.ball_top_right = self.hitbox.clipline(self.hitbox.center, self.hitbox.topright)
        self.ball_top_right = pygame.Rect(self.ball_top_right)
        self.ball_top_left = self.hitbox.clipline(self.hitbox.center, self.hitbox.topleft)
        self.ball_top_left = pygame.Rect(self.ball_top_left)

    def bounce_floor(self):
        self.trajectory = (self.trajectory[0], randint(-15, -5))

    def bounce_ceiling(self):
        self.trajectory = (self.trajectory[0], randint(5, 15))

    def bounce_wall(self):
        self.trajectory = (self.trajectory[0] * -1, self.trajectory[1])

    def set_direction(self, dire):
        self.direction = dire

    def reset_trajectory(self):
        if self.trajectory[1] < self.max_vel:
            self.trajectory = (self.trajectory[0], self.trajectory[1] + self.gravity)

    def update_pos(self):
        self.pos = (self.pos[0] + self.trajectory[0], self.pos[1] + self.trajectory[1] + self.gravity)

    def collision_bouncer(self, bouncers):
        for x in bouncers:
            if self.hitbox.colliderect(x.bouncer_left) or self.hitbox.colliderect(x.bouncer_right):
                self.bounce_wall()
            if self.hitbox.colliderect(x):
                if self.hitbox.colliderect(x.bouncer_top):
                    self.bounce_floor()
                elif self.hitbox.colliderect(x.bouncer_bottom):
                    self.bounce_ceiling()

    def inc_time(self):
        self.time += 1
