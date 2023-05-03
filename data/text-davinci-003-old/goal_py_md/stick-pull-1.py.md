

The steps of the program should be:
1. Put gripper above the stick
2. Drop gripper onto stick
3. Pull the stick towards the thermos
4. Put gripper in line with the thermos
5. Push the thermos to the target location

Solution: 
# stick-pull: use the stick to pull the thermos to the target location
# def stick_pull(robot):
    # Steps:
    # 1. Put gripper above the stick
    if check("the robot's gripper is not vertically aligned with stick"):
        robot.move_gripper("vertically aligned with stick")
    # 2. Drop gripper onto stick
    if check("the robot's gripper is vertically aligned with stick and the robot's gripper is not around stick"):
        robot.move_gripper("around the stick")
    # 3. Pull the stick towards the thermos
    if check("the robot's gripper is around stick"):
        robot.move_gripper("towards the thermos")
    # 4. Put gripper in line with the thermos
    if check("the robot's gripper is not forward aligned with thermos"):
        robot.move_gripper("forward aligned with thermos")
    # 5. Push the thermos to the target location
    if check("the robot's gripper is forward aligned with thermos"):
        robot.move_gripper("near the target location")