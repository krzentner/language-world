

The robot needs to grab the cube and move it to the target location.

Steps:

1. Put gripper above the cube
2. Reach the gripper onto the cube
3. Close the gripper around the cube
4. Sweep the cube to the target location

# sweep-into: grab the cube and move it to target location
# def sweep_into(robot):
    # Steps: 
    # 1. Put gripper above the cube 
    if check("the robot's gripper is not above cube"):
        robot.put("gripper above cube")
    # 2. Reach the gripper onto the cube
    # Since the cube is relatively small, it's important to line the gripper up
    # as best as possible, which may require the robot to scan the cube before
    # reaching its gripper on it.
    if check("the robot's gripper is not around cube"):
        robot.reach("gripper onto cube")
    # 3. Close the gripper around the cube
    # Once the gripper is around the cube, we can close the gripper around it
    if check("the robot's gripper is around cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # 4. Sweep the cube to the target location
    # After the cube is securely in the gripper, we can sweep the cube to the
    # target location
    if check("the robot has closed its gripper around the cube and the cube is not at the target location"):
        robot.sweep("cube to target location")