

Then, write the following steps: 

1. Put the gripper above the cube 
2. Grab the cube with the gripper 
3. Move the cube to the target bin 
4. Drop the cube into the bin

```
# bin-picking: pick up the cube and place it in the target bin
def bin_picking(robot):
    # Steps: 
    #  1. Put the gripper above the cube 
    #  2. Grab the cube with the gripper 
    #  3. Move the cube to the target bin 
    #  4. Drop the cube into the bin

    # First, put the gripper above the cube. 
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the cube is left of the robot's gripper, grab it with the gripper. 
    if check("the cube is left of the robot's gripper"):
        robot.move_gripper("around the cube", close_gripper=True)
    # If the cube is now grasped by the robot's gripper, move it to the target bin. 
    if check("the cube is grasped by the robot's gripper"):
        robot.move_gripper("above the target bin")
    # If the gripper is above the target bin, drop the cube into the bin.
    if check("the robot's gripper is above the target bin"):
        robot.move_gripper("above the bin", close_gripper=False)