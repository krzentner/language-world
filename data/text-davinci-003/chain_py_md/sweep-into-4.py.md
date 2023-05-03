


# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Sweep down and around the corner of the cube
    #  3. Move cube to target location
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above cube"):
        robot.put("gripper above cube")
    # If the cube isn't below the gripper as seen from above, move the
    # gripper down around the corner of the cube.
    if check("the cube is not below the robot's gripper and the cube is not around the corner of the robot's gripper"):
        robot.sweep("down and around cube's corner")
    # If the gripper is around the corner of the cube and so is the cube,
    # move the cube to the target location.
    if check("the robot's gripper is around corner of cube and the cube is around corner of gripper"):
        robot.move("cube to target location")