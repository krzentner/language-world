# Steps:
    #  1. Put gripper above the puck
    #  2. Push the gripper against the wall to tip the puck over it
    #  3. Move the gripper to capture the puck on the other side of the wall
    #  4. Slide the puck to the target location
    # The wall makes it more challenging since we need to tip the puck over it before we can slide it.
    # If the gripper is not above the puck, move it there to start.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't touching the wall, we need to push it against the wall to tip the puck over.
    if check("the gripper is not touching the wall"):
        robot.move_gripper("friction against the wall")
    # If the gripper is touching the wall and the puck has tipped over to the other side, move the gripper to the other side to capture the puck.
    if check("the gripper is touching the wall and the puck has tipped over"):
        robot.move_gripper("above the puck")
    # Once we have the puck on the gripper on the other side of the wall, we just need to slide it to the target location.
    if check("the robot's gripper is near the target location"):
        robot.move_gripper("above the target location")