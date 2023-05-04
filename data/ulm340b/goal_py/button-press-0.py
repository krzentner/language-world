
    # Steps:
    #  1. Put gripper above the button
    #  2. Drop gripper around the button
    #  3. Push down on the button
    #  4. Push down harder
    # First, put the gripper above the button.
    if check("the robot's gripper is not above the button"):
        robot.move_gripper("above the button")
    # If the gripper is above the button, drop it on the button and try pushing
    # down.
    # Close the gripper because the robot's gripper has some space between its
    # fingers.
    if check("the robot's gripper is above the button"):
        robot.move_gripper("near the button", close_gripper=True)
    # If the gripper is around the button, try pushing down harder.
    if check("the robot's gripper is around the button"):
        robot.move_gripper("vertically aligned with the button")

# block-insert-side: insert the block into the slot
def block_insert_side(robot):
    # Steps:
    #  1. Put gripper above the block
    #  2. Grab the block with the gripper
    #  3. Line the block up with the slot
    #  4. Slide the block sideways into the slot
    # First, put the gripper above the block.
    if check("the robot's gripper is not vertically aligned with the block"):
        robot.move_gripper("vertically aligned with the block")
    # If the block becomes left of the gripper, go back to putting the gripper
    # above the block.
    # Because the block is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("the block is not left of the robot's gripper and the block is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the block", close_gripper=True)
    # As long the gripper is still mostly around the block and the block isn't
    # lined up with the slot, line up the block with the slot.
    if check("the block is horizontally aligned with the slot"):
        robot.move_gripper("