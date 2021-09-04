import time
from math import sqrt, pow
from multiprocessing import Process
from random import randint

import pygame

import Ball
import Bouncer
import Chat
import Gui
import ParserJuego

global user_list


def logger():
    log = Chat.Chat()
    log.log()


def users(nm_list, dim):
    last_user = ParserJuego.comprobar_chat()
    if last_user not in user_list and last_user is not None and last_user != '\n':
        user_list.append(last_user)
        new_name = Ball.Name(dim, last_user)
        nm_list.append(new_name)
    return nm_list


def fall(ball):
    screen.blit(ball.text, ball.text_rect)
    pygame.draw.circle(screen, ball.color, ball.pos, ball.size)
    ball.update_pos()
    ball.set_y()


def draw_starting_ball(ball):
    screen.blit(ball.text, ball.text_rect)
    pygame.draw.circle(screen, ball.color, ball.pos, ball.size)


def draw_hitbox(ball):
    pygame.draw.rect(screen, ball.color, ball.hitbox)


def bounce(ball, dim, bouncers):
    if ball.pos[0] not in range(10, dim[0] - 10):
        ball.bounce_wall()
    if ball.pos[1] > dim[1] + 10:
        return False
    ball.reset_trajectory()
    ball.collision_bouncer(bouncers)
    return True


def create_bouncers(dim, sz):
    min_dist = sz * 2
    for z in range(0, 50):
        new_rect = Bouncer.Bouncer(dim, sz)
        for y in range(0, len(rect_list)):
            rect = rect_list[y]
            dist = sqrt(pow((rect.rect.centerx - new_rect.rect.centerx), 2) +
                        pow((rect.rect.centery - new_rect.rect.centery), 2))
            if dist <= min_dist:
                y = 0
                new_rect = Bouncer.Bouncer(dim, sz)
        rect_list.append(new_rect)


def create_bottom(dim):
    rect_left = Bouncer.Bouncer(dim, 0)
    rect_left.set_exact_coords(0, dim[1] - 20, "left")
    rect_left.set_size((500, 20))
    rect_left.update_hitbox("left")
    rect_list.append(rect_left)
    rect_right = Bouncer.Bouncer(dim, 0)
    rect_right.set_exact_coords(dim[0] - 500, dim[1] - 20, "right")
    rect_right.set_size((500, 20))
    rect_right.update_hitbox("right")
    rect_list.append(rect_right)


def create_balls(nm_list, nms, dim):
    for x in range(0, 50):
        new_ball = Ball.Name(dim, nms[randint(0, len(nms) - 1)])
        name_list.append(new_ball)
    return nm_list


def gui():
    tk = Gui.Gui()
    tk.mainloop()
    return tk.game, tk.debug


def exit(scr, scores):
    rect = pygame.Rect(0, 0, dims[0], dims[1])
    pygame.draw.rect(scr, "white", rect)
    max_name = str(scores[len(scores) - 1])
    min_name = str(scores[0])
    if len(scores) > 0:
        min_time = font.render("Faster user:", True, (0, 0, 0))
        min_time_rect = min_time.get_rect()
        min_time_rect.center = (dims[0]/2, (dims[1]/2) - 64)

        max_time = font.render("Most time bouncing:", True, (0, 0, 0))
        max_time_rect = max_time.get_rect()
        max_time_rect.center = (dims[0] / 2, (dims[1] / 2) + 32)

        min_time_name = font.render(min_name, True, (0, 0, 0))
        min_time_name_rect = min_time_name.get_rect()
        min_time_name_rect.center = (dims[0] / 2, (dims[1] / 2) - 32)
        max_time_name = font.render(max_name, True, (0, 0, 0))
        max_time_name_rect = max_time_name.get_rect()
        max_time_name_rect.center = (dims[0] / 2, (dims[1] / 2) + 64)

        scr.blit(min_time, min_time_rect)
        scr.blit(max_time, max_time_rect)

        scr.blit(min_time_name, min_time_name_rect)
        scr.blit(max_time_name, max_time_name_rect)

    pygame.display.flip()
    time.sleep(5)


if __name__ == '__main__':

    game = gui()
    if game[0]:

        dims = (1280, 720)

        pygame.init()
        screen = pygame.display.set_mode(dims)
        pygame.display.set_caption("YastAPachinko")
        pygame.display.flip()

        font = pygame.font.Font('etc/arial.ttf', 32)
        text_debug = font.render('Debug', True, (0, 0, 255), (255, 255, 255))
        rect_debug = text_debug.get_rect()

        user_list = []
        name_list = []
        names = ["JOSÉ", "ANTONIO", "MANUEL", "FRANCISCO", "JUAN", "PEDRO", "LUIS", "ÁNGEL", "MIGUEL", "JESÚS",
                 "VICENTE", "RAMÓN", "RAFAEL", "JOSE MARÍA", "JOAQUÍN", "ENRIQUE", "FERNANDO", "EMILIO", "JULIÁN",
                 "FÉLIX", "ANDRÉS", "TOMÁS", "MARIANO", "JULIO", "JOSÉ LUIS", "SALVADOR", "AGUSTÍN", "SANTIAGO",
                 "DOMINGO", "ALFONSO", "JOSEP", "GREGORIO", "JAIME", "CARLOS", "FELIPE", "JOSÉ ANTONIO", "EDUARDO",
                 "PABLO", "RICARDO", "EUGENIO", "ALEJANDRO", "JOAN", "LORENZO", "JUAN JOSÉ", "JUAN ANTONIO", "DIEGO",
                 "DANIEL", "SEBASTIÁN", "IGNACIO", "MARTÍN", "MARÍA", "CARMEN", "JOSEFA", "DOLORES", "FRANCISCA",
                 "ISABEL", "ANTONIA", "PILAR", "MARÍA CARMEN", "TERESA", "CONCEPCIÓN", "JUANA", "ROSA", "MERCEDES",
                 "MANUELA", "ROSARIO", "ANA", "MARÍA LUISA", "ENCARNACIÓN", "JULIA", "MARÍA DOLORES", "MARÍA TERESA",
                 "ÁNGELES", "MARÍA PILAR", "ANGELA", "CONSUELO", "LUISA", "AMPARO", "MARGARITA", "MARÍA ÁNGELES",
                 "EMILIA", "FELISA", "VICTORIA", "CATALINA", "VICENTA", "MARÍA JOSEFA", "ASUNCIÓN", "JOSEFINA",
                 "AURORA", "MONTSERRAT", "ANA MARÍA", "MATILDE", "ESPERANZA", "PURIFICACIÓN", "ELENA", "NATIVIDAD",
                 "TRINIDAD", "PETRA", "LUCÍA", "MARÍA CONCEPCIÓN"]

        rect_list = []

        leader_list = []

        size = 20

        create_bouncers(dims, size)
        create_bottom(dims)

        clock = pygame.time.Clock()
        running = True

        hitbox = False
        debug = game[1]

        if debug:
            create_balls(name_list, names, dims[0])
        else:
            release = False
            p1 = Process(target=logger)
            p1.start()

        while running:

            if not debug:
                name = users(name_list, dims[0])
                if release and p1.is_alive():
                    p1.terminate()

            screen.fill("white")

            if len(name_list) > 0:
                for x in name_list:
                    if release:
                        x.inc_time()
                        fall(x)
                    else:
                        draw_starting_ball(x)
                    if debug and hitbox:
                        draw_hitbox(x)
                    dest = bounce(x, dims, rect_list)
                    if not dest:
                        leader_list.append(x.name)
                        name_list.remove(x)

            for x in rect_list:
                pygame.draw.rect(screen, (0, 0, 0), x)
                if debug:
                    pygame.draw.rect(screen, "red", x.bouncer_bottom)
                    pygame.draw.rect(screen, "green", x.bouncer_top)
                    pygame.draw.rect(screen, "blue", x.bouncer_left)
                    pygame.draw.rect(screen, "purple", x.bouncer_right)

            if debug:
                screen.blit(text_debug, rect_debug)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    if p1.is_alive():
                        p1.kill()
                    exit(screen, leader_list)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        release = True
                    if event.key == pygame.K_r:
                        name_list.clear()
                        user_list.clear()
                        rect_list.clear()
                        create_bouncers(dims, size)
                        if debug:
                            name_list = create_balls(name_list, names, dims[0])
                        create_bottom(dims)
                        release = False
                        if not p1.is_alive():
                            p1.terminate()
                            p1 = Process(target=logger)
                            p1.start()
                    if event.key == pygame.K_d and debug:
                        debug = False
                        name_list.clear()
                    if event.key == pygame.K_h and debug:
                        if hitbox:
                            hitbox = False
                        else:
                            hitbox = True
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        if p1.is_alive():
                            p1.kill()
                        exit(screen, leader_list)

            pygame.display.flip()
            clock.tick(60)
            if len(name_list) == 0 and release:
                running = False
                exit(screen, leader_list)
