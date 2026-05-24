import pgzrun
WIDTH = 600
HEIGHT = 450
marquee_box = Rect(0, 0, 600, 100)
question_box = Rect(0, 110, 410, 100)
answer1_box = Rect(0, 220, 200, 100)
answer2_box = Rect(210, 220, 200, 100)
answer3_box = Rect(0, 330, 200, 100)
answer4_box = Rect(210, 330, 200, 100)
timer_box = Rect(420, 110, 150, 100)
skip_box = Rect(420, 220, 150, 210)
answer_boxes = [answer1_box, answer2_box, answer3_box, answer4_box]
def draw():
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(marquee_box, "black")
    screen.draw.filled_rect(question_box, "blue")
    screen.draw.filled_rect(timer_box, "orange")
    screen.draw.filled_rect(skip_box, "blue")
    for i in answer_boxes:
        screen.draw.filled_rect(i, "orange")
pgzrun.go()