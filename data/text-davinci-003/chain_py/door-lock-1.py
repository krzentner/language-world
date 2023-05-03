
    # Steps:
    #  1. Put gripper around the dial
    #  2. Turn the dial the correct amount
    # First, put the gripper roughly around the dial.
    if check("the robot's gripper is not around door handle"):
        robot.grab("door handle")
    # Once the gripper is around the dial, turn the dial with the gripper.
    if check("the robot's gripper is around the door handle"):
        robot.rotate("dial to goal")