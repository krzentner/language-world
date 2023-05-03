# sweep: grab the cube and move it sideways to the target location
def sweep(robot):
    # Steps:
    #  1. Put the gripper next to the cube
    #  2. Open the gripper to get ready to grab the cube
    #  3. Move the gripper around the cube and grab it
    #  4. Shift the gripper with the cube sideways to the target location
    #  5. Release the gripper and drop the cube at the target location
    # First, put the gripper next to the cube.
    if check("the robot's gripper is not near the cube"):
        robot.move("gripper next to cube")
    # Open the gripper to get ready to grab the cube.
    if check("the robot's gripper is near the cube and the robot's gripper is closed"):
        robot.open("gripper")
    # Move the gripper around the cube and grab it.
    if check("the robot's gripper is open and the cub is not inside the gripper"):
        robot.grab("cube")
    # Shift the gripper with the cube sideways to the target location.
    if check("the cube is in the gripper and the robot is not at the target location"):
        robot.shift("cube to target location")
    # Release the gripper and drop the cube at the target location.
    if check("the cube is in the gripper and the robot is at the target location"):
        robot.release("cube at target location")