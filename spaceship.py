import pgzrun
WIDTH = 1000
HEIGHT = 400

spaceship = Actor("spaceship")
spaceship.pos = (WIDTH/2, HEIGHT - 60)
speed = 5

bullets = []
bees = []
bees.append(Actor("spaceship_bee"))
bees[-1].x = 10
bees[-1].y = -100

score = 0

def update():
    global score
    if keyboard.a or keyboard.left:
        spaceship.x -= speed
        if spaceship.x <= 0:
            spaceship.x = 0
    elif keyboard.d or keyboard.right:
        spaceship.x += speed
        if spaceship.x >= 1000:
            spaceship.x = 1000
def draw():
    screen.clear()
    screen.fill("black")
    for i in bees:
        i.draw()
    spaceship.draw()
    screen.draw.text(f"Score = {score}", (WIDTH/2, 20))
pgzrun.go()