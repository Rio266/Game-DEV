import pgzrun
import random
WIDTH = 600
HEIGHT = 600

def draw():
    w = 160
    h = 100
    for i in range(10):
        rec = Rect((0, 0), (w, h))
        rec.center = (WIDTH/2, HEIGHT/2)
        screen.draw.rect(rec, "blue")
        w += 20
        h += 20
    radius = 100
    for i in range(8):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        screen.draw.filled_circle((WIDTH/2, HEIGHT/2), radius, (r, g, b))
        radius -= 20
    screen.draw.text("Hello!", (WIDTH/2 - 30, HEIGHT/2 - 250), color = "white", fontsize = 30)
pgzrun.go()