

Steps:
1. Move the robot's gripper to be behind the cube.
2. Grab the cube from the back side with the gripper.
3. Move the cube to the target location. 

```
# sweep-into: grab the cube and move it to the target location
# def sweep_into(robot):
    # Steps:
    #  1. Move the robot's gripper to be behind the cube.
    #  2. Grab the cube from the back side with the gripper.
    #  3. Move the cube to the target location.
    if check("the robot's gripper is not behind the cube"):
        robot.move("gripper behind cube")

    if check("the robot's gripper is behind the cube and the robot's gripper is not around the cube"):
        robot.grab("cube from back")
    
    if check("the robot's gripper is above the cube and the robot's gripper is closed"):
        robot.slide("cube to goal")

```