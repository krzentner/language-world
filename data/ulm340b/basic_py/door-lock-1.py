
    if check("the robot's gripper is not forward aligned with dial"):
        robot.grab("door dial")
    if check("the robot's gripper is forward aligned with dial"):
        robot.turn("knob left and right")

# pick-place-wall: pick up the puck and hold it at the target location
def pick_place_wall(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not open"):
        robot.open("gripper")
    if check("the robot's gripper is open and above puck"):
        robot.put("gripper around puck")
    if check("the robot's gripper is closed and above puck"):
        robot.place("puck at goal")

# dial-turn: grab the dial and turn it from side to side
def dial_turn(robot):
    if check("the robot's gripper is not forward aligned with dial"):
        robot.grab("dial")
    if check("the robot's gripper is forward aligned with dial"):
        robot.turn("dial left and right")

# lever-pull: pull the lever forward
def lever_pull(robot):
    if check("the robot's gripper is not forward aligned with lever"):
        robot.grab("lever")
    if check("the robot's gripper is forward aligned with lever"):
        robot.pull("lever")

# lift: pick up the block and hold it at the target location
def lift(robot):
    if check("the robot's gripper is not above the block"):
        robot.put("the gripper above the block")
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.drop("gripper around block")
    if check("the robot's gripper is near block and the robot's gripper is open"):
        robot.close("gripper around block")
    if check("the robot's gripper is above the block and the robot's gripper is closed"):
        robot.lift("block off table")

# drawer-pick-place: pick up the drawer and hold it at the target location
def drawer_pick_place(robot):
    if check("the robot's gripper is not above drawer and the robot's gripper is open"):
        robot.open("gripper")
    if check("the robot's