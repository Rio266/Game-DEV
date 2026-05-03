import pgzrun, random, time
WIDTH = 600
HEIGHT = 480
bee = Actor("bee")
bee.pos = 300, 300
score = 0
gameover = False

flower = Actor("flower")
flower.pos = 400, 400

def draw():
    screen.blit("grass", (0, 0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score : "+str(score), color = "Orange", midtop = (300, 100), fontsize = 20)
    if gameover:
        screen.fill("green")
        screen.draw.text("Time is up. Your score is "+str(score), color = "Red", midtop = (300, 300), fontsize = 30)
def update():
    global score
    if keyboard.left:
        bee.x -= 5
    if keyboard.right:
        bee.x += 5
    if keyboard.up:
        bee.y -= 5
    if keyboard.down:
        bee.y += 5
    flower_collected = bee.colliderect(flower)
    if flower_collected:
        score += 1
        move()
def move():
    flower.x = random.randint(50, 550)
    flower.y = random.randint(100, 380)
def timer():
    global gameover
    gameover = True
clock.schedule(timer, 10.0)
pgzrun.go()