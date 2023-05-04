

We expect it to perform the following steps:

  1. Line up the gripper above the door handle, roughly as seen from the side.
  2. Drop the gripper around the door handle.
  3. Push the door closed.

```
# door-close: push the door closed to the target location
def door_close(robot):
    Steps:
      1. Line up the gripper above the door handle, roughly as seen from the side.
      2. Drop the gripper around the door handle.
      3. Push the door closed.
    # If the robot's gripper is not near the door handle, move it to the door handle.
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")

    # If the door is aligned with the gripper as seen from in front, we can push the door closed.
    if check("the robot's gripper is forward aligned with door handle"):
        robot.push("door closed")
```

In this one, check the orientation of the gripper.
The robot's gripper can be "around", "in front of", or "vertically aligned with" an object.

- Check the orientation of the gripper:
```
robot.gripper_orientation
    'above' - gripper is above
    'around' - gripper is around
    'right' - gripper is right of
    'below' - gripper is below
    'in front' - gripper is in front
    'left' - gripper is left of
    'vertical' - gripper is vertically aligned with
    'on' - gripper is on top of
```

## Scene

- The world has a door and a door handle.
- The robot has a gripper.

- At the beginning of the scene, the door and door handle are at their default locations.
- The robot is at a random location.
- The robot's gripper has a random orientation.
- The door is closed.

## Goal

The goal of the scene is for the robot's gripper to be in front of the door handle.

## Rewards

- The reward is -1 at each step.

'''

# Task 5 code

# door-close: push the door closed to the target location
def door_close(robot):
    Steps:
      1. Line up the gripper above the door handle, roughly as seen from the side.
      2. Drop the gripper around the door handle.
      3. Push the door closed.
 