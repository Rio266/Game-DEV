import pgzrun, random
WIDTH = 600
HEIGHT = 480

satellites = []
lines = []
next_satellite = 0

start_time = 0
end_time = 0
total_time = 0

total_satellites = 8

def create():
    for i in range(total_satellites):
        satellite_character = Actor("satellitecharacter")
        satellite_character.pos = (random.randint(40, 560), random.randint(40, 440))
        satellites.append(satellite_character)
def draw():
    screen.blit("satellitebackground", (0, 0))
    n = 1
    for i in satellites:
        i.draw()
        screen.draw.text(str(n), (i.pos[0], i.pos[1] + 20))
        n += 1
    for i in lines:
        screen.draw.line(i[0], i[1], "orange")
def update():
    pass
def on_mouse_down(pos):
    global next_satellite, lines
    if next_satellite < total_satellites:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append((satellites[next_satellite - 1].pos, satellites[next_satellite].pos))
        else:
            lines = []
            next_satellite = 0
create()
pgzrun.go()