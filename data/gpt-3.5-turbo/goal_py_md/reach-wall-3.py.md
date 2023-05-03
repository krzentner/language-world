# reach-wall: reach to the target location with a short wall in the way
def reach_wall(robot):
    # Steps:
    #  1. Align the gripper perpendicular to the wall
    #  2. Move towards the target, staying parallel to the wall
    #  3. Move the gripper to the target location
    # First, align the gripper perpendicular to the wall.
    if check("the robot's gripper is not perpendicular to the wall"):
        robot.move_gripper("perpendicular to the wall")
    # Move towards the target while staying parallel to the wall.
    if check("the robot's gripper is not near the target location and the robot's gripper is not parallel to the wall"):
        robot.move_gripper("parallel to the wall")
    # Once the robot is parallel to the wall and near the target location,
    # move the gripper to the target location.
    if check("the robot is parallel to the wall and near the target location"):
        robot.move_gripper("near the reach target")