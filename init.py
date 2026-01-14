import os
import threading
import time

from system.lib import minescript
import sys
import json

script_dir = os.path.dirname(os.path.abspath(__file__))
macro_info_file_path = os.path.join(script_dir, "macro_info.json")

farm_dimensions = {
    'mf': (90, 186),
    'default': (90, 186)
}

if __name__ == "__main__":
    pos = minescript.player_position()
    orientation = minescript.player_orientation()
    farm_type = sys.argv[1] if (len(sys.argv) > 1 and sys.argv[1] in farm_dimensions) else 'default'
    with open(macro_info_file_path, "w") as f:
        data = {
            "farm_start": pos,
            "orientation": orientation,
            "farm_width": farm_dimensions[farm_type][0],
            "farm_length": farm_dimensions[farm_type][1],
        }
        json.dump(data, f, indent=4)
    minescript.echo(f"Saved home location: {pos}")
    macro_thread = threading.Thread(target=minescript.execute('\macro_checker'))
    macro_thread.start()
    macro_thread.join()
