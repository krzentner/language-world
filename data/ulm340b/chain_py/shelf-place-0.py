
    # Steps:
    #  1. Put gripper above block
    #  2. Drop gripper around block
    #  3. Close gripper around block
    #  4. Move block to goal
    # First, put the gripper roughly above block, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above block"):
        robot.place("gripper above block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.drop("gripper around block")
    # If the gripper is near the block and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near block and the robot's gripper is open"):
        robot.close("gripper around block")
    # We closed the gripper, and the block is still near the gripper, so maybe
    # we grabbed it.
    # Try to move the block to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is around block and the robot's gripper is closed"):
        robot.place("block at goal")

# grasp-place: grab the object and hold it at the target location
def grasp_place(robot):
    # Steps:
    #  1. Put gripper above object
    #  2. Drop gripper around object
    #  3. Close gripper around object
    #  4. Move object to goal
    # First, put the gripper roughly above object, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the object"):
        robot.place("gripper above object")
    # If the gripper isn't around the object, put it around the object.
    if check("the robot's gripper is not around object and the robot's gripper is open"):
        robot.drop("gripper around object")
    # If the gripper is near the object and open, maybe we can grab it by closing