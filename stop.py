import json

import init
from system.lib import minescript

with open(init.macro_info_file_path, "r") as f:
    data = json.load(f)
data['active'] = False
with open(init.macro_info_file_path, "w") as f:
    json.dump(data, f, indent = 4)
minescript.execute("\suspend 1")
minescript.player_press_attack(False)
minescript.player_press_left(False)
minescript.player_press_right(False)
minescript.player_press_backward(False)
minescript.player_press_forward(False)
minescript.execute("\killjob -1")
