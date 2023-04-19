# sweep: grab the cube and move it sideways to the target location
# def sweep(robot):
    # Steps:
    #  1. Put gripper above the cube
    #  2. Grab the cube with the gripper
    #  3. Lift the cube off the surface
    #  4. Move the gripper to the side
    #  5. Move the gripper to the target location
    #  6. Lower the cube to the surface
    # First put the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    # If the gripper is not around the cube, grab it.
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.grab("the cube")
    # If the gripper is holding the cube, lift it off the surface.
    if check("the robot's gripper is holding the cube and the robot's gripper is near the surface"):
        robot.lift("the cube off the surface")
    # Move the gripper to the side.
    if check("the robot's gripper is holding the cube and the robot's gripper is not at the side"):
        robot.slide("gripper to the side")
    # Move the gripper to the target location.
    if check("the robot's gripper is at the side and the robot's gripper is not at the target location"):
        robot.slide("gripper to the target location")
    # Lower the cube to the surface.
    if check("the robot's gripper is at the target location and the robot's gripper is holding the cube"):
        robot.lower("the cube to the surface")