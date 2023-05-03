# push: slide the puck to the target location
def push(robot):
    # Steps:
    #  1. Put gripper near the puck
    #  2. Push the puck towards the target location
    # First, put the gripper near the puck.
    if check("the robot's gripper is not near the puck"):
        robot.put("gripper near puck")
    # If the puck is left of the gripper, move the gripper to the left.
    if check("puck is left of the robot's gripper"):
        robot.move("gripper to the left of the puck")
    # Once the gripper is lined up with the puck, start pushing it towards the
    # target location. In this case, we'll push it to the right.
    if check("the robot's gripper is almost aligned with the puck"):
        robot.slide("puck right")