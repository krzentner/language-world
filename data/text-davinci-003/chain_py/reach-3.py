
    # Steps:
    #  1. Point the gripper generally at the target location
    #  2. Move the gripper until it reaches the target location
    #  3. Move the gripper onto the target location
    # Reach requires careful positioning.
    # Line up the gripper's end effector with the target location.
    if check("the robot's gripper is not horizontally aligned with the target location"):
        robot.point("the gripper at the target location")
    # If the target is still to the left of the gripper, move it to the right.
    if check("the target location is left of the robot's gripper and the robot's gripper is horizontal aligned with the the target location"):
        robot.move("the gripper to the target location")
    # If the target is facing the gripper and the gripper isn't quite on the
    # target yet, move the gripper onto the target location.
    if check("the robot's gripper is forward aligned with the target location and the robot's gripper is not on the target location"):
        robot.place("the gripper on the target location")