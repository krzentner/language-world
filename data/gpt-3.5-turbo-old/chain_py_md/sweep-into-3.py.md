# sweep-into: grab the cube and move it to the target location
# def sweep_into(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper to grab cube
    #  4. Lift up the cube and move it towards the target location
    #  5. Drop the cube at the target location
    # First, put the gripper above the cube, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # We closed the gripper and grabbed the cube, now let's move it towards
    # the target location.
    # First, lift up the cube.
    if check("the robot's gripper is closed and the cube is below the gripper"):
        robot.lift("the cube")
    # Move the cube towards the target location.
    if check("the robot's gripper is holding the cube and it's not yet at the goal"):
        robot.move("the cube towards the goal")
    # Once we reach the goal, drop the cube.
    if check("the robot's gripper is holding the cube and it's at the goal"):
        robot.drop("the cube at the goal")