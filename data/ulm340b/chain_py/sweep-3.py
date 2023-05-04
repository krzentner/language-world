
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move gripper to goal
    # First, put the gripper roughly above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    # If the gripper is not around the cube, put it around the cube.
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # If the gripper is near the cube and open, try to close it around the
    # cube.
    if check("the robot's gripper is near the cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # We closed the gripper, and the cube is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the cube to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above the cube and the robot's gripper is closed"):
        robot.place("cube at goal")

# lift: lift the cube to the target location
def lift(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Raise gripper to goal
    #  5. Open gripper to drop cube
    # First, put the gripper roughly above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    # If the gripper is not around the cube, put it around the cube.
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # If the gripper is near the cube and open, try to close it around the
    # cube.
    if check("the robot's gripper is near the cube and the robot