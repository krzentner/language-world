# Steps:
    #  1. Move gripper to the side of the wall
    #  2. Put gripper above puck
    #  3. Drop gripper around puck
    #  4. Close gripper around puck
    #  5. Move puck to goal
    # First, we need to move the gripper to the correct side of the wall to be able to access the puck.
    if check("the gripper is not on the correct side of the wall"):
        robot.move("gripper to the side of the wall")
    # Once the gripper is on the correct side of the wall, put it above the puck.
    if check("the gripper is on the correct side of the wall and the robot's gripper is not above the puck"):
        robot.put("gripper above the puck")
    # Drop the gripper around the puck.
    if check("the robot's gripper is above the puck and the gripper is not around the puck"):
        robot.drop("gripper around the puck")
    # Close the gripper around the puck.
    if check("the robot's gripper is around the puck and the gripper is not closed"):
        robot.close("gripper around the puck")
    # Move the puck to the goal.
    if check("the robot's gripper is closed around the puck and it's not at the goal"):
        robot.place("puck at goal")