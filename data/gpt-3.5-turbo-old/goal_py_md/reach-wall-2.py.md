# reach-wall: reach to the target location with a short wall in the way
# def reach_wall(robot):
    # Steps:
    #  1. Move gripper to location near wall
    #  2. Swing gripper around the wall to the other side
    #  3. Move gripper to target location
    # First, move the gripper to a location near the wall.
    if check("the robot's gripper is not near the wall"):
        robot.move_gripper("near the wall")
    # Once the gripper is close to the wall, swing it around to the other side.
    if check("the robot's gripper is near the wall and the robot's gripper is not vertically aligned with the wall"):
        robot.move_gripper("vertically aligned with the wall")
    # If the gripper is aligned with the wall but not on the other side, move
    # it to the other side of the wall.
    if check("the robot's gripper is vertically aligned with the wall and the robot's gripper is not around the wall"):
        robot.move_gripper("around the wall")
    # Once the gripper is on the other side of the wall, move it to the target
    # location.
    if check("the robot's gripper is around the wall and the robot's gripper is not near the reach target"):
        robot.move_gripper("near the reach target")