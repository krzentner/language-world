# Steps:
    #  1. Put gripper in front of cube
    #  2. Move gripper towards the cube until it's very close
    #  3. Close gripper around the cube
    #  4. Move gripper with cube to the target location
    # First, put the gripper near the cube, by moving it in front of the cube.
    if check("the robot's gripper is not in front of the cube"):
        robot.move("gripper in front of cube")
    # If the gripper isn't close to the cube, move it closer.
    if check("the robot's gripper is not near the cube"):
        robot.move("gripper towards the cube")
    # If the gripper is near the cube, close the gripper to grab it.
    if check("the robot's gripper is near the cube and the gripper is open"):
        robot.close("gripper around the cube")
    # If we grabbed the cube, move it to the target location.
    # Otherwise, go back to an earlier step.
    if check("the robot's gripper is holding the cube"):
        robot.place("cube at goal")