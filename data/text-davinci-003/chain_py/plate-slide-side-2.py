
    # Steps:
    #  1. Place the gripper near the plate
    #  2. Place the gripper around the plate
    #  3. Push the plate sideways
    # If the robot's gripper is not near the plate, it should move the robot's
    # gripper near the plate.
    if check("the robot's gripper is not near the plate"):
        robot.place("gripper near plate")
    # If the robot's gripper is near the plate and not around it, the robot
    # should move the gripper around the plate.
    if check("the robot's gripper is near the plate and the robot's gripper is not around the plate"):
        robot.grab("plate")
    # Once the gripper is around the plate, the robot can start pushing it
    # sideways towards the goal.
    if check("the robot's gripper is around the plate"):
        robot.slide("plate to goal")