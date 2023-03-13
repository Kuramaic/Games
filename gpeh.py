import pygame
from walls import Wall

pygame.init()

W = 1000
H = 1000
move = 1
sit = 1
stels = False
flag = False
a = 0
fall = 0
soft = True

jump = False

sc = pygame.display.set_mode((W, H))
sc_rect = sc.get_rect()
pygame.display.set_caption("0_0")

hero = pygame.image.load('hero_right.png')
hero = pygame.transform.scale(hero, (hero.get_rect().width * 4, hero.get_rect().height * 4))
hero_rect = hero.get_rect()
hero_rect.x = 450
hero_rect.y = 768

# wall = pygame.image.load('wall.png')
# wall1.rect = wall1.get_rect()
# wall1.rect.x = 800
# wall1.rect.y = 750


wall1=Wall(800, 750, 'wall.png', 6, 4)

# wall2 = pygame.transform.scale(wall, (wall.get_rect().width * 6, wall.get_rect().height * 4))
# wall2.rect = wall2.get_rect()
# wall2.rect.x = 1300
# wall2.rect.y = 750

wall2=Wall(1300, 750, 'wall.png', 6, 4)

# wall3 = pygame.transform.scale(wall, (wall.get_rect().width * 5, wall.get_rect().height * 4))
# wall3.rect = wall3.get_rect()
# wall3.rect.x = 1550
# wall3.rect.y = 350

wall3= Wall(1550,350,'wall.png',5,4)

# wall4 = pygame.transform.scale(wall, (wall.get_rect().width * 4, wall.get_rect().height * 4))
# wall4.rect = wall4.get_rect()
# wall4.rect.x = 2250
# wall4.rect.y = 350

wall4=Wall(2250,350,'wall.png',4,4)


# wall5 = pygame.transform.scale(wall, (wall.get_rect().width * 4, wall.get_rect().height * 4))
# wall5.rect = wall5.get_rect()
# wall5.rect.x = 2700
# wall5.rect.y = 250

wall5=Wall(2700,250,'wall.png',4,4)

# wall6 = pygame.transform.scale(wall, (wall.get_rect().width * 4, wall.get_rect().height * 4))
# wall6.rect = wall6.get_rect()
# wall6.rect.x = 3100
# wall6.rect.y = 200

wall6=Wall(3100,200,'wall.png',4,4)

ground = pygame.image.load('ground.png')
ground = pygame.transform.scale(ground, (ground.get_rect().width * 40, ground.get_rect().height // 2))
ground_rect = ground.get_rect()

town = pygame.image.load('town.png')
town = pygame.transform.scale(town, (town.get_rect().width * 10, town.get_rect().height * 10))
town_rect = town.get_rect()

platform00 = pygame.image.load('platform1.png')
platform00 = pygame.transform.scale(platform00, (platform00.get_rect().width * 5, platform00.get_rect().height * 3.5))
platform00_rect = platform00.get_rect()
platform00_rect.x = 1400
platform00_rect.y = 650

platform01 = pygame.image.load('platform1.png')
platform01 = pygame.transform.scale(platform01, (platform01.get_rect().width * 5, platform01.get_rect().height * 3.5))
platform01_rect = platform01.get_rect()
platform01_rect.x = 1400
platform01_rect.y = 550

platform02 = pygame.image.load('platform1.png')
platform02 = pygame.transform.scale(platform02, (platform02.get_rect().width * 5, platform02.get_rect().height * 3.5))
platform02_rect = platform02.get_rect()
platform02_rect.x = 1400
platform02_rect.y = 450

platform03 = pygame.image.load('platform1.png')
platform03 = pygame.transform.scale(platform03, (platform03.get_rect().width * 5, platform03.get_rect().height * 3.5))
platform03_rect = platform03.get_rect()
platform03_rect.x = 1400
platform03_rect.y = 350

platform04 = pygame.image.load('platform1.png')
platform04 = pygame.transform.scale(platform04, (platform04.get_rect().width * 5, platform04.get_rect().height * 3.5))
platform04_rect = platform04.get_rect()
platform04_rect.x = 2450
platform04_rect.y = 350

platform05 = pygame.image.load('platform1.png')
platform05 = pygame.transform.scale(platform05, (platform05.get_rect().width * 5, platform05.get_rect().height * 3.5))
platform05_rect = platform05.get_rect()
platform05_rect.x = 2450
platform05_rect.y = 450

platform06 = pygame.image.load('platform1.png')
platform06 = pygame.transform.scale(platform06, (platform06.get_rect().width * 5, platform06.get_rect().height * 3.5))
platform06_rect = platform06.get_rect()
platform06_rect.x = 2450
platform06_rect.y = 550

platform07 = pygame.image.load('platform1.png')
platform07 = pygame.transform.scale(platform07, (platform07.get_rect().width * 5, platform07.get_rect().height * 3.5))
platform07_rect = platform07.get_rect()
platform07_rect.x = 2450
platform07_rect.y = 650

platform08 = pygame.image.load('platform1.png')
platform08 = pygame.transform.scale(platform08, (platform08.get_rect().width * 5, platform08.get_rect().height * 3.5))
platform08_rect = platform08.get_rect()
platform08_rect.x = 2450
platform08_rect.y = 750

platform09 = pygame.image.load('platform1.png')
platform09 = pygame.transform.scale(platform09, (platform09.get_rect().width * 5, platform09.get_rect().height * 3.5))
platform09_rect = platform09.get_rect()
platform09_rect.x = 2450
platform09_rect.y = 850

platform = pygame.image.load('platform.png')
platform = pygame.transform.scale(platform, (platform.get_rect().width * 1.75, platform.get_rect().height * 1))
platform_rect = platform.get_rect()
platform_rect.x = 1750
platform_rect.y = 350

# house = pygame.image.load('gerald.png')
# house_rect = house.get_rect()
# house_rect.x = 4000
# house_rect.y = 800


ground_rect.bottom = sc_rect.bottom

hero_rect.bottom = ground_rect.top

FPS = 60
clock = pygame.time.Clock()

def fly(long):
    hero_rect.y -= long
    if 0 < hero_rect.right < W:
        if move == 1:
            wall1.rect.x += 5
            wall2.rect.x += 5
            wall3.rect.x += 5
            wall4.rect.x += 5
            wall5.rect.x += 5
            wall6.rect.x += 5
            ground_rect.x += 5
            platform_rect.x += 5
            platform00_rect.x += 5
            platform01_rect.x += 5
            platform02_rect.x += 5
            platform03_rect.x += 5
            platform04_rect.x += 5
            platform05_rect.x += 5
            platform06_rect.x += 5
            platform07_rect.x += 5
            platform08_rect.x += 5
            platform09_rect.x += 5
            #house_rect.x += 5
        if move == 2:
            wall1.rect.x -= 5
            wall2.rect.x -= 5
            wall3.rect.x -= 5
            wall4.rect.x -= 5
            wall5.rect.x -= 5
            wall6.rect.x -= 5
            ground_rect.x -= 5
            platform_rect.x -= 5
            platform00_rect.x -= 5
            platform01_rect.x -= 5
            platform02_rect.x -= 5
            platform03_rect.x -= 5
            platform04_rect.x -= 5
            platform05_rect.x -= 5
            platform06_rect.x -= 5
            platform07_rect.x -= 5
            platform08_rect.x -= 5
            platform09_rect.x -= 5
            #house_rect.x -= 5

    sc.blit(town, town_rect)
    sc.blit(wall1.image, wall1.rect)
    sc.blit(wall2.image, wall2.rect)
    sc.blit(wall3.image, wall3.rect)
    sc.blit(wall4.image, wall4.rect)
    sc.blit(wall5.image, wall5.rect)
    sc.blit(wall6.image, wall6.rect)
    sc.blit(platform, platform_rect)
    sc.blit(platform00, platform00_rect)
    sc.blit(platform01, platform01_rect)
    sc.blit(platform02, platform02_rect)
    sc.blit(platform03, platform03_rect)
    sc.blit(platform04, platform04_rect)
    sc.blit(platform05, platform05_rect)
    sc.blit(platform06, platform06_rect)
    sc.blit(platform07, platform07_rect)
    sc.blit(platform08, platform08_rect)
    sc.blit(platform09, platform09_rect)
    #sc.blit(house, house_rect)
    sc.blit(hero, hero_rect)
    sc.blit(ground, ground_rect)
    clock.tick(FPS)
    pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()

        # gravitazija
    if hero_rect.bottom < ground_rect.top:
        if wall1.rect.top + 9 > hero_rect.bottom >= wall1.rect.top and wall1.rect.x + 164 > hero_rect.x > wall1.rect.x - 52:
            hero_rect.bottom = wall1.rect.top
            fall = 0
        elif wall2.rect.top + 9 > hero_rect.bottom >= wall2.rect.top and wall2.rect.x + 200 > hero_rect.x > wall2.rect.x - 52:
            hero_rect.bottom = wall2.rect.top
            fall = 0
        elif wall3.rect.top + 9 > hero_rect.bottom >= wall3.rect.top and wall3.rect.x + 164 > hero_rect.x > wall3.rect.x - 52:
            hero_rect.bottom = wall3.rect.top
            fall = 0
        elif wall4.rect.top + 9 > hero_rect.bottom >= wall4.rect.top and wall4.rect.x + 164 > hero_rect.x > wall4.rect.x - 52:
            hero_rect.bottom = wall4.rect.top
            fall = 0
        elif wall5.rect.top + 9 > hero_rect.bottom >= wall5.rect.top and wall5.rect.x + 164 > hero_rect.x > wall5.rect.x - 52:
            hero_rect.bottom = wall5.rect.top
            fall = 0
        elif wall6.rect.top + 9 > hero_rect.bottom >= wall6.rect.top and wall6.rect.x + 164 > hero_rect.x > wall6.rect.x - 52:
            hero_rect.bottom = wall6.rect.top
            fall = 0
        elif platform_rect.top + 9 > hero_rect.bottom >= platform_rect.top and platform_rect.x + 500 > hero_rect.x > platform_rect.x - 52:
            hero_rect.bottom = platform_rect.top
            fall = 0
        elif platform00_rect.top + 9 > hero_rect.bottom >= platform00_rect.top and platform00_rect.x + 80 > hero_rect.x > platform00_rect.x - 52:
            hero_rect.bottom = platform00_rect.top
            fall = 0
        elif platform01_rect.top + 9 > hero_rect.bottom >= platform01_rect.top and platform01_rect.x + 80 > hero_rect.x > platform01_rect.x - 52:
            hero_rect.bottom = platform01_rect.top
            fall = 0
        elif platform02_rect.top + 9 > hero_rect.bottom >= platform02_rect.top and platform02_rect.x + 80 > hero_rect.x > platform02_rect.x - 52:
            hero_rect.bottom = platform02_rect.top
            fall = 0
        elif platform03_rect.top + 9 > hero_rect.bottom >= platform03_rect.top and platform03_rect.x + 80 > hero_rect.x > platform03_rect.x - 52:
            hero_rect.bottom = platform03_rect.top
            fall = 0
        elif platform04_rect.top + 9 > hero_rect.bottom >= platform04_rect.top and platform04_rect.x + 80 > hero_rect.x > platform04_rect.x - 52:
            hero_rect.bottom = platform04_rect.top
            fall = 0
        elif platform05_rect.top + 9 > hero_rect.bottom >= platform05_rect.top and platform05_rect.x + 80 > hero_rect.x > platform05_rect.x - 52:
            hero_rect.bottom = platform05_rect.top
            fall = 0
        elif platform06_rect.top + 9 > hero_rect.bottom >= platform06_rect.top and platform06_rect.x + 80 > hero_rect.x > platform06_rect.x - 52:
            hero_rect.bottom = platform06_rect.top
            fall = 0
        elif platform07_rect.top + 9 > hero_rect.bottom >= platform07_rect.top and platform07_rect.x + 80 > hero_rect.x > platform07_rect.x - 52:
            hero_rect.bottom = platform07_rect.top
            fall = 0
        elif platform08_rect.top + 9 > hero_rect.bottom >= platform08_rect.top and platform08_rect.x + 80 > hero_rect.x > platform08_rect.x - 52:
            hero_rect.bottom = platform08_rect.top
            fall = 0
        elif platform09_rect.top + 9 > hero_rect.bottom >= platform09_rect.top and platform09_rect.x + 80 > hero_rect.x > platform09_rect.x - 52:
            hero_rect.bottom = platform09_rect.top
            fall = 0
        else:
            if fall <= 60:
                hero_rect.bottom += 5
                fall += 1
            elif 60 < fall <= 120:
                hero_rect.bottom += 7
                fall += 1
            elif 120 < fall:
                hero_rect.bottom += 9

    if hero_rect.bottom == ground_rect.top:
        fall = 0

    if keys[1073742049]:
        if hero_rect.bottom == platform_rect.top and platform_rect.x + 400 > hero_rect.x > platform_rect.x:
            hero_rect.y += 5
        elif hero_rect.bottom == platform00_rect.top and platform00_rect.x + 80 > hero_rect.x > platform00_rect.x - 52:
            hero_rect.y += 5
        elif hero_rect.bottom == platform01_rect.top and platform01_rect.x + 80 > hero_rect.x > platform01_rect.x - 52:
            hero_rect.y += 5
        elif hero_rect.bottom == platform02_rect.top and platform02_rect.x + 80 > hero_rect.x > platform02_rect.x - 52:
            hero_rect.y += 5
        elif hero_rect.bottom == platform03_rect.top and platform03_rect.x + 80 > hero_rect.x > platform03_rect.x - 52:
            hero_rect.y += 5
        elif hero_rect.bottom == platform04_rect.top and platform04_rect.x + 80 > hero_rect.x > platform04_rect.x - 52:
            hero_rect.y += 5
        elif hero_rect.bottom == platform05_rect.top and platform05_rect.x + 80 > hero_rect.x > platform05_rect.x - 52:
            hero_rect.y += 5
        elif hero_rect.bottom == platform06_rect.top and platform06_rect.x + 80 > hero_rect.x > platform06_rect.x - 52:
            hero_rect.y += 5
        elif hero_rect.bottom == platform07_rect.top and platform07_rect.x + 80 > hero_rect.x > platform07_rect.x - 52:
            hero_rect.y += 5
        elif hero_rect.bottom == platform08_rect.top and platform08_rect.x + 80 > hero_rect.x > platform08_rect.x - 52:
            hero_rect.y += 5
        elif hero_rect.bottom == platform09_rect.top and platform09_rect.x + 80 > hero_rect.x > platform09_rect.x - 52:
            hero_rect.y += 5
        move = 0



    if keys[97] and not stels:
        if ground_rect.x == 300:
            wall1.rect.x = 900
            wall2.rect.x = 1400
            wall3.rect.x = 1800
            wall4.rect.x = 2500
            wall5.rect.x = 2700
            wall6.rect.x = 3400
            platform_rect.x = 2900
        else:
            hero = pygame.image.load('hero_left.png')
            hero = pygame.transform.scale(hero, (hero.get_rect().width * 4, hero.get_rect().height * 4))
            if soft and hero_rect.left > 0:
                hero_rect.x -= 5
            if not soft and hero_rect.left > 0:
                wall1.rect.x += 5
                wall2.rect.x += 5
                wall3.rect.x += 5
                wall4.rect.x += 5
                wall5.rect.x += 5
                wall6.rect.x += 5
                ground_rect.x += 5
                platform_rect.x += 5
                platform00_rect.x += 5
                platform01_rect.x += 5
                platform02_rect.x += 5
                platform03_rect.x += 5
                platform04_rect.x += 5
                platform05_rect.x += 5
                platform06_rect.x += 5
                platform07_rect.x += 5
                platform08_rect.x += 5
                platform09_rect.x += 5
                #house_rect.x += 5
        move = 1
        sit = 1
    elif keys[100] and not stels:
        hero = pygame.image.load('hero_right.png')
        hero = pygame.transform.scale(hero, (hero.get_rect().width * 4, hero.get_rect().height * 4))
        if ground_rect.x == -4000:
            wall1.rect.x = -3400
            wall2.rect.x = -2900
            wall3.rect.x = -2500
            wall4.rect.x = -1800
            wall5.rect.x = -1600
            wall6.rect.x = -900
            platform_rect.x = -1400
        else:
            if soft and hero_rect.right < W:
                hero_rect.x += 5

            if not soft and hero_rect.right < W:
                wall1.rect.x -= 5
                wall2.rect.x -= 5
                wall3.rect.x -= 5
                wall4.rect.x -= 5
                wall5.rect.x -= 5
                wall6.rect.x -= 5
                ground_rect.x -= 5
                platform_rect.x -= 5
                platform00_rect.x -= 5
                platform01_rect.x -= 5
                platform02_rect.x -= 5
                platform03_rect.x -= 5
                platform04_rect.x -= 5
                platform05_rect.x -= 5
                platform06_rect.x -= 5
                platform07_rect.x -= 5
                platform08_rect.x -= 5
                platform09_rect.x -= 5
                #house_rect.x -= 5
        move = 2
        sit = 2

    else:
        memory_move = move
        move = 0

    if keys[115]:
        memory_x = hero_rect.x
        memory_y = hero_rect.y
        if sit == 1 and not stels:
            hero = pygame.image.load('stels_left.png')
            hero = pygame.transform.scale(hero, (hero.get_rect().width * 4, hero.get_rect().height * 4))
            hero_rect = hero.get_rect()
            hero_rect.x = memory_x
            hero_rect.y = memory_y + 32
            stels = True
            flag = True
        if sit == 1:
            hero = pygame.image.load('stels_left.png')
            hero = pygame.transform.scale(hero, (hero.get_rect().width * 4, hero.get_rect().height * 4))
        if sit == 2 and not stels:
            hero = pygame.image.load('stels_right.png')
            hero = pygame.transform.scale(hero, (hero.get_rect().width * 4, hero.get_rect().height * 4))
            hero_rect = hero.get_rect()
            hero_rect.x = memory_x
            hero_rect.y = memory_y + 32
            stels = True
            flag = True
        if sit == 2:
            hero = pygame.image.load('stels_right.png')
            hero = pygame.transform.scale(hero, (hero.get_rect().width * 4, hero.get_rect().height * 4))
    elif not keys[115]:
        memory_x = hero_rect.x
        memory_y = hero_rect.y
        if sit == 1 and stels:
            hero = pygame.image.load('hero_left.png')
            hero = pygame.transform.scale(hero, (hero.get_rect().width * 4, hero.get_rect().height * 4))
            hero_rect = hero.get_rect()
            hero_rect.x = memory_x
            hero_rect.y = memory_y - 32
            stels = False
        elif sit == 2 and stels:
            hero = pygame.image.load('hero_right.png')
            hero = pygame.transform.scale(hero, (hero.get_rect().width * 4, hero.get_rect().height * 4))
            hero_rect = hero.get_rect()
            hero_rect.x = memory_x
            hero_rect.y = memory_y - 32
            stels = False
            move = 0
        
    if keys[32]:
        if hero_rect.top > 0 and hero_rect.bottom == ground_rect.top:
            jump = True
        elif wall1.rect.x + 200 > hero_rect.x > wall1.rect.x - 93 and hero_rect.bottom == wall1.rect.top:
            jump = True
        elif wall2.rect.x + 200 > hero_rect.x > wall2.rect.x - 93 and hero_rect.bottom == wall2.rect.top:
            jump = True
        elif wall3.rect.x + 200 > hero_rect.x > wall3.rect.x - 93 and hero_rect.bottom == wall3.rect.top:
            jump = True
        elif wall4.rect.x + 200 > hero_rect.x > wall4.rect.x - 93 and hero_rect.bottom == wall4.rect.top:
            jump = True
        elif wall5.rect.x + 200 > hero_rect.x > wall5.rect.x - 93 and hero_rect.bottom == wall5.rect.top:
            jump = True
        elif wall6.rect.x + 200 > hero_rect.x > wall6.rect.x - 93 and hero_rect.bottom == wall6.rect.top:
            jump = True
        elif hero_rect.bottom == platform_rect.top and platform_rect.x + 500 > hero_rect.x > platform_rect.x - 93:
            jump = True
        elif hero_rect.bottom == platform00_rect.top and platform00_rect.x + 80 > hero_rect.x > platform00_rect.x - 93:
            jump = True
        elif hero_rect.bottom == platform01_rect.top and platform01_rect.x + 80 > hero_rect.x > platform01_rect.x - 93:
            jump = True
        elif hero_rect.bottom == platform02_rect.top and platform02_rect.x + 80 > hero_rect.x > platform02_rect.x - 93:
            jump = True
        elif hero_rect.bottom == platform03_rect.top and platform03_rect.x + 80 > hero_rect.x > platform03_rect.x - 93:
            jump = True
        elif hero_rect.bottom == platform04_rect.top and platform04_rect.x + 80 > hero_rect.x > platform04_rect.x - 93:
            jump = True
        elif hero_rect.bottom == platform05_rect.top and platform05_rect.x + 80 > hero_rect.x > platform05_rect.x - 93:
            jump = True
        elif hero_rect.bottom == platform06_rect.top and platform06_rect.x + 80 > hero_rect.x > platform06_rect.x - 93:
            jump = True
        elif hero_rect.bottom == platform07_rect.top and platform07_rect.x + 80 > hero_rect.x > platform07_rect.x - 93:
            jump = True
        elif hero_rect.bottom == platform08_rect.top and platform08_rect.x + 80 > hero_rect.x > platform08_rect.x - 93:
            jump = True
        elif hero_rect.bottom == platform09_rect.top and platform09_rect.x + 80 > hero_rect.x > platform09_rect.x - 93:
            jump = True
        if jump:
            jump = False
            for _ in range(27):
                fly(12)
                if hero_rect.top == wall1.rect.bottom and wall1.rect.x + 200 > hero_rect.x > wall1.rect.x - 93:
                    break
                elif hero_rect.top == wall2.rect.bottom and wall2.rect.x + 200 > hero_rect.x > wall2.rect.x - 93:
                    break
                elif hero_rect.top == wall3.rect.bottom and wall3.rect.x + 200 > hero_rect.x > wall3.rect.x - 93:
                    break
                elif hero_rect.top == wall4.rect.bottom and wall4.rect.x + 250 > hero_rect.x > wall4.rect.x - 93:
                    break
                elif hero_rect.top == wall5.rect.bottom and wall5.rect.x + 200 > hero_rect.x > wall5.rect.x - 93:
                    break
                elif hero_rect.top == wall6.rect.bottom and wall6.rect.x + 200 > hero_rect.x > wall6.rect.x - 93:
                    break

                if hero_rect.right > wall1.rect.left and hero_rect.colliderect(wall1.rect) is True and hero_rect.x < wall1.rect.x:
                    break
                elif hero_rect.right > wall2.rect.left and hero_rect.colliderect(wall2.rect) is True and hero_rect.x < wall2.rect.x:
                    break
                elif hero_rect.right > wall3.rect.left and hero_rect.colliderect(wall3.rect) is True and hero_rect.x < wall3.rect.x:
                    break
                elif hero_rect.right > wall4.rect.left and hero_rect.colliderect(wall4.rect) is True and hero_rect.x < wall4.rect.x:
                    break
                elif hero_rect.right > wall5.rect.left and hero_rect.colliderect(wall5.rect) is True and hero_rect.x < wall5.rect.x:
                    break
                elif hero_rect.right > wall6.rect.left and hero_rect.colliderect(wall6.rect) is True and hero_rect.x < wall6.rect.x:
                    break

                if hero_rect.left < wall1.rect.right and hero_rect.colliderect(wall1.rect) is True and hero_rect.x > wall1.rect.x:
                    break
                elif hero_rect.left < wall2.rect.right and hero_rect.colliderect(wall2.rect) is True and hero_rect.x > wall2.rect.x:
                    break
                elif hero_rect.left < wall3.rect.right and hero_rect.colliderect(wall3.rect) is True and hero_rect.x > wall3.rect.x:
                    break
                elif hero_rect.left < wall4.rect.right and hero_rect.colliderect(wall4.rect) is True and hero_rect.x > wall4.rect.x: 
                    break
                elif hero_rect.left < wall5.rect.right and hero_rect.colliderect(wall5.rect) is True and hero_rect.x > wall5.rect.x:
                    break
                elif hero_rect.left < wall6.rect.right and hero_rect.colliderect(wall6.rect) is True and hero_rect.x > wall6.rect.x:
                    break
                if hero_rect.y <= 0:
                    break




    if hero_rect.right > wall1.rect.left and hero_rect.colliderect(wall1.rect) is True and hero_rect.x < wall1.rect.x and hero_rect.top < wall1.rect.top and hero_rect.bottom > wall1.rect.bottom + 9:
        hero_rect.right = wall1.rect.left
    elif hero_rect.right > wall2.rect.left and hero_rect.colliderect(wall2.rect) is True and hero_rect.x < wall2.rect.x and hero_rect.top < wall2.rect.top and hero_rect.bottom > wall2.rect.bottom + 9:
        hero_rect.right = wall2.rect.left
    elif hero_rect.right > wall3.rect.left and hero_rect.colliderect(wall3.rect) is True and hero_rect.x < wall3.rect.x and hero_rect.top < wall3.rect.top and hero_rect.bottom > wall3.rect.bottom + 9:
        hero_rect.right = wall3.rect.left
    elif hero_rect.right > wall4.rect.left and hero_rect.colliderect(wall4.rect) is True and hero_rect.x < wall4.rect.x and hero_rect.top < wall4.rect.top and hero_rect.bottom > wall4.rect.bottom + 9:
        hero_rect.right = wall4.rect.left
    elif hero_rect.right > wall5.rect.left and hero_rect.colliderect(wall5.rect) is True and hero_rect.x < wall5.rect.x and hero_rect.top < wall5.rect.top and hero_rect.bottom > wall5.rect.bottom + 9:
        hero_rect.right = wall5.rect.left
    elif hero_rect.right > wall6.rect.left and hero_rect.colliderect(wall6.rect) is True and hero_rect.x < wall6.rect.x and hero_rect.top < wall6.rect.top and hero_rect.bottom > wall6.rect.bottom + 9:
        hero_rect.right = wall6.rect.left

    elif hero_rect.left < wall1.rect.right and hero_rect.colliderect(wall1.rect) is True and hero_rect.x > wall1.rect.x and hero_rect.top < wall1.rect.top and hero_rect.bottom > wall1.rect.bottom + 9:
        hero_rect.left = wall1.rect.right
    elif hero_rect.left < wall2.rect.right and hero_rect.colliderect(wall2.rect) is True and hero_rect.x > wall2.rect.x and hero_rect.top < wall2.rect.top and hero_rect.bottom > wall2.rect.bottom + 9:
        hero_rect.left = wall2.rect.right
    elif hero_rect.left < wall3.rect.right and hero_rect.colliderect(wall3.rect) is True and hero_rect.x > wall3.rect.x and hero_rect.top < wall3.rect.top and hero_rect.bottom > wall3.rect.bottom + 9:
        hero_rect.left = wall3.rect.right
    elif hero_rect.left < wall4.rect.right and hero_rect.colliderect(wall4.rect) is True and hero_rect.x > wall4.rect.x and hero_rect.top < wall4.rect.top and hero_rect.bottom > wall4.rect.bottom + 9:
        hero_rect.left = wall4.rect.right
    elif hero_rect.left < wall5.rect.right and hero_rect.colliderect(wall5.rect) is True and hero_rect.x > wall5.rect.x and hero_rect.top < wall5.rect.top and hero_rect.bottom > wall5.rect.bottom + 9:
        hero_rect.left = wall5.rect.right
    elif hero_rect.left < wall6.rect.right and hero_rect.colliderect(wall6.rect) is True and hero_rect.x > wall6.rect.x and hero_rect.top < wall6.rect.top and hero_rect.bottom > wall6.rect.bottom + 9:
        hero_rect.left = wall6.rect.right

    if hero_rect.bottom > ground_rect.top:
        hero_rect.bottom = ground_rect.top

    if a == 15:
        a = 0
    
    a += 1

    if move == 0 and memory_move == 1:
        hero = pygame.image.load('hero_left.png')
        hero = pygame.transform.scale(hero, (hero.get_rect().width * 4, hero.get_rect().height * 4))
    elif move == 0 and memory_move == 2:
        hero = pygame.image.load('hero_right.png')
        hero = pygame.transform.scale(hero, (hero.get_rect().width * 4, hero.get_rect().height * 4))

    if hero_rect.x > 600 or hero_rect.x < 300:
        soft = False
    if move == 0 and hero_rect.x < 450 and not soft:
        hero_rect.x += 10
        wall1.rect.x += 10
        wall2.rect.x += 10
        wall3.rect.x += 10
        wall4.rect.x += 10
        wall5.rect.x += 10
        wall6.rect.x += 10
        ground_rect.x += 10
        platform_rect.x += 10
        platform00_rect.x += 10
        platform01_rect.x += 10
        platform02_rect.x += 10
        platform03_rect.x += 10
        platform04_rect.x += 10
        platform05_rect.x += 10
        platform06_rect.x += 10
        platform07_rect.x += 10
        platform08_rect.x += 10
        platform09_rect.x += 10
    if move == 0 and hero_rect.x > 450 and not soft:
        hero_rect.x -= 10
        wall1.rect.x -= 10
        wall2.rect.x -= 10
        wall3.rect.x -= 10
        wall4.rect.x -= 10
        wall5.rect.x -= 10
        wall6.rect.x -= 10
        ground_rect.x -= 10
        platform_rect.x -= 10
        platform00_rect.x -= 10
        platform01_rect.x -= 10
        platform02_rect.x -= 10
        platform03_rect.x -= 10
        platform04_rect.x -= 10
        platform05_rect.x -= 10
        platform06_rect.x -= 10
        platform07_rect.x -= 10
        platform08_rect.x -= 10
        platform09_rect.x -= 10
    if 440 < hero_rect.x < 460:
        soft = True

    sc.blit(town, town_rect)
    sc.blit(ground, ground_rect)
    sc.blit(wall1.image, wall1.rect)
    sc.blit(wall2.image, wall2.rect)
    sc.blit(wall3.image, wall3.rect)
    sc.blit(wall4.image, wall4.rect)
    sc.blit(wall5.image, wall5.rect)
    sc.blit(wall6.image, wall6.rect)
    sc.blit(platform, platform_rect)
    sc.blit(platform00, platform00_rect)
    sc.blit(platform01, platform01_rect)
    sc.blit(platform02, platform02_rect)
    sc.blit(platform03, platform03_rect)
    sc.blit(platform04, platform04_rect)
    sc.blit(platform05, platform05_rect)
    sc.blit(platform06, platform06_rect)
    sc.blit(platform07, platform07_rect)
    sc.blit(platform08, platform08_rect)
    sc.blit(platform09, platform09_rect)
    #sc.blit(house, house_rect)
    sc.blit(hero, hero_rect)
    sc.blit(ground, ground_rect)
    clock.tick(FPS)
    pygame.display.update()