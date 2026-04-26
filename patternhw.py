import pgzrun
WIDTH = 600
HEIGHT = 600
def draw():
    w = 300
    h = 100
    r = 150
    for i in range(20):
        rec = Rect((0, 0), (w, h))
        rec.center = (WIDTH/2, HEIGHT/2)
        screen.draw.rect(rec, "blue")
        screen.draw.circle((WIDTH/2, HEIGHT/2), r, "orange")
        w -= 20
        h -= 6.6
        r -= 10
pgzrun.go()