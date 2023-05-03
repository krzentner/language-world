# Steps:
    #  1. Put gripper beside the cube
    #  2. Push gripper into the cube
    #  3. Lift the cube up off the surface
    #  4. Move the cube to the target location
    #  5. Lower the cube down onto the surface at the target location
    # First, position the gripper beside the cube.
    if check("the robot's gripper is not beside the cube"):
        robot.move("gripper beside cube")
    # Move the gripper into the cube to trap it.
    if check("the robot's gripper is beside the cube and the cube is not trapped"):
        robot.push("the gripper into the cube")
    # Once the cube is trapped, lift it off the surface.
    if check("the cube is trapped and not lifted off surface"):
        robot.lift("the cube off the surface")
    # Move the gripper to the target location with the cube trapped inside.
    if check("the cube is trapped and the robot's gripper is not at the target location"):
        robot.move("gripper to target location")
    # Lower the cube down onto the surface at the target location.
    if check("the robot's gripper is at the target location and the cube is not placed on the surface"):
        robot.drop("the cube onto the surface")