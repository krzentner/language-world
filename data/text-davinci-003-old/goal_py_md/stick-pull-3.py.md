

The program should look like this:
```
# stick-pull: use the stick to pull the thermos to the target location
# def stick_pull(robot):
    # Steps:
    #  1. Put gripper above the top of the stick
    #  2. Grab the stick with the gripper
    #  3. Pull the stick towards the target location
    #  4. Release the stick
    # Put the robot's gripper above the top of the stick.
    if check("the robot's gripper is not above the top of the stick"):
        robot.move_gripper("above the top of the stick")
    # Grab the stick with the gripper
    if check("the robot's gripper is not around the stick and the robot's gripper is open"):
        robot.move_gripper("around the stick", close_gripper=True)
    # Pull the stick towards the target location
    if check("the robot's gripper is around the stick and the the stick is not close to the target location"):
        robot.move_gripper("towards the target location")
    # Release the stick
    if check("the stick is close to the target location"):
        robot.move_gripper("near the target location", open_gripper=True)
```