```
# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Move the gripper and stick to the top of the thermos
    #  4. Push the thermos to the goal
    # First, put the gripper above the stick.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.move_gripper("vertically aligned with the stick")
    # Once the gripper is above the stick, grab it.
    if check("the robot's gripper is vertically aligned with the stick and the gripper is open"):
        robot.move_gripper("around the stick", close_gripper=True)
    # Once the gripper is around the stick, move it to the top of the thermos.
    if check("the robot's gripper is around the stick and the robot's gripper is not vertically aligned with the top of the thermos"):
        robot.move_gripper("vertically aligned with the top of the thermos")
    # Once the gripper is over the top of the thermos, push the thermos to the goal.
    if check("the robot's gripper is vertically aligned with the top of the thermos and the gripper is around the stick"):
        robot.move_gripper("near the goal")