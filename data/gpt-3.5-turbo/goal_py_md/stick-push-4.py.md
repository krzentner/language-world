# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    # Steps:
    # 1. Put the gripper above the stick
    # 2. Drop the gripper around the stick
    # 3. Close the gripper around the stick
    # 4. Move the gripper to the thermos
    # 5. Line up the gripper with the stick
    # 6. Pick up the stick
    # 7. Slide the stick towards the thermos
    # 8. Push the thermos towards the target location
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("above the stick")
    if check("the robot's gripper is not around the stick and the robot's gripper is open"):
        robot.move_gripper("near the stick", close_gripper=True)
    if check("the robot's gripper is near the stick and the robot's gripper is closed"):
        robot.move_gripper("near the thermos")
    if check("the robot's gripper is not aligned with the stick and the stick is below the robot's gripper"):
        robot.move_gripper("aligned with the stick")
    if check("the robot's gripper is aligned with the stick and the robot's gripper is closed"):
        robot.move_gripper("above the stick")
    if check("the robot's gripper is above the stick and the stick is below the robot's gripper"):
        robot.move_gripper("above the thermos")
    if check("the robot's gripper is above the thermos"):
        robot.move_gripper("in front of the thermos")
    if check("the robot's gripper is in front of the thermos"):
        robot.move_gripper("around the thermos")
    if check("the robot's gripper is around the thermos"):
        robot.move_gripper("near the target location")
    if check("the robot's gripper is near the target location"):
        robot.move_gripper("horizontally aligned with the thermos")
    if check("the robot's gripper is horizontally aligned with the thermos"):
        robot.move_gripper("above the thermos")
    if check("the robot's gripper is above the thermos"):
        robot.move_gripper("almost around the stick")
    if check("the robot's gripper is almost around the stick"):
        robot.move_gripper("around the stick, with the stick trapped inside")
    if check("the gripper is trapping the stick"):
        robot.move_gripper("in front of the target location")
    if check("the gripper is in front of the target location"):
        robot.move_gripper("above the target location")
    if check("the gripper is above the target location"):
        robot.move_gripper("