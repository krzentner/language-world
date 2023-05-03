

Then continue with the code:

```
    # Steps:
  1. Put gripper above the door handle
  2. Drop gripper around the door handle
  3. Move the robot's gripper to line up with the door handle dial
  4. Turn the dial clockwise to unlock the door
 
    # First, even though this is a small task, let's move the robot's gripper
    # above the door handle just to be safe.
    if check("the robot's gripper is not above the door handle"):
        robot.move_gripper("above the door handle")
    # Now that the gripper is above the door handle, let's make sure to get it
    # around the handle so that it has grip.
    if check("the robot's gripper is not around door handle and the robot's gripper is open"):
        robot.move_gripper("around the door handle", close_gripper=True)
    # Once the gripper has a grip on the door handle, we can align it with the dial.
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is closed"):
        robot.move_gripper("left of handle dial")
    # With the gripper lined up with the dial, we can turn it to unlock the door.
    if check("the robot's gripper is lined up with handle dial"):
        robot.move_gripper("turn handle clockwise")
```