
    # Steps:
    #  1. Put gripper above wrench
    #  2. Grab the wrench
    #  3. Lift wrench off the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.move_gripper("vertically aligned with the wrench")
    # Once the gripper is vertically aligned with the wrench, we can just drop
    # the gripper down to grab it.
    if check("the robot's gripper is vertically aligned with the wrench and the wrench is below the robot's gripper"):
        robot.move_gripper("near the wrench", close_gripper=True)
    # If the gripper is open, we can lift the wrench by closing the gripper.
    if check("the robot's gripper is near the wrench and the robot's gripper is closed"):
        robot.move_gripper("below the wrench")

# flip-switch-down: flip the switch from up to down
def flip_switch_down(robot):
    # Steps:
    #  1. Put gripper above switch handle
    #  2. Flip switch
    # First, put the gripper above the switch handle.
    if check("the robot's gripper is not vertically aligned with switch handle"):
        robot.move_gripper("vertically aligned with the switch handle")
    # Once the gripper is vertically aligned with the switch handle, we can flip
    # the switch.
    if check("the robot's gripper is vertically aligned with switch handle"):
        robot.move_gripper("around the switch handle")

# flip-switch-up: flip the switch from down to up
def flip_switch_up(robot):
    # Steps:
    #  1. Put gripper above switch handle
    #  2. Flip switch
    # First, put the gripper above the switch handle.
    if check("the robot's gripper is not vertically aligned with switch handle"):
        robot.move_gripper("vertically aligned with the switch handle")
    # Once the gripper is vertically aligned with the switch handle, we can flip
    # the switch.
    if check("the robot's gripper is vertically aligned with switch handle"):
        robot.move_gripper("around the