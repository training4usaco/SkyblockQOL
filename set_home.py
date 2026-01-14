from system.lib import minescript
import json

pos = minescript.player_position()
with open("home_pos.json", "w") as f:
    json.dump(pos, f)
minescript.echo(f"Saved to file home location: {pos}")