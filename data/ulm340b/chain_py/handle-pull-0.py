
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Pull the handle all the way up
    # First, put the gripper above the handle.
    if check("the robot's gripper is not above handle"):
        robot.place("gripper above handle")
    # Once the gripper is above the handle, we can drop it around the handle.
    if check("the robot's gripper is above handle and the robot's gripper is open"):
        robot.put("gripper around handle")
    # If the gripper is around the handle, we can pull it all the way up.
    if check("the robot's gripper is around handle"):
        robot.pull("up on handle")

# handle-side-open: pull the handle out to the side
def handle_side_open(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Pull the handle all the way out to the side
    # First, put the gripper above the handle.
    if check("the robot's gripper is not above handle"):
        robot.place("gripper above handle")
    # Once the gripper is above the handle, we can drop it around the handle.
    if check("the robot's gripper is above handle and the robot's gripper is open"):
        robot.put("gripper around handle")
    # If the gripper is around the handle, we can pull it all the way to the
    # side.
    if check("the robot's gripper is around handle"):
        robot.pull("out on handle")

# handle-turn: twist the handle
def handle_turn(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Turn the handle clockwise
    # First, put the gripper above the handle.
    if check("the robot's gripper is not above handle"):
        robot.place("gripper above handle")
    # Once the gripper is above the handle, we can drop it around the handle.
    if check("the robot's gripper is above handle and