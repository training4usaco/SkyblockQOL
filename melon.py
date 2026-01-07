from system.lib import minescript
import time
import random

#-141 67.9 -143.3 
#yaw 0.0 pitch -59.0
#400 speed
minescript.execute("warp garden home") 

time.sleep(1)
minescript.player_set_orientation(0,-59.0)
start_pos = minescript.player_position()

minescript.player_press_attack(True)
minescript.player_press_forward(True)
while(True):
    pos = minescript.player_position()
    if((pos[2]-start_pos[2])%6 < 2.75):
        if(pos[2]>=-116.5):
            minescript.player_press_right(True)
            minescript.player_press_left(False)
        else:
            minescript.player_press_right(False)
            minescript.player_press_left(True)
    else:
        if(pos[2]>=-116.5):
            minescript.player_press_right(False)
            minescript.player_press_left(True)
        else:
            minescript.player_press_right(True)
            minescript.player_press_left(False)
    if((pos[0]>142 or pos[0]<-142) and random.randint(0,5) == 0):
        time.sleep(random.uniform(0,1))
    if(pos[2]>-103):
        time.sleep(2+random.uniform(0,1))
        minescript.execute("warp garden home")
        time.sleep(1)