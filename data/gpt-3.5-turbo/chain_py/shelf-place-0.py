# Steps:
    #  1. Put gripper above block
    #  2. Drop gripper around block
    #  3. Close gripper around block
    #  4. Lift block up
    #  5. Move block to goal
    #  6. Lower block
    # First, put the gripper roughly above the block, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the block"):
        robot.place("gripper above block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.drop("gripper around block")
    # If the gripper is near the block and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near block and the robot's gripper is open"):
        robot.close("gripper around block")
    # We closed the gripper, and the block is still near the gripper, so maybe we
    # grabbed it.
    # Try to lift the block up.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is around block and the block is below the robot's gripper"):
        robot.lift("block up")
    # If the gripper is holding the block, we can move it to the target location.
    if check("the robot's gripper is holding block"):
        robot.move("block to goal")
    # Once we reach the destination, we can lower the block down onto the shelf.
    if check("the robot's gripper is above the goal location"):
        robot.place("block on shelf")