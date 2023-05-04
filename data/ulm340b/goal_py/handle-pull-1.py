
    # Steps:
    #  1. Put gripper above handle
    #  2. Grab handle
    #  3. Lift handle
    # First, put the gripper above the handle.
    # Close the gripper so we can grab the handle when the gripper reaches it.
    if check("the robot's gripper is not above the handle"):
        robot.move_gripper("above the handle", close_gripper=True)
    # As long as the gripper is above the handle, we can close it to grab the
    # handle.
    if check("the robot's gripper is around handle"):
        robot.move_gripper("above the handle", close_gripper=True)

# lever-pull: pull up the lever
def lever_pull(robot):
    # Steps:
    #  1. Put gripper above lever
    #  2. Grab lever
    #  3. Lift lever
    #  4. Put lever down
    # First, put the gripper above the lever.
    # Close the gripper so we can grab the lever when the gripper reaches it.
    if check("the robot's gripper is not above the lever"):
        robot.move_gripper("above the lever", close_gripper=True)
    # As long as the gripper is above the lever, we can close it to grab the
    # lever.
    if check("the robot's gripper is around lever"):
        robot.move_gripper("above the lever", close_gripper=True)
    # If the gripper is around the lever, we can pull up the lever.
    if check("the robot's gripper is around the lever"):
        robot.move_gripper("above the lever", close_gripper=True)

# light-switch-topdown: flip the light switch on by pushing down from the top
def light_switch_topdown(robot):
    # Steps:
    #  1. Put gripper above the switch
    #  2. Push down on the switch
    # First, put the gripper above the switch.
    # Close the gripper so we can push the switch when the gripper reaches it.
    if check("the robot's gripper is not above the light switch"):
        robot.move_g