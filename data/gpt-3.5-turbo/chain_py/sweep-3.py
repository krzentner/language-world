# Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move cube to side
    #  5. Move gripper to goal
    # First, put the gripper roughly above the cube, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # We closed the gripper, and the cube is still near the gripper, so maybe we
    # grabbed it.
    # Now we want to move the cube to the side.
    # If the gripper is not left of the cube, move it left.
    if check("the robot's gripper is not left of the cube"):
        robot.move("gripper left")
    # If the gripper is left of the cube, move it farther left to slide the cube
    # to the target location.
    if check("the robot's gripper is left of the cube"):
        robot.slide("cube to the goal")
    # Once we're near the target location, move the gripper (with the cube) to
    # the goal.
    if check("the robot's gripper is near the goal"):
       robot.move("the gripper to the goal")