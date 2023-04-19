# sweep-into: grab the cube and move it to the target location
# def sweep_into(robot):
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is above cube and the cube is not at the target location"):
        # First, sweep the cube into the gripper
        sweep_cube_into_gripper(robot)
        # Then, move the gripper to the target location
        robot.reach("to target location")
        # Drop the cube at the target location
        robot.open("the gripper")

def sweep_cube_into_gripper(robot):
    # Move the gripper to one side of the cube
    robot.move("gripper to the left of cube")
    # Align the gripper with the cube
    robot.align("gripper with cube")
    # Close the gripper around the cube
    robot.close("gripper around cube")
    # Move the gripper and cube to the other side of the table
    robot.slide("gripper and cube to the right")