

The function should complete the task in a few lines of code.

- - -

Add `hammer` below this line to complete the task.
"""

button_press_topdown = lambda r: \
    r.put("gripper above button") if check("the robot's gripper is not vertically aligned with button") \
    else r.push("down on button")
door_open = lambda r: \
    r.put("gripper above door handle") if check("the robot's gripper is not almost vertically aligned with door handle") \
    else r.put("gripper around door handle") if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open") \
    else r.pull("door open") if check("the robot's gripper is vertically aligned with the door handle") \
    else r
reach = lambda r: \
    r.reach("to goal") if check("the robot's gripper is not near reach target") \
    else r
drawer_close = lambda r: \
    r.grab("drawer handle") if check("the robot's gripper is not near the drawer handle") \
    else r.push("drawer closed") if check("the robot's gripper is forward aligned with drawer handle") \
    else r
drawer_open = lambda r: \
    r.put("gripper above drawer handle") if check("the robot's gripper is not vertically aligned with drawer handle") \
    else r.put("gripper around drawer handle") if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle") \
    else r.pull("away from drawer") if check("the robot's gripper is around drawer handle") \
    else r
peg_insert_side = lambda r: \
    r.put("gripper above peg") if check("the robot's gripper is not vertically aligned with the peg") \
    else r.grab("peg") if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper") \
    else r.align("peg to hole") if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole") \
    else r.insert("peg into hole") if check("peg is horizontally aligned with hole") \
    else r
pick_place = lambda r: \
    r.place("gripper