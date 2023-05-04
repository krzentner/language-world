
    # Steps:
    #  1. Put gripper above block
    #  2. Drop gripper around block
    #  3. Close gripper around block
    #  4. Move block to goal
    # The block is like the puck except we have to place it on a shelf.
    # First, put the gripper roughly above block, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not vertically aligned with the block"):
        robot.put("gripper above block")
    # If the gripper is above the block but not around it, drop the gripper
    # around it.
    if check("the robot's gripper is above the block and the robot's gripper is open"):
        robot.drop("gripper around block")
    # If the gripper is near the block and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near block and the robot's gripper is open"):
        robot.close("gripper around block")
    # We closed the gripper, and the block is still near the gripper, so maybe we
    # grabbed it.
    # Try to place the block on the shelf.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is around block"):
        robot.put("block on shelf")

# block-stack: pick up the block and stack it on top of the other block
def block_stack(robot):
    # Steps:
    #  1. Put gripper above block
    #  2. Drop gripper around block
    #  3. Close gripper around block
    #  4. Line gripper up with shelf
    #  5. Put block on shelf
    # The block is like the puck except we have to place it on a shelf.
    # First, put the gripper roughly above block, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the block"):
        robot.put("gripper above block")
    # If the gripper is above the block but not around it, drop the gripper