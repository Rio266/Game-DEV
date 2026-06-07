import pgzrun
WIDTH = 600
HEIGHT = 450
marquee_box = Rect(0, 0, 600, 50)
question_box = Rect(0, 110, 410, 100)
answer1_box = Rect(0, 220, 200, 100)
answer2_box = Rect(210, 220, 200, 100)
answer3_box = Rect(0, 330, 200, 100)
answer4_box = Rect(210, 330, 200, 100)
timer_box = Rect(420, 110, 150, 100)
skip_box = Rect(420, 220, 150, 210)
answer_boxes = [answer1_box, answer2_box, answer3_box, answer4_box]
score = 0
time_left  = 10
question_file = "questions.txt"
marquee_text = ""
is_gameover = False
questions = []
count = 0
index = 0
def readquestion():
    global count, questions
    file = open(question_file, "r")
    for i in file:
        questions.append(i)
        count += 1
    file.close()
def readnextquestion():
    global index
    index += 1
    return questions.pop(0).split(",")
readquestion()
question = readnextquestion()
def draw():
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(marquee_box, "black")
    screen.draw.filled_rect(question_box, "blue")
    screen.draw.filled_rect(timer_box, "orange")
    screen.draw.filled_rect(skip_box, "blue")
    for i in answer_boxes:
        screen.draw.filled_rect(i, "orange")
    marquee_text = f"Welcome to Quizmaster! You are on Question {index}/{count}"
    screen.draw.textbox(marquee_text, marquee_box, color = "orange")
    screen.draw.textbox(str(time_left), timer_box, color = "blue")
    screen.draw.textbox("Skip", skip_box, color = "orange")
    screen.draw.textbox(question[0].strip(), question_box, color = "orange")
    j = 1
    for i in answer_boxes:
        screen.draw.textbox(question[j].strip(), i, color = "blue")
        j += 1
def update():
    move_marquee()
def move_marquee():
    marquee_box.x -= 2
    if marquee_box.right < 0:
        marquee_box.left = WIDTH
def on_mouse_down(pos):
    j = 1
    for i in answer_boxes:
        if i.collidepoint(pos):
            if j is int(question[5]):
                correct_answer()
            else:
                game_over()
        j += 1
    if skip_box.collidepoint(pos):
        skip_question()
def correct_answer():
    global score, question, questions, time_left
    score += 1
    if questions:
        question = readnextquestion()
        time_left = 10
    else:
        game_over()
def game_over():
    global question, time_left,  is_gameover
    message = f"The game is over! Well done! \nYour score is {score}/{count}"
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0
    is_gameover = True
def skip_question():
    global question, time_left
    if questions and not is_gameover:
        question = readnextquestion()
        time_left = 10
    else:
        game_over()
def timer():
    global time_left
    if time_left:
        time_left -= 1
    else:
        game_over()
clock.schedule_interval(timer, 1)
pgzrun.go()