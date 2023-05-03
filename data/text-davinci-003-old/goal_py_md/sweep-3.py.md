

Steps:
    1. Put gripper directly above cube 
    2. Drop gripper around cube
    3. Close gripper around cube
    4. Move cube sideways to the target location

If the robot's gripper is not above the cube, move it directly above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")

If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)

If the gripper is near the cube and open, maybe we can grab it by closing the gripper.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.move_gripper("near the target location")
        
If the robot's gripper is near the cube and the cube is above the robot's gripper, move the cube sideways to the target location.
    if check("the robot's gripper is near the cube and the cube is below the robot's gripper"):
        robot.move_gripper("sideways to the target location")