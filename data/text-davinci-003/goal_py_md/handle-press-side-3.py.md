

The steps to complete this task are: 
  1. Put the gripper roughly along side the handle
  2. Push down on the handle from the side 

To begin, we need to move the gripper to the side of the handle. 

```
# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    # Steps:
    #  1. Put gripper roughly along side the handle
    #  2. Push down on the handle from the side
    #If the robot's gripper is not roughly along side the handle, move it there
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle") 
```

Next, the gripper needs to push down on the handle from the side. 

```
# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    # Steps:
    #  1. Put gripper roughly along side the handle
    #  2. Push down on the handle from the side
    # If the robot's gripper is not roughly along side the handle, move it there
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle") 
    # Now that the robot's gripper is near the handle, push down on it from the side
    if check("the robot's gripper is near the handle"):
        robot.move_gripper("horizontally aligned with the handle") 
```

Finally, the handle should move down as the gripper pushes it from the side.

```
# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    # Steps:
    #  1. Put gripper roughly along side the handle
    #  2. Push down on the handle from the side
    # If the robot's gripper is not roughly along side the handle, move it there
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle") 
    # Now that the robot's gripper is near the handle, push down on it from the side
    if check("the robot's gripper is near the handle"):
        robot.move_gripper("horizontally aligned with the handle")
    #Once the handle has been pressed down, the task is complete. 
    if check("the handle is below the robot's gripper"):
        robot.move_gri