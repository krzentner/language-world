
    if check("the robot's gripper is not above box lid"):
        robot.move("gripper above box lid")
    if check("the robot's gripper is above box lid and the robot's gripper is open"):
        robot.drop("gripper around box lid")
    if check("the robot's gripper is around box lid"):
        robot.close("gripper")
    if check("the robot's gripper is above box and box lid is closed"):
        robot.place("box lid on box")

# box-open: grab the lid of the box and lift it off the box
def box_open(robot):
    if check("the robot's gripper is not above the box lid"):
        robot.move("gripper above box lid")
    if check("the robot's gripper is above the box lid"):
        robot.grab("box lid")
    if check("the robot's gripper is around the box lid and the robot's gripper is closed"):
        robot.lift("box lid")

# pick-place-wall: pick up the puck and hold it at the target location
def pick_place_wall(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# stack: pick up the cylinder and place it on top of the cube
def stack(robot):
    if check("the robot's gripper is not above cylinder"):
        robot.place("gripper above cylinder")
    if check("the robot's gripper is above cylinder and the robot's gripper is open"):
        robot.drop("gripper around cylinder")
    if check("the robot's gripper is around cylinder"):
        robot.close("gripper")
    if check("the robot's gripper is above cube and cylinder is closed"):
        robot.place("cylinder on cube")

# peg-unstack: grab the top cylinder and