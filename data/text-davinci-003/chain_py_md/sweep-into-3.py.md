

Steps:
1. Put gripper to the left of the cube
2. Move gripper around the left side of the cube
3. Close gripper around the cube
4. Move cube to target location

#sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    # Steps:
    #  1. Put gripper to the left of the cube
    #  2. Move gripper around the left side of the cube
    #  3. Close gripper around the cube
    #  4. Move cube to target location
    # Put the gripper to the left of the cube
    if check("the robot's gripper is not left of the cube"):
        robot.put("gripper to left of cube")
    # If the gripper is slightly left of the cube, move it around the left
    # side of the cube.
    if check("the robot's gripper is slightly left of the cube"):
        robot.sweep("gripper around left side of cube")
    # If the gripper is aligned with the cube, close it around the cube.
    if check("the robot's gripper is aligned with cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # Once the gripper is closed, we can move the cube to the target location 
    if check("the robot's gripper is closed around cube"):
        robot.move("cube to target location")