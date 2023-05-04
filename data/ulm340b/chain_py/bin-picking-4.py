
    # Steps:
    #  1. Put gripper near one of the cubes
    #  2. Drop gripper around one of the cubes
    #  3. Close gripper around one of the cubes
    #  4. Move one of the cubes to the goal
    # First, get the gripper near one of the cubes.
    if check("the robot's gripper is not near one of the cubes"):
        robot.move("gripper near one of the cubes")
    # If the gripper isn't around one of the cubes, put it around one of the cubes.
    if check("the robot's gripper is not around one of the cubes and the robot's gripper is open"):
        robot.drop("gripper around one of the cubes")
    # If the gripper is near one of the cubes and open, maybe we can grab one of the cubes by closing the gripper.
    if check("the robot's gripper is near one of the cubes and the robot's gripper is open"):
        robot.close("gripper around one of the cubes")
    # We closed the gripper, and one of the cubes is still near the gripper, so maybe we grabbed one of the cubes.
    # Try to move the cube to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is near one of the cubes and the robot's gripper is closed"):
        robot.place("one of the cubes at goal")

# insert: pick up the block and insert it into the hole
def insert(robot):
    # Steps:
    #  1. Put gripper above block
    #  2. Drop gripper around block
    #  3. Close gripper around block
    #  4. Line up the block with the hole
    #  5. Drop the block in the hole
    # First, get the gripper above the block.
    if check("the robot's gripper is not above block and the robot's gripper is not vertically aligned with block"):
        robot.put("gripper above block")
    # If the gripper is vertically aligned with block but not around block, put the gripper around block.
    if check("the robot's gripper is vertically aligned with block and the robot's gripper is not