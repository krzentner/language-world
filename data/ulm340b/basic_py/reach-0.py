
    if check("the robot's gripper is not at the goal"):
        robot.place("gripper at goal")

# turn-switch-ccw: turn the switch ccw
def turn_switch_ccw(robot):
    if check("the robot's gripper is not vertically aligned with the switch handle"):
        robot.put("gripper above switch handle")
    if check("the robot's gripper is not near switch handle"):
        robot.grab("switch handle")
    if check("the robot's gripper is near the switch handle"):
        robot.turn("switch ccw")

# turn-switch-cw: turn the switch cw
def turn_switch_cw(robot):
    if check("the robot's gripper is not vertically aligned with the switch handle"):
        robot.put("gripper above switch handle")
    if check("the robot's gripper is not near switch handle"):
        robot.grab("switch handle")
    if check("the robot's gripper is near the switch handle"):
        robot.turn("switch cw")

# pick: pick up the block
def pick(robot):
    if check("the robot's gripper is not above the block and the robot's gripper is not forward aligned with the block"):
        robot.place("gripper above block")
    if check("the robot's gripper is not vertically aligned with block"):
        robot.put("gripper around block")
    if check("the robot's gripper is vertically aligned with block"):
        robot.grab("block")

# place: place the block on the table
def place(robot):
    if check("the robot's gripper is not around block and the robot's gripper is not above the table"):
        robot.grab("block")
    if check("the robot's gripper is around block and the robot's gripper is not above table"):
        robot.put("gripper above table")
    if check("the robot's gripper is around block and the robot's gripper is above table"):
        robot.drop("block onto table")

# grasp: grasp the item on the table
def grasp(robot):
    if check("the robot's gripper is not around item and the robot's gripper is not above item"):
        robot.grab("item")
    if check("the robot's gripper is around item and the robot's grip