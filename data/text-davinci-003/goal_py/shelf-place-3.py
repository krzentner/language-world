
    # Steps:
    #  1. Put gripper in front of block
    #  2. Finish closing gripper
    #  3. Swing gripper and block up
    #  4. Drop the block onto the shelf
    # Move the gripper in front of the block.
    if check("the robot's gripper is not near the block"):
        robot.move_gripper("near the block")
    # If the gripper is near the block, grab it by finishing closing the
    # gripper.
    if check("the robot's gripper is open and the robot's gripper is nearly filled with the block"):
        robot.move_gripper("above the block", close_gripper=True)
    # Once the block is secured in the gripper, swing the gripper and block up.
    if check("the robot's gripper is filled with the block and the robot's gripper is not above the shelf"):
        robot.move_gripper("above the shelf")
    # Finally, drop the block onto the shelf.
    if check("the robot's gripper is above the shelf"):
        robot.move_gripper("near the target location")