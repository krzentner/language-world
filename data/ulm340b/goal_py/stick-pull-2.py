
    # Steps:
    #  1. Grab the stick
    #  2. Move the stick towards the thermos
    #  3. Pull the thermos towards the goal
    # First, grab the stick.
    if check("the robot's gripper is not around the stick"):
        robot.move_gripper("above the stick", close_gripper=True)
    # Once the gripper is around the stick, move the stick towards the thermos.
    if check("the robot's gripper is around the stick"):
        robot.move_gripper("above the thermos")
    # Now that the stick is near the thermos, we can push the thermos towards
    # the goal.
    if check("the robot's gripper is above the thermos"):
        robot.move_gripper("above the target location")

# cloth-pull: pick up the cloth and use it to pull the thermos to the target location
def cloth_pull(robot):
    # Steps:
    #  1. Pick up the cloth
    #  2. Drag the cloth towards the thermos
    #  3. Pull the thermos towards the goal
    # Grab the cloth and pull it towards the thermos.
    # If the robot's gripper is not above the cloth, move it above the cloth.
    if check("the robot's gripper is not above the cloth"):
        robot.move_gripper("above the cloth", close_gripper=True)
    # If the robot's gripper is above the cloth and the cloth is not near the
    # robot's gripper, move the gripper near the cloth.
    if check("the robot's gripper is above the cloth and the cloth is not near the robot's gripper"):
        robot.move_gripper("near the cloth")
    # If the robot's gripper is around the cloth, drag the cloth towards the
    # thermos.
    if check("the robot's gripper is around the cloth"):
        robot.move_gripper("above the thermos")
    # Now that the cloth is near the thermos, we can pull the thermos towards the
    # goal.
    if check("the robot's gripper is above the thermos"):
        robot.move_gripper("above the target location")

#