

The steps for this program are as follows:

1. Put gripper above short wall
2. Reach over short wall
3. Reach towards the target

# reach-wall: reach to the target location with a short wall in the way
def reach_wall(robot):
    # Steps:
    #  1. Put gripper above the short wall
    #  2. Reach over the short wall
    #  3. Reach towards the target
    # We need to move the gripper above the short wall, so it's out of the way.
    if check("the robot's gripper is not above the short wall"):
        robot.move_gripper("above the short wall")
    # Once the gripper is above the wall, reach over the wall with the robot's
    # arm.
    if check("the robot's arm is not over the wall"):
        robot.move_arm("over the wall")
    # When the arm is over the wall, move the gripper to the target.
    if check("the robot's arm is over the wall"):
        robot.move_gripper("near the reach target")