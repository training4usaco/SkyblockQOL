import time
import random

from system.lib import minescript
import sys

lane_start_position = minescript.player_position()
FARM_START_POSITION = minescript.player_position()



FARMING_X_OFFSET = random.randint(1, 15) / 10
FARMING_Z_OFFSET = random.randint(1, 15) / 10

offset1 = random.randint(1, 8) / 10
offset2 = random.randint(1, 8) / 10



def stop_left():
    if (random.randint(1, 5) == 1):
        time.sleep(random.randint(1, 4) / 10)
    elif (random.randint(1, 100) == 1):
        time.sleep(random.randint(50, 150) / 10)
    else:
        time.sleep(random.randint(1, 5) / 50)
    minescript.player_press_left(False)

def start_back():
    if (random.randint(1, 5) == 1):
        time.sleep(random.randint(1, 5) / 10)
    elif (random.randint(1, 100) == 1):
        time.sleep(random.randint(50, 150) / 10)
    else:
        time.sleep(random.randint(1, 3) / 50)
    minescript.player_press_backward(True)

def start_left():
    if (random.randint(1, 5) == 1):
        time.sleep(random.randint(1, 4) / 10)
    elif (random.randint(1, 100) == 1):
        time.sleep(random.randint(50, 150) / 10)
    else:
        time.sleep(random.randint(1, 5) / 50)
    minescript.player_press_left(True)

def stop_back():
    if (random.randint(1, 5) == 1):
        time.sleep(random.randint(1, 5) / 10)
    elif (random.randint(1, 100) == 1):
        time.sleep(random.randint(50, 150) / 10)
    else:
        time.sleep(random.randint(1, 3) / 50)
    minescript.player_press_backward(False)

def should_continue():
    return ((minescript.player_position()[0] < (FARM_START_POSITION[0] + 90 - FARMING_X_OFFSET))
    or (minescript.player_position()[2] < (FARM_START_POSITION[2] + 90 - FARMING_Z_OFFSET)))

while True:
    lane_start_position = minescript.player_position()
    if(random.randint(1, 5) == 1):
        minescript.player_press_attack(True)
        time.sleep(random.randint(1, 5) / 50)
        minescript.player_press_left(True)
    else:
        minescript.player_press_left(True)
        time.sleep(random.randint(1, 5) / 50)
        minescript.player_press_attack(True)


    while should_continue():
        while should_continue() and (minescript.player_position()[0] < 3 + lane_start_position[0] - random.randint(3, 8) / 10):
            time.sleep(0.001)
        if not should_continue():
            break

        if (random.randint(1, 3) == 1):
            stop_left()
            start_back()
        else:
            start_back()
            stop_left()

        lane_start_position = minescript.player_position()


        while minescript.player_position()[0] < 3 + lane_start_position[0] - random.randint(3, 8) / 10:
            time.sleep(0.001)
        if not should_continue():
            break

        if (random.randint(1, 3) == 1):
            start_left()
            stop_back()
        else:
            stop_back()
            start_left()

        lane_start_position = minescript.player_position()


    minescript.player_press_left(False)
    time.sleep(random.randint(3, 8) / 50)
    minescript.player_press_backward(False)

    time.sleep(random.randint(3, 8) / 10)
    minescript.player_press_attack(False)

    minescript.execute('warp garden')
    time.sleep(random.randint(2, 8) / 10)

