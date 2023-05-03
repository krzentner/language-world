

Steps:
1. Reach the cube with the gripper.
2. If the cube is not being grasped, close the gripper around the cube.
3. Move towards the bin and lower the cube into it.
4. Once the cube is inside the bin, release the cube from the gripper.

```
# bin-picking: pick up the cube and place it in the target bin
# def bin_picking(robot):
    # Steps:
    #  1. Reach the cube with the gripper.
    if check("the robot's gripper is not near the cube"):
        robot.reach("cube")
    #  2. If the cube is not being grasped, close the gripper around the cube.
    if check("the robot's gripper is near the cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    #  3. Move towards the bin and lower the cube into it.
    if check("the robot's gripper is above the bin and the robot's gripper is closed"):
        robot.place("cube in bin")
    #  4. Once the cube is inside the bin, release the cube from the gripper.
    if check("the cube is inside the bin"):
        robot.open("gripper around cube")
```