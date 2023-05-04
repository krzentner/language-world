
    # Steps:
    #  1. Put gripper above the handle
    #  2. Drop gripper around the handle
    #  3. Pull up the handle
    # If the gripper is not above the handle, move it above the handle
    if check("the robot's gripper is not above the handle"):
        robot.place("gripper above handle")
    # If the gripper is above the handle, put the gripper around the handle.
    # We have to check if the gripper is open so that we can do this again
    # if it fails
    if check("the robot's gripper is above the handle and the robot's gripper is open"):
        robot.drop("gripper around handle")
    # If the gripper is around the handle, pull up the handle
    if check("the robot's gripper is around the handle"):
        robot.pull("the handle up")

# light-switch-flip-bottomup: flip the light switch up
def light_switch_flip_bottomup(robot):
    # Steps:
    #  1. Put gripper above light switch
    #  2. Push down on the light switch
    # First, put the gripper above the light switch.
    if check("the robot's gripper is not vertically aligned with light switch"):
        robot.put("gripper above light switch")
    # As long as the gripper is lined up, push the light switch.
    if check("the robot's gripper is vertically aligned with light switch"):
        robot.push("down on light switch")

# light-switch-flip-topdown: flip the light switch up
def light_switch_flip_topdown(robot):
    # Steps:
    #  1. Put gripper above light switch
    #  2. Push down on the light switch
    # First, put the gripper above the light switch.
    if check("the robot's gripper is not vertically aligned with light switch"):
        robot.put("gripper above light switch")
    # As long as the gripper is lined up, push the light switch.
    if check("the robot's gripper is vertically aligned with light switch"):
        robot.push("down on light switch")

# bottle-cap-turn-cw: turn the bottle cap clockwise
def bottle_cap_turn