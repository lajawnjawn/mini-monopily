screen_precision = 0
console_precision = 0
FWD = Event()
RT = Event()
LT = Event()
myVariable = 0
DICE1 = 0
DICE2 = 0
SPACE_TO_MOVE = 0
CURRENT_SPACE_NUMBER = 0

def play_game():
    global my_event, FWD, RT, LT, myVariable, DICE1, DICE2, SPACE_TO_MOVE, CURRENT_SPACE_NUMBER, screen_precision, console_precision
    while True:
        roll_dice()
        move()
        complete_task()
        brain.screen.set_cursor(1, 1)
        wait(1, SECONDS)
        wait(5, MSEC)

def complete_task():
    global my_event, FWD, RT, LT, myVariable, DICE1, DICE2, SPACE_TO_MOVE, CURRENT_SPACE_NUMBER, screen_precision, console_precision
    brain.screen.print(str("Land on space") + str(CURRENT_SPACE_NUMBER))
    brain.screen.next_row()
    wait(1, SECONDS)
    if CURRENT_SPACE_NUMBER == 1:
        # Space = Go
        for repeat_count in range(10):
            LT.broadcast_and_wait()
            wait(5, MSEC)
    elif CURRENT_SPACE_NUMBER == 4:
        # Space = Jail
        wait(3, SECONDS)
    elif CURRENT_SPACE_NUMBER == 7:
        # Space = Free Parking
        pass
    elif CURRENT_SPACE_NUMBER == 10:
        # Space = Go to Jail
        pass
    else:
        # Space = Blue 1 or 2, Green 1 or 2, Yellow 1 or 2, Red 1 or 2
        RT.broadcast_and_wait()
        FWD.broadcast_and_wait()
        for repeat_count2 in range(2):
            LT.broadcast_and_wait()
            wait(5, MSEC)
        FWD.broadcast_and_wait()
        RT.broadcast_and_wait()

def roll_dice():
    global my_event, FWD, RT, LT, myVariable, DICE1, DICE2, SPACE_TO_MOVE, CURRENT_SPACE_NUMBER, screen_precision, console_precision
    DICE1 = int(round(urandom.uniform(1, 5), 2))
    brain.screen.print(str("Rolled a:") + str(DICE1))
    brain.screen.next_row()
    DICE2 = int(round(urandom.uniform(1, 5), 2))
    brain.screen.print(str("Rolled a:") + str(DICE2))
    brain.screen.next_row()
    SPACE_TO_MOVE = DICE1 + DICE2

def move():
    global my_event, FWD, RT, LT, myVariable, DICE1, DICE2, SPACE_TO_MOVE, CURRENT_SPACE_NUMBER, screen_precision, console_precision
    brain.screen.print(str("Moving") + str(str(SPACE_TO_MOVE) + str("Spaces!")))
    brain.screen.next_row()
    for repeat_count3 in range(int(SPACE_TO_MOVE)):
        FWD.broadcast_and_wait()
        CURRENT_SPACE_NUMBER = CURRENT_SPACE_NUMBER + 1
        if CURRENT_SPACE_NUMBER > 12:
            CURRENT_SPACE_NUMBER = 1
        if CURRENT_SPACE_NUMBER == 1:
            RT.broadcast_and_wait()
        if CURRENT_SPACE_NUMBER == 4:
            RT.broadcast_and_wait()
        if CURRENT_SPACE_NUMBER == 7:
            RT.broadcast_and_wait()
        if CURRENT_SPACE_NUMBER == 10:
            RT.broadcast_and_wait()
        wait(5, MSEC)

def when_started1():
    global my_event, FWD, RT, LT, myVariable, DICE1, DICE2, SPACE_TO_MOVE, CURRENT_SPACE_NUMBER, screen_precision, console_precision
    CURRENT_SPACE_NUMBER = 1
    play_game()

def FWD_callback_0():
    global my_event, FWD, RT, LT, myVariable, DICE1, DICE2, SPACE_TO_MOVE, CURRENT_SPACE_NUMBER, screen_precision, console_precision
    motor_5.spin_for(FORWARD, 400, DEGREES)

def FWD_callback_1():
    global my_event, FWD, RT, LT, myVariable, DICE1, DICE2, SPACE_TO_MOVE, CURRENT_SPACE_NUMBER, screen_precision, console_precision
    motor_1.spin_for(FORWARD, 400, DEGREES)

def LT_callback_0():
    global my_event, FWD, RT, LT, myVariable, DICE1, DICE2, SPACE_TO_MOVE, CURRENT_SPACE_NUMBER, screen_precision, console_precision
    motor_5.spin_for(FORWARD, 200, DEGREES)

def LT_callback_1():
    global my_event, FWD, RT, LT, myVariable, DICE1, DICE2, SPACE_TO_MOVE, CURRENT_SPACE_NUMBER, screen_precision, console_precision
    motor_1.spin_for(REVERSE, 200, DEGREES)

def RT_callback_0():
    global my_event, FWD, RT, LT, myVariable, DICE1, DICE2, SPACE_TO_MOVE, CURRENT_SPACE_NUMBER, screen_precision, console_precision
    motor_5.spin_for(REVERSE, 215, DEGREES)

def RT_callback_1():
    global my_event, FWD, RT, LT, myVariable, DICE1, DICE2, SPACE_TO_MOVE, CURRENT_SPACE_NUMBER, screen_precision, console_precision
    motor_1.spin_for(FORWARD, 215, DEGREES)

# system event handlers
FWD(FWD_callback_0)
FWD(FWD_callback_1)
LT(LT_callback_0)
LT(LT_callback_1)
RT(RT_callback_0)
RT(RT_callback_1)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

when_started1()
