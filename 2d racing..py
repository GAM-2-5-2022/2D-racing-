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
    app.blit(bg, (0, 0))
    app.blit(strip, (d, d1))
    app.blit(strip, (d, d2))
    app.blit(strip, (d, d3))
    app.blit(strip, (d, d4))
    app.blit(strip, (d, d5))
    app.blit(green_car, (x, y))
    app.blit(yellow_car, (a, a1))
    app.blit(blue_car, (c, c1))
    app.blit(white_car, (b, b1))
    pygame.display.update()

runtime = True
while runtime:
    pygame.time.delay(70)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runtime=False
            
    keys_pressed=pygame.key.get_pressed()

    if keys_pressed[pygame.K_RIGHT]:
        if x < 375:
            x = x + speed
            
    if keys_pressed[pygame.K_LEFT]:
        if x > 70:
            x = x - speed
            
    if keys_pressed[pygame.K_DOWN]:
        if y < 400:
            y = y + speed
            
    if keys_pressed[pygame.K_UP]:
        if y > 0:
            y = y - speed


    if a1 >= 400:
        a1 = 0
        a = random.randint(70, 175)
        score = score + 1

    if c1 >= 400:
        c1 = 0
        c = random.randint(175, 275)
        score = score + 1

    if b1 >= 400:
        b1 = 0
        b = random.randint(275, 375)
        score = score + 1


    if d1 >= 500:
        d1 = 0
    if d2 >= 500:
        d2 = 0
    if d3 >= 500:
        d3 = 0
    if d4 >= 500:
        d4 = 0
    if d5 >= 500:
        d5 = 0

    if score % 79 == 0:
        speed = speed + 1


    a1 = a1 + speed
    c1 = c1 + speed
    b1 = b1 + speed
    d1 = d1 + speed
    d2 = d2 + speed
    d3 = d3 + speed
    d4 = d4 + speed
    d5 = d5 + speed

    abc()
 

running = True
while running:
    pygame.display.flip()
    app.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
