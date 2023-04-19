

Steps: 
1. Put gripper above mug
2. Drop gripper around mug
3. Close gripper around mug
4. Pull mug to target location

``` 
# coffee-pull: grab the mug and pull it to the target location
# def coffee_pull(robot):
    # Steps:
    #  1. Put gripper above mug
    #  2. Drop gripper around mug
    #  3. Close gripper around mug
    #  4. Pull mug to target location
    # First, put the gripper roughly above mug, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the mug"):
        robot.move_gripper("above the mug")
    # If the gripper isn't around the mug, put it around the mug.
    if check("the robot's gripper is not around mug and the robot's gripper is open"):
        robot.move_gripper("near the mug", close_gripper=True)
    # If the gripper is near the mug and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above mug and the robot's gripper is closed"):
        robot.move_gripper("near the target location")
    # Once the gripper is around the mug, we can just pull the mug
    # to the target location.
    if check("the robot's gripper is around mug"):
        robot.move_gripper("left of the target location")