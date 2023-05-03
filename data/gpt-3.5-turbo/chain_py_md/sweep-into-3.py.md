# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around the side of the cube
    #  3. Close gripper around the cube
    #  4. Move cube to target location
    # First, put the gripper above the cube, to prep for grabbing it.
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    # Once the gripper is above the cube, move it around the side of the cube
    # until it's ready to be grabbed.
    if check("the robot's gripper is above the cube and not around the cube"):
        robot.put("gripper around the side of the cube")
    # Now that the gripper is positioned around the cube, close it to grab the
    # cube.
    if check("the robot's gripper is around the cube and open"):
        robot.close("gripper around the cube")
    # Once the gripper is closed around the cube and the cube is near the
    # gripper, move it to the target location.
    if check("the robot's gripper is around the cube and the robot's gripper is near the target location"):
        robot.move("cube to target location")