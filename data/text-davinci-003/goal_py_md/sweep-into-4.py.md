

The task 'sweep-into' involves grab the cube and move it to the target location

Steps: 
1. Put the gripper above the cube 
2. Drop the gripper around the cube 
3. Push the cube to the target location

Code:
# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    # Steps:
    #  1. Put gripper above the cube
    #  2. Drop gripper around the cube
    #  3. Push the cube to the target location
    # Put the gripper above the cube so it doesn't accidentally touch the cube
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the cube is left of the gripper, line up the gripper with it
    if check("the cube is not left of the robot's gripper"):
        robot.move_gripper("left of the cube")
    # Once the gripper is lined up, move it around the cube to grab it.
    if check("the robot's gripper is left of the cube and the robot's gripper is not around the cube"):
        robot.move_gripper("around the cube")
    # Once the gripper is around the cube, we can slide it to the target location.
    if check("the robot's gripper is around the cube"):
        robot.move_gripper("near the target location")