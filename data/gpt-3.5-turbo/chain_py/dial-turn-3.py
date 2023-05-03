# Steps:
    #  1. Put gripper around the dial
    #  2. Turn dial to the desired position
    # Similar to picking up an object, we need to first put the gripper roughly
    # around the dial to avoid bumping it.
    if check("the robot's gripper is not around dial and the robot's gripper is open"):
        robot.place("gripper around dial")
    # If the gripper is around the dial, we can turn it to the desired
    # position by rotating the gripper.
    if check("the robot's gripper is around dial"):
        robot.rotate("gripper to desired position")