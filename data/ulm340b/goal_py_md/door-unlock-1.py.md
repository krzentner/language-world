

and then write the rest of the program.

Here are some examples of programs that work:
```


```
# door-unlock: turn the dial on the door
def door_unlock(robot):
    # Steps:
    #  1. Put gripper in front of dial on door
    #  2. Turn the dial on the door to the right
    #  3. Keep turning the dial until it unlocks
    #  4. Push the door open
    # First, make sure the gripper is roughly in front of the dial on the door,
    # and the dial is turned counter-clockwise.
    if check("the robot's gripper is not in front of dial on door"):
        robot.move_gripper("in front of dial on door")
        robot.turn_dial(-1)
        print(robot.check_dial_unlocked())
    # If the robot's gripper is aligned with the dial on the door and the dial is
    # in the counter-clockwise position, push it clockwise.
    if check("the robot's gripper is not vertically aligned with dial on door and the robot's gripper is not around dial on door and the dial on door is turned counter-clockwise"):
        robot.move_gripper("around dial on door")
        print(robot.check_dial_unlocked())
        robot.turn_dial(+1)
    # If the robot's gripper is almost lined up with the door handle, it's time
    # to pull the door open.
    if check("the robot's gripper is vertically aligned with door handle"):
        robot.move_gripper("left of the door handle")

door_unlock(robot)
```

```












































































































































































