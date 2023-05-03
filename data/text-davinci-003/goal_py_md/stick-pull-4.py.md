

Steps: 
1. Put gripper below the stick 
2. Grab the stick with the gripper 
3. Move the stick to the thermos until it is near 
4. Pull the thermos towards you 

```
# stick-pull: grab the stick and use it to pull the thermos to the target location
def stick_pull(robot):
    # Steps:
    #  1. Put gripper below the stick
    #  2. Grab the stick with the gripper
    #  3. Move the stick to the thermos until it is near
    #  4. Pull the thermos towards you
    # First, put the gripper below the stick.
    if check("the robot's gripper is not below the stick"):
        robot.move_gripper("below the stick")
    # If the gripper is above the stick but not near it, grab it.
    if check("the robot's gripper is above the stick and the robot's gripper is not near the stick"):
        robot.move_gripper("near the stick", close_gripper=True)
    # If the gripper is around the stick, move it towards the thermos until it
    # is near it.
    if check("the robot's gripper is near the stick and the stick is not near the thermos"):
        robot.move_gripper("near the thermos")
    # With the stick near the thermos, grab it and pull it towards you.
    if check("the robot's gripper is near the thermos"):
        robot.move_gripper("towards you")
```