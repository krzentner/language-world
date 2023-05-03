

Then add the code:

```
  # Steps:
  #  1. Put gripper left of the door handle
  #  2. Push down on the handle from the side
  # First, put the gripper roughly left of the door handle so that we don't
  # bump it while trying to push it down.
  if check("the robot's gripper is not left of the door handle"):
      robot.move_gripper("left of the door handle")
  # If the door handle is left of the robot's gripper, push down on the handle.
  if check("the door handle is left of the robot's gripper"):
      robot.move_gripper("vertically aligned with the door handle", close_gripper=True)
```