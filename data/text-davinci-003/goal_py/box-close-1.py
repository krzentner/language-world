
    # Steps:
    #  1. Put gripper near the box lid
    #  2. Pick up the box lid
    #  3. Place the box lid onto the box
    # If the robot's gripper is not near the box lid, move the gripper near it.
    if check("the robot's gripper is not near the box lid"):
        robot.move_gripper("near the box lid", close_gripper=True)  
    # If the box lid is below the gripper as seen from above, pick up the box
    # lid.
    if check("the robot's gripper is near the box lid and the box lid is below the robot's gripper"):
        robot.move_gripper("above the box")
    # Once the box lid is picked up, move the gripper towards the box and
    # place the box lid on top.
    if check("the robot's gripper is above the box and the box lid is below the robot's gripper"):
        robot.move_gripper("near the box")