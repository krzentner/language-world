

Steps:
1. Put gripper above the stick
2. Drop gripper around the stick
3. Pull the stick towards the target location
4. Move the stick until the thermos is at the target location

# stick-pull: use the stick to pull the thermos to the target location
# def stick_pull(robot):
    # Steps:
    #  1. Put gripper above the stick
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.move_gripper("vertically aligned with the stick")
    #  2. Drop gripper around the stick
    if check("the robot's gripper is not around the stick"):
        robot.move_gripper("around the stick")
    #  3. Pull the stick towards the target location
    if check("the robot's gripper is around the stick"):
        robot.move_gripper("near the target location")       
    #  4. Move the stick until the thermos is at the target location
    if check("the thermos is not near the target location"):
        robot.move_gripper("near the thermos")