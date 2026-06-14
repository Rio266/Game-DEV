import pgzrun, random
WIDTH = 1000
HEIGHT = 800

spaceship = Actor("spaceship")
spaceship.pos = (WIDTH/2, HEIGHT - 60)
speed = 5

bullets = []
bees = []
for i in range(6):
    for j in range(4):
        bees.append(Actor("spaceship_bee"))
        bees[-1].x = 100 + 50*i
        bees[-1].y = 80 + 50*j

score = 0
direction = 1
spaceship.dead = False
spaceship.countdown = 90

def update():
    global score, direction
    move_down = False
    if spaceship.dead == False:
        if keyboard.a or keyboard.left:
            spaceship.x -= speed
            if spaceship.x <= 0:
                spaceship.x = 0
        elif keyboard.d or keyboard.right:
            spaceship.x += speed
            if spaceship.x >= 1000:
                spaceship.x = 1000
    for i in bullets:
        if i.y <= 0:
            bullets.remove(i)
        else:
            i.y -= 10
    if len(bees) == 0:
        gameover()
    if len(bees) > 0 and (bees[-1].x > WIDTH - 18 or bees[0].x < 18):
        move_down = True
        direction = direction*-1
    for i in bees:
        i.x += 5*direction
        if move_down == True:
            i.y += 100
        if i.y > HEIGHT:
            bees.remove(i)
        for j in bullets:
            if i.colliderect(j):
                score += 100
                bullets.remove(j)
                bees.remove(i)
                if len(bees) == 0:
                    gameover()
        if i.colliderect(spaceship):
            spaceship.dead = True
    if spaceship.dead:
        spaceship.countdown -= 1
    if spaceship.countdown == 0:
        spaceship.dead = False
        spaceship.countdown = 90
def draw():
    screen.clear()
    screen.fill("black")
    for i in bees:
        i.draw()
    spaceship.draw()
    screen.draw.text(f"Score = {score}", (WIDTH/2, 20))
    for i in bullets:
        i.draw()
    if len(bees) == 0:
        gameover()
def on_key_down(key):
    if spaceship.dead == False:
        if key == keys.SPACE:
            bullets.append(Actor("spaceship_bullet"))
            bullets[-1].x = spaceship.x
            bullets[-1].y = spaceship.y - 50
def gameover():
    screen.draw.text("Well done! The game is over.", (20, 20))
pgzrun.go()