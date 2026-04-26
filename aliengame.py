import pgzrun, random
WIDTH = 600
HEIGHT = 600
image = Actor("alien")
message = ""
def draw():
    screen.fill("black")
    image.draw()
    screen.draw.text(message, (300, 100), fontsize = 20)
def update():
    if keyboard.left:
        image.x -= 5
    if keyboard.right:
        image.x += 5
    if keyboard.up:
        image.y -= 5
    if keyboard.down:
        image.y += 5
def move():
    image.x = random.randint(70, 530)
    image.y = random.randint(100, 500)
def on_mouse_down(pos):
    global message
    if image.collidepoint(pos):
        move()
        message = "Alien Hit"
    else:
        message = "Alien Missed"
pgzrun.go()