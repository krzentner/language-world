

The goal is to grab the mug safely and be able to move it to the target location.

Steps:
1. Put the gripper above the mug
2. Drop the gripper around the mug
3. Close the gripper around the mug
4. Move the mug to the target location

We should put the gripper near the mug, but not so near that it bumps the mug while trying to grab it.

```
# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    # Steps:
    #  1. Put gripper above mug
    #  2. Drop gripper around mug
    #  3. Close gripper around mug
    #  4. Move mug to target location
    # First, put the gripper safely above the mug.
    if check("the robot's gripper is not above mug"):
        robot.move_gripper("above the mug")
    # If the mug is out of the gripper's reach, put it closer by dropping the
    # gripper around the mug.
    if check("the robot's gripper is not around mug and the robot's gripper is open"):
        robot.move_gripper("near the mug", close_gripper=True)
    # If the gripper is near the mug and open, grab it by closing the gripper.
    if check("the robot's gripper is around mug and the robot's gripper is closed"):
        robot.move_gripper("above the target location")