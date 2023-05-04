
    # Steps:
    #  1. Put gripper above the mug
    #  2. Drop gripper around the mug
    #  3. Push the mug to the target location
    # We need to put the gripper above the mug before we can grab it, because of
    # the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with mug"):
        robot.move_gripper("vertically aligned with the mug")
    # Once the gripper is lined up above the mug, we should be able to grab it
    # by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with mug and the robot's gripper is not around mug"):
        robot.move_gripper("around the mug", close_gripper=True)
    # Once the gripper is around the mug, we can just push the mug to the target
    # location.
    if check("the robot's gripper is around the mug"):
        robot.move_gripper("near the target location")

# turn-on: turn on the switch
def turn_on(robot):
    # Steps:
    #  1. Put gripper above switch handle
    #  2. Flip the switch handle upward
    # First, put the gripper above the switch handle.
    if check("the robot's gripper is not above switch handle"):
        robot.move_gripper("vertically aligned with the switch handle")
    # Once the gripper is above the switch handle, we should be able to flip it.
    if check("the robot's gripper is vertically aligned with switch handle"):
        robot.move_gripper("above switch handle")

# turn-off: turn off the switch
def turn_off(robot):
    # Steps:
    #  1. Put gripper above switch handle
    #  2. Flip the switch handle downward
    # First, put the gripper above the switch handle.
    if check("the robot's gripper is not above switch handle"):
        robot.move_gripper("vertically aligned with the switch handle")
    # Once the gripper is above the switch handle, we should be able to flip it.
    if check("the robot's gripper is vertically aligned with switch handle"):
        robot.