
    # Steps:
    #  1. Put gripper above the soccer ball
    #  2. Push down on the soccer ball
    #  3. Move soccer ball to target location
    # First, move the gripper above the soccer ball without touching it.
    if check("the soccer is not below the robot's gripper"):
        robot.move_gripper("above the soccer ball")
    # If the soccer ball is below the gripper, push down on the soccer ball to
    # move it.
    if check("the robot's gripper is above soccer ball"):
        robot.move_gripper("left of the soccer ball")
    # Once the soccer ball starts to move a bit, we can just keep pushing it
    # towards the target location.
    if check("the robot's gripper is above soccer ball"):
        robot.move_gripper("above the soccer ball")