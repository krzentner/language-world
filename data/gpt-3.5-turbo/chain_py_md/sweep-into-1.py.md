# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    # Steps:
    #  1. Put gripper in front of the cube
    #  2. Grab the cube with the gripper
    #  3. Move the gripper until the cube is aligned with the target location.
    #  4. Push the gripper so that the cube slides into the target location.
    # First, put the gripper in front of the cube.
    if check("the robot's gripper is not in front of the cube"):
        robot.move("gripper in front of cube")
    # If the gripper is in front of the cube, but not holding it, grab the cube with the gripper.
    if check("the robot's gripper is in front of the cube and the robot's gripper is open"):
        robot.grab("cube")
    # If the gripper is holding the cube, move the gripper so that the cube is aligned with the target location.
    if check("the robot's gripper is holding the cube and the cube is not aligned with the target location"):
        robot.align("cube to target location")
    # If the gripper is holding the cube and the cube is aligned with the target location, push the gripper so that the cube slides into the target location.
    if check("the robot's gripper is holding the cube and the cube is aligned with the target location"):
        robot.push("the gripper to slide the cube into the target location")