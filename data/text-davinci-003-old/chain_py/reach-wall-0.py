
    # Steps:
    #  1. Reach around the wall to the target
    # We need to position the gripper so it's over the wall.
    # Move the gripper to the right of the wall.
    if check("the robot's gripper is not right of the wall"):
        robot.move("gripper to right of wall")
    # If the gripper is right of the wall, we can try to reach around it to the
    # target location.
    if check("the robot's gripper is right of the wall"):
        robot.reach("around the wall to the target")