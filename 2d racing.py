import pygame
import random

pygame.init()

app = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Game")

bg = pygame.image.load('D:\\Razredi\\2.5\\Viktor Versic\\slike\\cesta2.jpg')
blue_car = pygame.image.load('D:\\Razredi\\2.5\\Viktor Versic\\slike\\pc.png')
yellow_car = pygame.image.load('D:\\Razredi\\2.5\\Viktor Versic\\slike\\yc.png')
green_car = pygame.image.load('D:\\Razredi\\2.5\\Viktor Versic\\slike\\zc.png')
white_car = pygame.image.load('D:\\Razredi\\2.5\\Viktor Versic\\slike\\bc.png')
strip = pygame.image.load('D:\\Razredi\\2.5\\Viktor Versic\\slike\\strip.png')

x = 160
y = 400
speed = 1
score = 0

a1 = 0
b1 = 350
c1 = 175
a = random.randint(370, 375)
b = random.randint(370, 375)
c = random.randint(370, 375)

d = 250
d1 = 5
d2 = 100
d3 = 200
d4 = 300
d5 = 400

def abc():
    app.blit(strip, (d, d1))
    app.blit(strip, (d, d2))
    app.blit(strip, (d, d3))
    app.blit(strip, (d, d4))
    app.blit(strip, (d, d5))

    app.blit(green_car, (x, y))
    app.blit(yellow_car, (a, a1))
    app.blit(blue_car, (c, c1))
    app.bilt(white_car, (b, b1))

    pygame.display.update()
    
running = True
while running:
    pygame.display.flip()
    app.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
