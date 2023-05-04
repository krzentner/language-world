
    # Steps:
    #  1. Reach up to the top of the wall
    #  2. Go over the top of the wall
    #  3. Lower down on the other side of the wall
    # We can reach the reach target by going over the top of the wall.
    if check("the robot's gripper is not on top of the wall and the robot's gripper is not near the reach target"):
        robot.move_gripper("near the wall")
    if check("the robot's gripper is on top of the wall and the robot's gripper is not near the reach target"):
        robot.move_gripper("on top of the wall")
    if check("the robot's gripper is on top of the wall and the robot's gripper is not near the reach target"):
        robot.move_gripper("on top of the wall")

# reach-wall-shelf: reach to the target location through a wall with a shelf
def reach_wall_shelf(robot):
    # Steps:
    #  1. Reach up to the top of the wall
    #  2. Go over the top of the wall
    #  3. Go along the shelf to the reach target
    # We can reach the reach target by going over the top of the wall and
    # moving along the shelf.
    if check("the robot's gripper is not above the shelf and the robot's gripper is not near the reach target"):
        robot.move_gripper("on top of the wall")
    if check("the robot's gripper is above the shelf and the robot's gripper is not near the reach target"):
        robot.move_gripper("horizontally aligned with the reach target")

# reach-wall-behind: reach to the target location behind a wall
def reach_wall_behind(robot):
    # Steps:
    #  1. Put gripper around reach target
    #  2. Reach behind the wall
    # We can't reach the reach target from the front, so go around the wall.
    if check("the robot's gripper is not below the reach target"):
        robot.move_gripper("right of the wall")
    if check("the robot's gripper is below the reach target and the robot's gripper is not near the reach target"):
        robot.move_gripper("