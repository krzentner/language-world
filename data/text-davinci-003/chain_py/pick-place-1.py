
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Move puck to goal
    # First, put the gripper above the hockey puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    # Once the puck is below the gripper, drop the gripper around the puck.
    if check("the robot's gripper is vertically aligned with puck"):
        robot.drop("gripper around puck")
    # Move the puck to the goal by moving the robot's gripper.
    if check("the robot's gripper is around puck and the puck is below the robot's gripper"):
        robot.move("puck to goal")