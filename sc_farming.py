import os
import time
import random

import init
from system.lib import minescript
import json


lane_start_position = minescript.player_position()
if os.path.exists(init.macro_info_file_path):
    with open(init.macro_info_file_path, "r") as f:
        data = json.load(f)
        FARM_START_POSITION = data["farm_start"]
if FARM_START_POSITION is None:
    FARM_START_POSITION = minescript.player_position()
if data is None:
    data = {}

minescript.echo(f"Loaded home location: {FARM_START_POSITION}")

FARMING_X_OFFSET = random.randint(1, 15) / 10
FARMING_Z_OFFSET = random.randint(1, 15) / 10

offset1 = random.randint(1, 8) / 10
offset2 = random.randint(1, 8) / 10

def random_stop(coeff = 1):
    global data
    if (random.randint(1, 7 * coeff) <= 3):
        pause_time = random.randint(1, 6) / 10

        data['pause_time'] = pause_time
        with open(init.macro_info_file_path, "w") as f:
            json.dump(data, f, indent = 4)

        time.sleep(pause_time)
        data['pause_time'] = 0.0
        with open(init.macro_info_file_path, "w") as f:
            json.dump(data, f, indent = 4)
    elif (random.randint(1, 50 * coeff) == 1):
        pause_time = random.randint(100, 150) / 10

        data['pause_time'] = pause_time
        with open(init.macro_info_file_path, "w") as f:
            json.dump(data, f, indent=4)

        time.sleep(pause_time)
        data['pause_time'] = 0.0
        with open(init.macro_info_file_path, "w") as f:
            json.dump(data, f, indent = 4)


def random_order_funcs(funcs: list['func']):
    coeff = 1
    random.shuffle(funcs)
    for func in funcs:
        func(coeff)
        coeff *= 3

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
    return ((minescript.player_position()[0] < (FARM_START_POSITION[0] + data['farm_width'] - FARMING_X_OFFSET))
    or (minescript.player_position()[2] < (FARM_START_POSITION[2] + data['farm_length'] - FARMING_Z_OFFSET)))

data['active'] = True
with open(init.macro_info_file_path, "w") as f:
    json.dump(data, f, indent = 4)

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

