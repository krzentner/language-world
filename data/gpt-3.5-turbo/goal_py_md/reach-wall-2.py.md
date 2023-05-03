# reach-wall: reach to the target location with a short wall in the way
def reach_wall(robot):
    # Steps:
    #  1. Move the gripper close to the wall
    #  2. Tilt the gripper to get over the wall
    #  3. Move the gripper to the target location
    # First, move the gripper close to the wall, keeping it parallel to the wall.
    if check("the robot's gripper is not parallel with the wall and the robot's gripper is not near the wall"):
        robot.move_gripper("parallel with the wall and near the wall")
    # Once the gripper is near the wall, we need to tilt it to get over the wall.
    if check("the robot's gripper is near the wall and the robot's gripper is not tilted over the wall"):
        robot.move_gripper("tilted over the wall")
    # Finally, move the gripper to the target location.
    if check("the robot's gripper is tilted over the wall and the robot's gripper is not near the reach target"):
        robot.move_gripper("near the reach target")