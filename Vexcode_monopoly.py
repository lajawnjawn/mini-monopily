FWD = Event()
RT = Event()
LT = Event()
myVariable = 0
DICE1 = 0
DICE2 = 0
SPACE_TO_MOVE = 0
CURRENT_SPACE_NUMBER = 0

def play_game():
    global my_event, FWD, RT, LT, myVariable, DICE1, DICE2, SPACE_TO_MOVE, CURRENT_SPACE_NUMBER
    while True:
        roll_dice()
        move()
        complete_task()
        wait(5, MSEC)

def roll_dice():
    global my_event, FWD, RT, LT, myVariable, DICE1, DICE2, SPACE_TO_MOVE, CURRENT_SPACE_NUMBER
    pass

def move():
    global my_event, FWD, RT, LT, myVariable, DICE1, DICE2, SPACE_TO_MOVE, CURRENT_SPACE_NUMBER
    pass

def complete_task():
    global my_event, FWD, RT, LT, myVariable, DICE1, DICE2, SPACE_TO_MOVE, CURRENT_SPACE_NUMBER
    pass

def when_started1():
    global my_event, FWD, RT, LT, myVariable, DICE1, DICE2, SPACE_TO_MOVE, CURRENT_SPACE_NUMBER
    CURRENT_SPACE_NUMBER = 1
    play_game()

def when_started2():
    global my_event, FWD, RT, LT, myVariable, DICE1, DICE2, SPACE_TO_MOVE, CURRENT_SPACE_NUMBER
    pass

def FWD_callback_0():
    global my_event, FWD, RT, LT, myVariable, DICE1, DICE2, SPACE_TO_MOVE, CURRENT_SPACE_NUMBER
    pass

def FWD_callback_1():
    global my_event, FWD, RT, LT, myVariable, DICE1, DICE2, SPACE_TO_MOVE, CURRENT_SPACE_NUMBER
    pass

def LT_callback_0():
    global my_event, FWD, RT, LT, myVariable, DICE1, DICE2, SPACE_TO_MOVE, CURRENT_SPACE_NUMBER
    pass

def LT_callback_1():
    global my_event, FWD, RT, LT, myVariable, DICE1, DICE2, SPACE_TO_MOVE, CURRENT_SPACE_NUMBER
    pass

def RT_callback_0():
    global my_event, FWD, RT, LT, myVariable, DICE1, DICE2, SPACE_TO_MOVE, CURRENT_SPACE_NUMBER
    pass

def RT_callback_1():
    global my_event, FWD, RT, LT, myVariable, DICE1, DICE2, SPACE_TO_MOVE, CURRENT_SPACE_NUMBER
    pass

# system event handlers
FWD(FWD_callback_0)
FWD(FWD_callback_1)
LT(LT_callback_0)
LT(LT_callback_1)
RT(RT_callback_0)
RT(RT_callback_1)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

ws2 = Thread( when_started2 )
when_started1()
