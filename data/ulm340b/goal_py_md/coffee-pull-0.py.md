

You can edit your solution by pasting it into this box:

```
# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    # Steps:
    #  1. Put gripper above mug
    #  2. Grab the mug with the gripper
    #  3. Move the mug towards you
    # First, put the gripper above the mug.
    if check("the robot's gripper is not vertically aligned with the mug"):
        robot.move_gripper("vertically aligned with the mug")
    # If the gripper isn't around the mug, put it around the mug.
    if check("the robot's gripper is not around the mug and the robot's gripper is open"):
        robot.move_gripper("above the mug", close_gripper=True)
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is around the mug"):
        robot.move_gripper("vertically aligned with the mug")

```

You can call the `robot.move_gripper(description, close_gripper=False)` function to control the gripper.
The `description` argument is a human-readable description of the robot's gripper state:

| Description | Meaning       |
|-------------|---------------|
| left of the door handle | The robot's gripper should be left of the door handle, as seen from the left of the screen. |
| vertically aligned with the door handle | The robot's gripper should be vertically aligned with the door handle, as seen from the top of the screen. |
| almost vertically aligned with the door handle | The robot's gripper should be almost vertically aligned with the door handle, as seen from the top of the screen. |
| near the door handle | The robot's gripper should be near the door handle. |
| around the door handle | The robot's gripper should be around the door handle. |
| forward aligned with the door handle | The robot's gripper should be forward aligned with the door handle, as seen from the top of the screen. |
| above the door handle | The robot's gripper should be above the door handle, as seen from the top of the screen. |
| left of the drawer handle | The robot's gripper should be left of the drawer handle, as seen from the left of the screen. |
| vertically aligned with the drawer handle |