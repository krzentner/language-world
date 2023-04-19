# Steps:
    #  1. Move gripper to right of the wall
    #  2. Move gripper up above the wall
    #  3. Move gripper left to target location
    # To reach a target location with a short wall in the way, we can first move
    # the gripper to the right of the wall.
    if check("the robot's gripper is not right of the wall"):
        robot.move("gripper to right of wall")
    # Once the gripper is right of the wall, we can move it up above the wall.
    if check("the robot's gripper is right of the wall and the robot's gripper is not above the wall"):
        robot.move("gripper up above the wall")
    # Finally, move the gripper left to the target location.
    if check("the robot's gripper is above the wall and the robot's gripper is not at the target location"):
        robot.move("gripper to target location")