# shelf-place: pick up the block and place it at the target location
# def shelf_place(robot):
    # Steps:
    #  1. Put gripper above the block
    #  2. Grab the block with the gripper
    #  3. Line up the block with the target location
    #  4. Release the block at the target location
    # First, put the gripper above the block.
    if check("the robot's gripper is not vertically aligned with the block"):
        robot.put("gripper above block")
    # If the gripper is not around the block, grab it.
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.grab("block")
    # If the gripper is around the block, move to target location while lining up the block with it.
    if check("the robot's gripper is around block"):
        robot.move("to target location while aligning block")
    # Place the block at the target location.
    if check("the robot has reached the target location while the block is still in the gripper"):
        robot.release("block at target location")