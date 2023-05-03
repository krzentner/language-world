
    # Steps:
    #  1. Put gripper above wall
    #  2. Reach around wall
    #  3. Reach towards the target
    # Because of the short wall, we'll need to move the robot's gripper in two
    # steps.
    # First, place the gripper above the short wall, then move around the wall.
    if check("the robot's gripper is not above the wall"):
        robot.put("gripper above wall")
    # Move the gripper's arm around the wall.
    if check("the robot's gripper is above the wall and the robot's gripper is not around the wall"):
        robot.put("gripper around wall")
    # Now that the gripper is around the wall, we can reach for the target
    # location.
    if check("the robot's gripper is around wall"):
        robot.reach("to goal")