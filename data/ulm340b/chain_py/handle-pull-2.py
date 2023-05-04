
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Pull handle up
    # Put the robot's gripper above the handle so we can grab it.
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above handle")
    # As long as the gripper is lined up with the handle and open, just close it
    # around the handle to grab it.
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is open"):
        robot.put("gripper around handle")
    # Since we grabbed the handle, we can just pull it up.
    if check("the robot's gripper is around the handle"):
        robot.pull("the handle up")

# handle-turn-cw: turn the handle clockwise
def handle_turn_cw(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Turn handle clockwise
    # Put the robot's gripper above the handle so we can grab it.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    # As long as the gripper is lined up with the handle and open, just close it
    # around the handle to grab it.
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is open"):
        robot.put("gripper around handle")
    # Now that we've grabbed the handle, we can just turn it clockwise
    if check("the robot's gripper is around the handle"):
        robot.turn("the handle clockwise")

# handle-turn-ccw: turn the handle counterclockwise
def handle_turn_ccw(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Turn handle counterclockwise
    # Put the robot's gripper above the handle so we can grab it.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("g