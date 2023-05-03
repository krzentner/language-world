

# shelf-place: pick up the block and place it at the target location
def shelf_place(robot):
    # Steps:
    #  1. Put gripper above block
    #  2. Drop gripper around block
    #  3. Close gripper around block
    #  4. Move block to goal
    #  5. Place block on shelf

    # First, put the gripper roughly above the block.
    if check("the robot's gripper is not above the block"):
        robot.put("gripper above block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.drop("gripper around block")
    # If the gripper is near the block and open, try to grab it by closing the
    # gripper.
    if check("the robot's gripper is near block and the robot's gripper is open"):
        robot.close("gripper around block")
    # Check if the block is still near the robot's gripper.
    # If the block is above the gripper and the gripper is closed, try to move 
    # the block to the goal.
    if check("the robot's gripper is above block and the robot's gripper is closed"):
        robot.move("block to goal")
    # Once the block is at the goal, place it on the shelf.
    if check("the block is at the goal"):
        robot.place("block on shelf")