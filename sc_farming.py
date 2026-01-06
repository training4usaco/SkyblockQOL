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

def random_stop(coeff = 1):
    if (random.randint(1, 7 * coeff) <= 3):
        time.sleep(random.randint(1, 6) / 10)
    elif (random.randint(1, 50 * coeff) == 1):
        time.sleep(random.randint(100, 150) / 10)

def random_order_funcs(funcs: list['func']):
    coeff = 1
    random.shuffle(funcs)
    for func in funcs:
        func(coeff)
        coeff *= 5

def start_left(coeff = 1):
    random_stop(coeff)
    minescript.player_press_left(True)

def stop_left(coeff = 1):
    random_stop(coeff)
    minescript.player_press_left(False)

def start_back(coeff = 1):
    random_stop(coeff)
    minescript.player_press_backward(True)

def stop_back(coeff = 1):
    random_stop(coeff)
    minescript.player_press_backward(False)

def start_attack(coeff = 1):
    random_stop(coeff)
    minescript.player_press_attack(True)

def stop_attack(_coeff = 1):
    minescript.player_press_attack(False)

def should_continue():
    return ((minescript.player_position()[0] < (FARM_START_POSITION[0] + 186 - FARMING_X_OFFSET))
    or (minescript.player_position()[2] < (FARM_START_POSITION[2] + 91 - FARMING_Z_OFFSET)))

while True:
    lane_start_position = minescript.player_position()
    random_order_funcs([start_attack, start_left])

    while should_continue():
        while should_continue() and (minescript.player_position()[0] < (3 + lane_start_position[0] - random.randint(3, 8) / 10)):
            random_stop(10000)
            time.sleep(0.001)
        if not should_continue():
            break

        random_order_funcs([stop_left, start_back])

        lane_start_position = minescript.player_position()
        while should_continue() and (minescript.player_position()[0] < (3 + lane_start_position[0] - random.randint(3, 8) / 10)):
            random_stop(10000)
            time.sleep(0.001)
        if not should_continue():
            break

        random_order_funcs([start_left, stop_back])
        lane_start_position = minescript.player_position()

    random_order_funcs([stop_left, stop_back, stop_attack])

    minescript.execute('warp garden')
    time.sleep(random.randint(2, 8) / 10)

