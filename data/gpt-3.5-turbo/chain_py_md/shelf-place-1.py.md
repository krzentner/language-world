# shelf-place: pick up the block and place it at the target location
def shelf_place(robot):
    # Steps:
    #  1. Move the gripper above the block
    #  2. Drop the gripper around the block
    #  3. Close the gripper around the block
    #  4. Move the block to the target location
    #  5. Open the gripper
    # First, move the gripper above the block.
    if check("the gripper is not above the block"):
        robot.place("gripper above block")
    # Once the gripper is above the block, drop the gripper down to grab it.
    if check("the gripper is above the block and the gripper is not around the block"):
        robot.drop("gripper around block")
    # Close the gripper around the block to grab it.
    if check("the gripper is around the block and the gripper is open"):
        robot.close("gripper around block")
    # Move the block to the target location.
    if check("the gripper is closed and the block is not at the target location"):
        robot.place("block at target location")
    # Open the gripper to release the block.
    if check("the block is at the target location and the gripper is closed"):
        robot.open("gripper")