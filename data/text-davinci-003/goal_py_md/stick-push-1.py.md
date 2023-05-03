

Steps:
  1. Put gripper above the stick
  2. Grab the stick with the gripper
  3. Push the thermos by pushing the stick

# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    # First, put the gripper above the stick.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.move_gripper("vertically aligned with the stick")
    # Once the gripper is above the stick, drop it around the stick.
    if check("the robot's gripper is not around the stick"):
        robot.move_gripper("around the stick", close_gripper=True)
    # Once the gripper is around the stick, the robot can move it to the
    # thermos.
    if check("the robot's gripper is around the stick"):
        robot.move_gripper("near the thermos")
    # Once the robot is near the thermos, the robot can move the stick to push
    # the thermos to the target location.
    if check("the robot's gripper is near the thermos"):
        robot.move_gripper("forward aligned with the thermos")