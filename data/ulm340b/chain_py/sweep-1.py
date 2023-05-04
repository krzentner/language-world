
    # Steps:
    #  1. Move gripper to the front of the cube
    #  2. Push gripper into the top of the cube
    #  3. Close gripper around top of cube
    #  4. Slide gripper sideways to the target location
    # Since the cube is large, we don't have to worry about moving it around or
    # aligning it.
    # We can just start pushing it right away.
    if check("the robot's gripper is not near the front of the cube"):
        robot.move("gripper to front of cube")
    # If the robot's gripper is in front of the cube, we can push into the
    # cube's top to grab it.
    if check("the robot's gripper is near the front of the cube"):
        robot.push("into the top of the cube")
    # If the robot's gripper is near the cube and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is near the cube and the robot's gripper is open"):
        robot.close("gripper around top of cube")
    # We closed the gripper, and the cube is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the cube to the target location.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is near the top of cube and the robot's gripper is closed"):
        robot.slide("gripper to the target location")

# grasp: grab the cube and move it to the target location
def grasp(robot):
    # Steps:
    #  1. Put gripper above the cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Lift cube up
    # First, put the gripper above the cube so that we don't accidentally bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's