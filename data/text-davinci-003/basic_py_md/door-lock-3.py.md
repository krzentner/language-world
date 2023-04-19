

Here's the program:

```
# door-lock: turn the dial on the door
# def door_lock(robot):
    if check("the robot's gripper is not near the door lock dial"):
        robot.reach("to door lock dial")
    if check("the robot's gripper is near the door lock dial and the robot's gripper is open"):
        robot.grab("door lock dial")
    if check("the robot's gripper is around the door lock dial and the door lock dial is rotated to the left"):
        robot.turn("door lock dial clockwise")
    if check("the robot's gripper is around the door lock dial and the door lock dial is rotated to the right"):
        robot.turn("door lock dial counter-clockwise")    
```