from system.lib import minescript
import time
import random

#x:142.7 y:5  z:49,7
#yaw 0.0 pitch 3.8
#93 speed

minescript.execute("warp garden home")

time.sleep(1)
start_pos = minescript.player_position()
minescript.player_press_attack(True)

while (True):
    pos = minescript.player_position()
    if((start_pos[1]-pos[1])%4<1.75):
        minescript.player_press_right(True)
        minescript.player_press_left(False)
    else:
        minescript.player_press_left(True)
        minescript.player_press_right(False)
    if(pos[2]<49.6):
        minescript.player_press_forward(True)
    else:
        minescript.player_press_forward(False)
    if((pos[0]>142 or pos[0]<-238) and random.randint(0,5) == 0):
        time.sleep(random.uniform(0,1))
    if(pos[0]<-238 and pos[1] < 68):
        time.sleep(2+random.uniform(0,1))
        minescript.execute("warp garden home")
        time.sleep(1)
