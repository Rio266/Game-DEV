import pgzrun, random
WIDTH = 800
HEIGHT = 480
non_recycle = ["book", "lamp", "bottle", "battery", "pen", "laptop"]
total_levels = 6
starting_speed = 10
game_over = False
game_complete = False
current_level = 1

items = []
animations = []
def draw():
    global items, current_level, game_over, game_complete
    screen.clear()
    screen.blit("nature", (0, 0))
    if game_over:
        screen.draw.text("Game Over!", center = (400, 240), color = "orange", fontsize = 30)
    elif game_complete:
        screen.draw.text("Well Done! You have completed all the rounds.", center = (400, 240), color = "blue", fontsize = 30)
    else:
        for i in items:
            i.draw()
def update():
    global items
    if len(items) == 0:
        items = makeitems(current_level)
def makeitems(extraitems):
    itemstocreate = optiontocreate(extraitems)
    newitems = createitems(itemstocreate)
    layout_items(newitems)
    animate_items(newitems)
    return newitems
def optiontocreate(extraitems):
    itemstocreate = ["paper"]
    for i in range(extraitems):
        option = random.choice(non_recycle)
        itemstocreate.append(option)
    return itemstocreate
def createitems(itemstocreate):
    newitems = []
    for i in itemstocreate:
        item = Actor(i + "img")
        newitems.append(item)
    return newitems
def layout_items(itemstolayout):
    gaps = len(itemstolayout) + 1
    gapsize = WIDTH/gaps
    random.shuffle(itemstolayout)
    for i, j in enumerate(itemstolayout):
        newx = (i + 1) * gapsize
        j.x = newx
def animate_items(itemstoanimate):
    global animations
    for i in itemstoanimate:
        duration = starting_speed - current_level
        i.anchor = ("center", "bottom")
        animation = animate(i, duration = duration, on_finished = handle_gameover, y = HEIGHT)
        animations.append(animation)
def handle_gameover():
    global game_over
    game_over = True
def on_mouse_down(pos):
    global items, current_level
    for i in items:
        if i.collidepoint(pos):
            if "paper" in i.image:
                handle_gamecomplete()
            else:
                handle_gameover()
def handle_gamecomplete():
    global current_level, items, animations, game_complete
    stop_animations(animations)
    if current_level == total_levels:
        game_complete = True
    else:
        current_level += 1
        items = []
        animations = []
def stop_animations(animationstostop):
    for i in animationstostop:
        if i.running:
            i.stop()
pgzrun.go()