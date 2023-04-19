

Here's the program:

```
# door-lock: turn the dial on the door
# def door_lock(robot):
    # Steps:
    #  1. Put gripper above the door lock knob
    #  2. Drop gripper around the door lock knob
    #  3. Turn the door lock knob
    # First, put the gripper above the door lock knob, so that we don't bump it while trying to grab it.
    if check("the robot's gripper is not above the door lock knob"):
        robot.put("gripper above door lock knob")
    # If the gripper isn't around the door lock knob, put it around the knob.
    if check("the robot's gripper is not around door lock knob and the robot's gripper is open"):
        robot.drop("gripper around door lock knob")
    # Once the gripper is around the door lock knob, turn the knob to lock the door.
    if check("the robot's gripper is around door lock knob"):
        robot.turn("door lock knob")
```