
    # Steps:
    #  1. Put gripper above puck, above wall
    #  2. Drop gripper around puck, above wall
    #  3. Close gripper around puck, still above wall
    #  4. Move puck to goal, pushing the wall
    # Put the gripper above the puck and above the wall, so that it won't hit the
    # wall.
    if check("the robot's gripper is not vertically aligned with the puck and the robot's gripper is not above the wall"):
        robot.move("gripper above puck, above wall")
    # Drop the gripper to grab the puck and make sure we don't hit the wall.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not around the puck"):
        robot.drop("gripper around puck, above wall")
    # If the gripper is around the puck, close the gripper so that we can move
    # it and the wall at the same time.
    if check("the robot's gripper is around the puck and the puck is not in front of the gripper and the wall is not in front of the gripper"):
        robot.close("gripper around puck, above wall")
    # If the gripper is in front of the wall and the puck, push the wall and the
    # puck to the goal.
    if check("the gripper is in front of the wall and the puck"):
        robot.push("wall and puck to goal")