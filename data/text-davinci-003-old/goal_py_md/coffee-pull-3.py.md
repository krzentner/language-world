

Then,

```
# coffee-pull: grab the mug and pull it to the target location
# def coffee_pull(robot):
    # Steps:
    #  1. Put gripper left of mug
    #  2. Grab mug with gripper 
    #  3. Pull mug to the target location
    # First, we want to move the gripper left of the mug, so that we don't
    # accidentally click it while we're trying to grab it.
    if check("the robot's gripper is not left of mug"):
        robot.move_gripper("left of the mug")
    # If the mug is now left of the robot's gripper, close the gripper around the
    # mug.
    if check("the robot's gripper is open and the mug is left of the robot's gripper"):
        robot.move_gripper("around the mug", close_gripper=True)
    # Once we have the mug securely in the gripper, we can just pull it to the
    # target location.
    if check("the robot's gripper is around mug"):
        robot.move_gripper("near the target location")

```