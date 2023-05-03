

The robot should be able to reach the target location with a short wall in the way.

# reach-wall: reach to the target location with a short wall in the way
def reach_wall(robot):
    # Steps:
    #  1. Put gripper above wall
    #  2. Reach over the wall 
    #  3. Keep gripping and reach the target

    # First, the robot should put its gripper above the wall.
    if check("the robot's gripper is not above wall"):
        robot.move_gripper("above wall")
    # After putting the gripper above the wall, the robot should reach over it.
    if check("the robot's gripper is not above target and the robot's gripper is not over wall"):
        robot.move_gripper("over wall")
    # Finally, the robot should keep grasping and reach out to the target.
    if check("the robot's gripper is above target"):
        robot.move_gripper("near the reach target")