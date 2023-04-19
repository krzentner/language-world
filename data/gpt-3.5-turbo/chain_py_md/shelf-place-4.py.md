# shelf-place: pick up the block and place it at the target location
# def shelf_place(robot):
    # Steps:
    #  1. Put gripper above the block
    #  2. Grab the block with the gripper
    #  3. Move the block above the shelf
    #  4. Put the block down on the shelf
    # First, put the gripper above the block.
    if check("the robot's gripper is not vertically aligned with the block"):
        robot.put("gripper above block")
    # If the gripper isn't around the block, move the gripper around the
    # block.
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.drop("gripper around block")
    # If the gripper is near the block and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near block and the robot's gripper is open"):
        robot.close("gripper around block")
    # We closed the gripper, the block is still near the gripper, so maybe we
    # grabbed it.
    # Move the block above the shelf.
    if check("the robot's gripper is above block and the robot's gripper is closed"):
        robot.move("block above the shelf")
    # Put the block down on the shelf.
    if check("the block is above the shelf"):
        robot.place("block on the shelf")