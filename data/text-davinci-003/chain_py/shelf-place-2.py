
    # Steps:
    #  1. Put gripper in front of shelf
    #  2. Reach up to grasp block
    #  3. Pull block out of shelf
    #  4. Move block to goal
    # We want to pick up a block from a shelf.
    # We need to move the gripper in front of the shelf first.
    if check("the robot's gripper is not in front of shelf"):
        robot.move("gripper in front of shelf")
    # If the gripper is in front of the shelf, we can try to grasp the block by
    # reaching up.
    if check("the robot's gripper is in front of shelf and the block is not within reach of robot's gripper"):
        robot.reach("up to grasp block")
    # When the gripper has the block, try to pull the block out of the shelf.
    if check("the block is within reach of robot's gripper"):
        robot.pull("block out of shelf")
    # If the block is no longer in the shelf, move it to the goal.
    if check("the block is no longer in shelf"):
        robot.place("block at goal")