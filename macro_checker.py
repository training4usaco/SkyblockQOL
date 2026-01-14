import os
import sys
import time
import random

import init
from system.lib import minescript
import json

def macro_check_alert():
    script = 'activate application "Prism Launcher"'
    os.system(f"osascript -e '{script}'")
    minescript.echo("MACRO CHECK ALERT!!!!!!!!!")
    time.sleep(random.randint(15, 25) / 10)
    minescript.execute("\stop")
    sys.exit(0)

def near_position(position1, position2):
    return abs(position1[0] - position2[0]) + abs(position1[1] - position2[1]) + abs(position1[2] - position2[2]) < 5

def start_macro_checker():
    if os.path.exists(init.macro_info_file_path):
        with open(init.macro_info_file_path, "r") as f:
            data = json.load(f)
            farm_start_pos = data["farm_start"]
            orientation = data["orientation"]

    if farm_start_pos is None or orientation is None:
        minescript.echo("Remember to run \init! This script won't do anything until you do :)")
    else:
        farm_end_pos = (farm_start_pos[0] + data["farm_width"], farm_start_pos[1], farm_start_pos[2] + data["farm_length"])

        prev_position = minescript.player_position()
        while(True):
            time.sleep(1)
            current_position = minescript.player_position()
            current_orientation = minescript.player_orientation()

            if abs(current_orientation[0] - orientation[0]) > 0.1 or abs(current_orientation[1] - orientation[1]) > 0.1:
                minescript.echo('camera changed orientation')
                macro_check_alert()

            if abs(current_position[0] - prev_position[0]) < 0.01 and abs(current_position[2] - prev_position[2]) < 0.01:
                with open(init.macro_info_file_path, "r") as f:
                    data = json.load(f)
                    if "pause_time" not in data or data["pause_time"] == 0.0:
                        minescript.echo('stayed in place for too long')
                        macro_check_alert()
                    else:
                        time.sleep(data["pause_time"] - 1)

            if(not (near_position(prev_position, farm_end_pos) and near_position(current_position, farm_start_pos)) and
                    (abs(current_position[0] - prev_position[0]) > 20 or abs(current_position[1] - prev_position[1]) > 20 or abs(current_position[2] - prev_position[2]) > 20)):
                minescript.echo("teleported a large distance (that wasn't warping to start of farm)")
                macro_check_alert()

            # This doesn't really work for wart...
            if (abs(current_position[1] - farm_start_pos[1]) > 1 or
                    not(min(farm_start_pos[0], farm_end_pos[0]) <= current_position[0] <= max(farm_start_pos[0], farm_end_pos[0])) or
                    not(min(farm_start_pos[2], farm_end_pos[2]) <= current_position[2] <= max(farm_start_pos[0], farm_end_pos[2]))):
                minescript.echo('moved outside the farm')
                macro_check_alert()

            prev_position = current_position

minescript.echo("waiting for macro to start")
while(True):
    with open(init.macro_info_file_path, "r") as f:
        data = json.load(f)
        if 'active' in data and data['active']:
            break
    time.sleep(10)


minescript.echo("started macro checking. you're in good hands :)")
start_macro_checker()

