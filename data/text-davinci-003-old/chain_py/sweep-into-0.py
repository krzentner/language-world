
    # Steps:
    #  1. Put gripper above cube
    #  2. Grab cube with open gripper
    #  3. Lift cube with gripper
    #  4. Move cube to goal
    # We need to put the gripper above the cube before we can grab it, because
    # of the angle of the robot's gripper.
    if check("the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    # Once the gripper is lined up above the cube, we should be able to grab the
    # cube by moving the gripper down around it.
    if check("the robot's gripper is above cube and the robot's gripper is not around cube"):
        robot.grab("cube")
    # Depending on the size of the cube, we might need to lift the cube off the
    # surface before we start moving it. 
    if check("the cube is below the robot's gripper"):
        robot.lift("cube")
    # Once the cube if lifted off the surface, we can move the cube to target
    # location.
    # Make sure to keep the cube in the gripper's range if possible.
    if check("the cube is above the robot's gripper"):
        robot.move("cube to goal")