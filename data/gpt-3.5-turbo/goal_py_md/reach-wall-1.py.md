# reach-wall: reach to the target location with a short wall in the way
def reach_wall(robot):
    # Steps:
    #  1. Move gripper to the left side of the wall
    #  2. Move gripper up until it clears the wall
    #  3. Move gripper towards the target
    # First, move the gripper to the left side of the wall.
    if check("the robot's gripper is not left of the wall"):
        robot.move_gripper("left of the wall")
    # Next, move the gripper up until it clears the wall.
    if check("the robot's gripper is not clearing the wall"):
        robot.move_gripper("above the wall")
    # Finally, move the gripper towards the target.
    if check("the robot's gripper is not near reach target"):
        robot.move_gripper("near the reach target")